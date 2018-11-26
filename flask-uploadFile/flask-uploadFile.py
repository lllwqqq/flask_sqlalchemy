from flask import Flask,request,render_template,send_from_directory
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
from forms import UploadForm

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'files')

@app.route('/upload/',methods=['GET','POST'])
def uploadFile():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        form = UploadForm(CombinedMultiDict([request.form,request.files]))
        if form.validate():
            desc = request.form.get('desc')
            avatar = request.files.get('avatar')
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(UPLOAD_PATH,avatar.filename))
            return '文件上传成功!!!'
        else:
            print(form.errors)
            return 'Failed!!'


@app.route('/files/<filename>/')
def get_file(filename):
    return send_from_directory(UPLOAD_PATH,filename)


if __name__ == '__main__':
    app.run()
