from app.logic.conteggio import conteggio_nucleotidi

def percentuale_coppie(sequenza):
    if sequenza is None:
        return "Sequenza non valida"
    
    conteggio = conteggio_nucleotidi(sequenza)
    frequenza_a = conteggio["A"]
    frequenza_t = conteggio["T"]
    frequenza_c = conteggio["C"]
    frequenza_g = conteggio["G"]
    percentuale_at = round((((frequenza_a+frequenza_t)/len(sequenza))*100), 2)
    percentuale_cg = round((((frequenza_c+frequenza_g)/len(sequenza))*100), 2)
    return f"La percentuale di AT è : {percentuale_at}%, quella di CG è : {percentuale_cg}%"
