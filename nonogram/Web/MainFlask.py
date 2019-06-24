import os
from NonoPy.nonogram import *
from flask import Flask, request, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/temarales/PycharmProjects/nonogram/uploaded_files'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MainFlask = Flask(__name__)
MainFlask.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@MainFlask.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(MainFlask.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@MainFlask.route('/uploads/<filename>')
def uploaded_file(filename):
    n = nonogram.Nonogram(UPLOAD_FOLDER + "/" + filename)
    n.convert(26, 29, 550, UPLOAD_FOLDER + "/" + filename)
    return send_from_directory(MainFlask.config['UPLOAD_FOLDER'],
                               filename + "_answer.png")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    import sys
    print(sys.path)
    MainFlask.run()