from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import os
import hashlib

app = Flask(__name__)

UPLOAD_FOLDER = './store'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['PUT'])
def upload_file():
    if request.method == 'PUT':
        f = request.files['file']
        hashname = secure_filename(f.filename)
        filename = hashlib.md5(hashname.encode()).hexdigest()
        path = str(filename[:2])

        # Create dir
        try:
            dirpath = f"./store/{path}"
            os.makedirs(dirpath)
        except OSError:
            print(f"Creation of the directory {path} failed")
        else:
            print(f"Successfully created the directory {path}")

        # Save file
        try:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], path, filename))
            return {'status': '200', 'hash': f'{filename}'}
        except:
            return {'status': '400', 'error': 'Something went wrong'}
    else:
        return {'status': '400', 'error': 'Something went wrong'}


@app.route('/download/<path:hash>')
def download(hash):
    try:
        pathfile = f'./store/{hash[:2]}/{hash}'
        return send_file(pathfile, as_attachment=True)
    except:
        payload = {'status': '404', 'error': 'File not found'}
        return payload


@app.route('/delete/<path:hash>', methods=['DELETE'])
def delete(hash):
    if request.method == 'DELETE':
        try:
            pathfile = f'./store/{hash[:2]}/{hash}'
            os.remove(pathfile)
            return {'status': '200', 'file': hash}
        except:
            payload = {'status': '404', 'error': 'File not found'}
            return payload
    else:
        return {'status': '400', 'error': 'Something went wrong'}


@app.errorhandler(404)
def not_found():
    return {'status': '404'}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
