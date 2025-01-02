from flask import Flask, request, send_file
import cv2
import numpy as np
import io
from utils.image_processing import process_image

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    if 'image' not in request.files:
        return {"error": "Nenhuma imagem foi enviada."}, 400

    file = request.files['image']
    file_stream = file.read()

    # Ler a imagem enviada
    npimg = np.frombuffer(file_stream, np.uint8)
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Processar a imagem
    final_image = process_image(image)

    # Converter a imagem final para um arquivo de resposta
    _, buffer = cv2.imencode('.png', final_image)
    response_stream = io.BytesIO(buffer)

    return send_file(response_stream, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
