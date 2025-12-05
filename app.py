from flask import Flask, render_template, request, jsonify
from src.components.prediction import PredictionPipeline
from flask_cors import CORS


app = Flask(__name__, template_folder="src/frontend",
            static_folder="src/frontend"
        )
            

CORS(app) 

prediction=PredictionPipeline()

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")
    max_length = data.get("max_length", 128)
    num_beams = data.get("num_beams", 8)

    summary = prediction.predict(text,num_length=max_length,beam_length=num_beams)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)