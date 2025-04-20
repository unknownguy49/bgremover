from flask import Flask, request, jsonify
from rembg import remove
import os
from io import BytesIO
from PIL import Image
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return "Background Remover API is working!"

@app.route('/remove-background/', methods=['POST'])
def remove_background():
    try:
        # Get the uploaded file
        file = request.files.get('image')

        if not file:
            return jsonify({"status": "error", "message": "No image file uploaded."}), 400

        # Read the image and remove the background
        input_image = Image.open(file.stream)
        output_image = remove(input_image)

        # Convert the output image to base64
        buffered = BytesIO()
        output_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        # Return the base64 encoded image as JSON response
        return jsonify({"status": "success", "cleaned_image": img_str})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 8000))
