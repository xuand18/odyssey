from flask import Flask, render_template, request 
import io
from google.cloud import vision
from google.cloud.vision import types

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.files['file']
    client = vision.ImageAnnotatorClient()

    response = client.text_detection(image=text)
    texts = response.text_annotations

    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

if __name__ == '__main__':
    app.run(host = "0.0.0.0")


