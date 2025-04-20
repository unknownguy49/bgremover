from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/remove-bg/', methods=['POST'])
def remove_bg():
    # Get the uploaded file from the request
    file = request.files['file']
    contents = file.read()

    # Remove the background using rembg
    result = remove(contents)

    # Return the processed image as a response
    return send_file(BytesIO(result), mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
