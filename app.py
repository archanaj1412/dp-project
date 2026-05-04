
from flask import Flask, render_template, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("tiny")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    path = "temp_audio.wav"
    file.save(path)

    result = model.transcribe(path)

    return jsonify({
        "transcript": result["text"],
        "language": result["language"]
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)), debug=False)
