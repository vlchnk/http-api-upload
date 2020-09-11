from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage
import os
import hashlib

app = Flask(__name__)

UPLOAD_FOLDER = './store'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def upload_site():
    return "Hello"


@app.route('/upload', methods=['GET', 'PUT'])
def upload_file():
    if request.method == 'PUT':
        f = request.files['file']
        hashName = secure_filename(f.filename)
        filename = hashlib.md5(hashName.encode()).hexdigest()
        path = str(filename[:2])

        try:
            dirPath = "./store/" + path
            os.makedirs(dirPath)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

        try:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], path, filename))
            return filename
        except:
            return 'Bad :c'


@app.route('/download/<path:hash>', methods=['GET', 'POST'])
def download(hash):
    # uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    try:
        uploads = './store/' + hash[:2] + "/" + hash
        return send_file(uploads, as_attachment=True)
    except:
        payload = {'status': '404', 'error': 'File not found'}
        return payload


if __name__ == '__main__':
    app.run(debug=True)
