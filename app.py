from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import os
import hashlib

app = Flask(__name__)

UPLOAD_FOLDER = './store'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['GET', 'PUT'])
def upload_file():
    if request.method == 'PUT':
        f = request.files['file']
        hashName = secure_filename(f.filename)
        filename = hashlib.md5(hashName.encode()).hexdigest()
        path = str(filename[:2])

        # Create dir
        try:
            dirPath = f"./store/{path}"
            os.makedirs(dirPath)
        except OSError:
            print(f"Creation of the directory {path} failed")
        else:
            print(f"Successfully created the directory {path}")

        # Save file
        try:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], path, filename))
            return filename
        except:
            return 'Bad :c'


@app.route('/download/<path:hash>', methods=['GET', 'POST'])
def download(hash):
    try:
        pathFile = f'./store/{hash[:2]}/{hash}'
        return send_file(pathFile, as_attachment=True)
    except:
        payload = {'status': '404', 'error': 'File not found'}
        return payload


@app.route('/delete/<path:hash>', methods=['DELETE'])
def delete(hash):
    try:
        pathFile = f'./store/{hash[:2]}/{hash}'
        os.remove(pathFile)
        return {'status': '200', 'description': f'File {hash} deleted'}
    except:
        payload = {'status': '404', 'error': 'File not found'}
        return payload


@app.errorhandler(404)
def not_found(error):
    return {'status': '404'}


if __name__ == '__main__':
    app.run()
