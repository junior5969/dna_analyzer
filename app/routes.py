from app import app
from flask import request, jsonify, render_template
from app.logic.analyzer import *

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route('/analizza', methods=['POST'])
def analizza():
    data = request.get_json()  # riceve JSON dal fetch

    if not data:
        return jsonify({"errore": "Nessun JSON ricevuto"}), 400

    sequenza = data.get("sequenza")
    azione = data.get("azione")

    if not sequenza or not azione:
        return jsonify({"errore": "Parametri mancanti"}), 400

    try:
        if azione == "conteggio":
            risultato = conteggio_nucleotidi(sequenza)
        elif azione == "percentuale":
            risultato = percentuale_coppie(sequenza)
        elif azione == "trascrizione":
            risultato = trascrizione(sequenza)
        elif azione == "traduzione":
            risultato = traduzione(sequenza)
        else:
            return jsonify({"errore": "Azione sconosciuta"}), 400

        return jsonify({"risultato": risultato})

    except ValueError as e:  # se validazione solleva ValueError
        return jsonify({"errore": str(e)}), 400
    except Exception as e:
        return jsonify({"errore": str(e)}), 500
