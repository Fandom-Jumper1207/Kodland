for i in range(10):
    meme_dict = {"CRINGE": "Algo excepcionalmente raro o embarazoso","LOL": "Una respuesta común a algo gracioso","CREEPY": "Algo raro/siniestro/extraño", "SLAY": "Algo increíble o cool", "RIZZ": "Nivel de atractivida", "AURA": "Nivel de cool", "DELULU": "Loco/a", "NO CAP": "Mentira/falso"}
    
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("No se encontró su palabra.")
