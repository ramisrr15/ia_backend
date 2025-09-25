from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/diagnostico", methods=["POST"])
def diagnostico():
    resumen = request.json["resumen"]

    headers = {"Authorization": "Bearer TU_API_KEY"}  # Hugging Face API Key
    payload = {"inputs": resumen}

    response = requests.post(
        "https://api-inference.huggingface.co/models/google/flan-t5-large",
        headers=headers,
        json=payload
    )

    try:
        respuesta = response.json()[0]["generated_text"]
    except:
        respuesta = "No se pudo obtener una respuesta de la IA."

    return jsonify({"respuesta": respuesta})
