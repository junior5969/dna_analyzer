
def cerca_motivo(sequenza, motivo):
 posizioni = {motivo: []}
 start = 0

 while True:
    indice = sequenza.find(motivo, start)

    if indice == -1:
        break  

    if indice not in posizioni[motivo]:
        posizioni[motivo].append(indice+1)
    
    start = indice + 1

 return f"Il motivo {motivo} è stato trovato nelle seguenti posizioni {posizioni[motivo]}"
