from flask import Flask, render_template, request
from audio_analysis import analyze_voice

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        file = request.files["audio"]
        file_path = "uploads/" + file.filename
        file.save(file_path)

        result = analyze_voice(file_path)

    return render_template("index.html", result=result)

app.run(debug=True)
