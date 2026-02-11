import os

from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI()
model_name = "gpt-5"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static"


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        language = request.form["language"]
        file = request.files["file"]
        if file:
            filename = file.filename
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            with open("static/recording.mp3", "rb") as audio_file:
                translation = client.audio.translations.create(
                    model="whisper-1",
                    file=audio_file,
                )

                response = client.responses.create(
                    model=model_name,
                    input=[
                        {
                            "role": "system",
                            "content": f"You will be provided with a sentence in English, and your task is to translate it into {language}"
                        },
                        {
                            "role": "user",
                            "content": translation.text
                        },
                    ],
                    temparature=0,
                    max_tokens=256
                )
                return jsonify(response)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
