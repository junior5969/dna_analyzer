
from app import app
from flask import request, render_template
from app.logic.analyzer import *

@app.route('/analizza', methods=['POST'])
def analizza():
    sequenza = request.form.get("sequenza")
    azione = request.form.get("azione")

    if azione == "conteggio":
        risultato = conteggio_nucleotidi(sequenza)
        return render_template("risultato.html", conteggio=risultato)
    elif azione == "percentuale":
        risultato = percentuale_coppie(sequenza)
        return render_template("risultato.html", percentuale=risultato)
    elif azione == "trascrizione":
        risultato = trascrizione(sequenza)
        return render_template("risultato.html", sequenza_trascritta=risultato)
    elif azione == "traduzione":
        risultato = traduzione(sequenza)
        return render_template("risultato.html", sequenza_tradotta=risultato)
