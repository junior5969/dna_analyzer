
def cerca_motivo(sequenza, motivo):
 lista_posizioni= []
 posizioni_motivo = {motivo: lista_posizioni}
 start = 0

 while True:
    indice = sequenza.find(motivo, start)

    if indice == -1:
        break  
 
    posizione=indice+1
    if indice not in lista_posizioni:
        lista_posizioni.append(posizione)
    
    start = indice + 1
    stringa_posizioni=", ".join([str(x) for x in lista_posizioni])

 return f"Il motivo {motivo} è stato trovato nelle seguenti posizioni: {stringa_posizioni}"
