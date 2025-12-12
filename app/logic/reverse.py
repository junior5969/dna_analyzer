from app.logic.validazione import validazione

def reverse(sequenza):
    sequenza_validata = validazione(sequenza)
    if sequenza is None:
        return "Sequenza non valida"

    conversione_nucleotidi = str.maketrans({
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    })
    sequenza_complementare = sequenza_validata.translate(conversione_nucleotidi)
    return sequenza_complementare
