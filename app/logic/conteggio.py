from app.logic.dizionario import dizionario_nucleotidi

def conteggio_nucleotidi(sequenza):
  conteggio=dizionario_nucleotidi(sequenza)
  if conteggio is None:
    return "Sequenza non valida"
  frequenza_a=conteggio["A"]
  frequenza_t=conteggio["T"]
  frequenza_c=conteggio["C"]
  frequenza_g=conteggio["G"]
  return f"L'Adenina (A) è presente {frequenza_a} volte, la Timina (T) è presente {frequenza_t} volte, la Guanina (G) è presente {frequenza_g} volte e la Citosina (C) è presente {frequenza_c} volte."
