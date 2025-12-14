from flask import Blueprint, request, jsonify
from app.logic.reverse import reverse
from app.logic.conteggio import conteggio_nucleotidi
from app.logic.percentuale import percentuale_coppie
from app.logic.trascrizione import trascrizione, trascrizione_string
from app.logic.traduzione import traduzione
from app.logic.cerca_motivo import cerca_motivo 

api = Blueprint("api", __name__)


@api.route('/analizza', methods=['POST'])
def analizza():
    data = request.get_json()  # riceve JSON dal fetch

    if not data:
        return jsonify({"errore": "Nessun JSON ricevuto"}), 400

    sequenza = data.get("sequenza")
    motivo = data.get("motivo")
    azione = data.get("azione")

    if not sequenza or not azione:
        return jsonify({"errore": "Parametri mancanti"}), 400

    try:
        if azione == "conteggio":
            risultato = conteggio_nucleotidi(sequenza)
        elif azione == "percentuale":
            risultato = percentuale_coppie(sequenza)
        elif azione == "trascrizione":
            complementare = reverse(sequenza)
            trascritta=trascrizione(sequenza)
            risultato = trascrizione_string(complementare, trascritta)
        elif azione == "traduzione":
            risultato = traduzione(sequenza)
        elif azione == "motivo":
            risultato = cerca_motivo(sequenza,motivo)
        else:
            return jsonify({"errore": "Azione sconosciuta"}), 400

        return jsonify({"risultato": risultato})

    except ValueError as e:  # se validazione solleva ValueError
        return jsonify({"errore": str(e)}), 400
    except Exception as e:
        return jsonify({"errore": str(e)}), 500
