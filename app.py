from flask import Flask, render_template, request
import os

app = Flask(__name__)

def classify_file(file_name):
    file_extension = file_name.split('.')[-1]
    if file_extension.lower() == 'pdf':
        return 'Top Secret'
    elif file_extension.lower() == 'docx':
        return 'Secret'
    else:
        return 'Public'

@app.route('/', methods=['GET', 'POST'])
def upload_folder():
    if request.method == 'POST':
        files = request.files.getlist('folderInput')
        file_data = []
        for file in files:
            file_name = file.filename
            classification = classify_file(file_name)
            file_data.append((file_name, classification))
        return render_template('index.html', file_data=file_data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)
    # app.run(host="127.0.0.1", port="50000", debug=True, ssl_context=('cert.pem', 'key.pem'))
