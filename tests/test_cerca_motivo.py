from app.logic.cerca_motivo import cerca_motivo

def test_cerca_motivo():
    seq = "AATCCCGGCCC"
    motivo="CCC"
    risultato = cerca_motivo(seq, motivo)

    assert "Il motivo CCC è stato trovato nelle seguenti posizioni: 4, 9" in risultato
