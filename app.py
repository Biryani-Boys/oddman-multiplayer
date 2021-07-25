from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello World!'

@app.route("/files/<string:filename>+<string:accmode>+<string:txtinput>")
def files(filename,accmode,txtinput):
    files = open(filename,accmode) 
    if accmode == 'r':
        for line in files:
            pass
        return line
    elif accmode == 'w':
        files.write(txtinput)
        return 'success'
    elif accmode == 'a':
        files.write(txtinput)
        return 'success'
    return 'Error Occured'

@app.route("/delete/<string:filename>")
def delete_file(filename):
    os.remove(filename)
    return 'File Deleted'

if __name__ == '__main__':
    app.run(debug=True)