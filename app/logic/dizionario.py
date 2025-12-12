
from app.logic.validazione import validazione

def dizionario_nucleotidi(sequenza):
 sequenza_valida = validazione(sequenza)
 if sequenza_valida is None:
        return None
 conteggio = {"A": 0, "T": 0, "C": 0, "G": 0}
 for base in sequenza:
    conteggio[base] += 1
 return conteggio