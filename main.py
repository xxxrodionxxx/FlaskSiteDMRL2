from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    gifs = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.endswith('.gif')]
    return render_template('index.html', gifs=gifs)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
