from app.logic.conteggio import conteggio_nucleotidi

def test_conteggio_nucleotidi():
    seq = "AATCCCGG"
    risultato = conteggio_nucleotidi(seq)

    assert "L'Adenina (A) è presente 2 volte, la Timina (T) è presente 1 volte, la Guanina (G) è presente 2 volte e la Citosina (C) è presente 3 volte." in risultato
