def validazione(sequenza):
    nucleotidi= "ATCG"
    for nucleotide in sequenza:
        if nucleotide not in nucleotidi:
            return None  
    return sequenza