from flask import Flask, request, jsonify
from src.components.prediction import PredictionPipeline
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data["text"]
    prediction=PredictionPipeline()
    summary = prediction.predict(text)

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(debug=True)