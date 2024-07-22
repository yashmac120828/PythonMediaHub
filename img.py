from flask import Flask,render_template,request,send_from_directory,redirect,url_for
import os
app=Flask(__name__,template_folder='template_files')
UPLOAD_FOLDER ='uploads'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER,exist_ok=True)
@app.route("/")
def index():
    filenames=os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template("img.html",filenames=filenames)
@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file found"
    file=request.files['file']
    if file.filename=="":
        return "No selected files"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
    return redirect(url_for('index'))
@app.route('/download/<filename>')
def download_file(filename):
     return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
if __name__=='__main__':
     app.run(debug=True)