from flask import Flask, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os
import hashlib

app = Flask(__name__)

UPLOAD_FOLDER = './store'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['PUT'])
def upload_file():
    f = request.files['file']
    hashname = secure_filename(f.filename)
    filename = hashlib.sha256(hashname.encode()).hexdigest()
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
        return jsonify(hash=filename)
    except:
        return jsonify(error='Something went wrong'), 404


@app.route('/download/<path:hash>')
def download(hash):
    try:
        pathfile = f'./store/{hash[:2]}/{hash}'
        return send_file(pathfile, as_attachment=True)
    except:
        return jsonify(error='File not found'), 404


@app.route('/delete/<path:hash>', methods=['DELETE'])
def delete(hash):
    try:
        pathfile = f'./store/{hash[:2]}/{hash}'
        os.remove(pathfile)
        return jsonify(hash=hash)
    except:
        return jsonify(error='File not found'), 404


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error=str(e)), 405


@app.errorhandler(500)
def server_error(e):
    return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')