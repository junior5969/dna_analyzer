from app.logic.percentuale import percentuale_coppie

def test_percentuale():
    seq="ATTGCTT"
    risultato=percentuale_coppie(seq)
    assert "La percentuale di AT è del 71% mentre quella di CG è del 29%" in risultato
