from app.logic.validazione import validazione

def conteggio_nucleotidi(sequenza):
    if sequenza is None:
        return "Sequenza non valida"
    conteggio = {}
    sequenza = validazione(sequenza)
    for nucleotide in sequenza:
        if nucleotide in conteggio:
            conteggio[nucleotide] += 1
        else:
            conteggio[nucleotide] = 1
    for n in conteggio:
        frequenza_a=conteggio["A"]
        frequenza_t=conteggio["T"]
        frequenza_c=conteggio["C"]
        frequenza_g=conteggio["G"]
    return f"L'Adenina (A) è presente {frequenza_a} volte, la Timina (T) è presente {frequenza_t} volte, la Guanina (G) è presente {frequenza_g} volte e la Citosina (C) è presente {frequenza_c} volte."
