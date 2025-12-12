from app.logic.dizionario import dizionario_nucleotidi

def percentuale_coppie(sequenza):
    conteggio=dizionario_nucleotidi(sequenza)
    if conteggio is None:
      return "Sequenza non valida"
    frequenza_a=conteggio["A"]
    frequenza_t=conteggio["T"]
    frequenza_c=conteggio["C"]
    frequenza_g=conteggio["G"]
    percentuale_at = round((((frequenza_a+frequenza_t)/len(sequenza))*100), 2)
    percentuale_cg = round((((frequenza_c+frequenza_g)/len(sequenza))*100), 2)
    return f"La percentuale di AT è : {percentuale_at}%, quella di CG è : {percentuale_cg}%"
