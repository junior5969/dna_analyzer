from app.logic.analyzer import validazione, reverse, conteggio_nucleotidi, percentuale_coppie, trascrizione, traduzione
from app.logic.codons import codoni
from app.logic.amino_acids import amminoacidi

# sequenza = input("Inserisci la sequenza DNA: ").upper()
# count = conteggio_nucleotidi(sequenza)
# print(count)


# sequenza = input("Inserisci la sequenza DNA: ").upper()
# percentuale = percentuale_coppie(sequenza)
# print(percentuale)

# sequenza = input("Inserisci la sequenza DNA: ").upper()
# trascritta = trascrizione(sequenza)
# print(trascritta)

# sequenza = input("Inserisci la sequenza DNA: ").upper()
# sequenza_verificata=validazione(sequenza)
# print(sequenza_verificata)

# sequenza = input("Inserisci la sequenza DNA: ").upper()
# complementare = reverse(sequenza)
# print(complementare)

# sequenza = input("Inserisci la sequenza DNA: ").upper()
# sequenza_tradotta=traduzione(sequenza)
# print(sequenza_tradotta)

# sequenza = input("Inserisci la sequenza DNA: ").upper()
# sequenza_corretta=trascrizione(sequenza)
# codone_di_inizio="AUG"
# inidice_inizio=sequenza_corretta.find(codone_di_inizio)
# print(f" sequenza trascritta {sequenza_corretta}, indice : {inidice_inizio}, sequenza: {sequenza_corretta[inidice_inizio:]}")

# amminoacido = input("Inserisci la sequenza DNA: ")
# for key in amminoacidi.keys():
#  if amminoacido == key:
#   print(amminoacidi[key])
#   break
# else:
#   print("Amminoacido non trovato")



sequenza = input("Inserisci la sequenza DNA: ").upper()
sequenza_trascritta = trascrizione(sequenza)

codone_di_inizio="AUG"
inidice_codone_di_inizio=sequenza_trascritta.find(codone_di_inizio)
sequenza_da_tradurre=sequenza_trascritta[inidice_codone_di_inizio:]
triplette = []
for nucleotide in range(0, len(sequenza_da_tradurre), 3):
  triplette.append(sequenza_da_tradurre[nucleotide:nucleotide+3])

risultati = []
  
for t in triplette:
  fermati = False
  for codone in codoni.values():
   for tripletta in codone:
    if t == tripletta:
        amminoacido = list(codoni.keys())[list(codoni.values()).index(codone)]
        risultati.append(amminoacido)
        if amminoacido == "Stop":
         fermati = True
         break
    if fermati:
        break
  if fermati:
     break
proteina = []
for key in amminoacidi.keys():
   for a in risultati:
    if a == key:
     sigla_amminoacido=(amminoacidi[key])
     proteina.append(sigla_amminoacido)
proteina_str = ''.join(proteina)
print(f"La sequenza complementare è {sequenza_trascritta} quella da tradurre è {sequenza_da_tradurre} e le triplette sono {triplette} e gli amminoacidi {proteina_str}")