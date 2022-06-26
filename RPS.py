import random

## similar a abbey creo un diccionario para asignar si cadena esta o no entre las posibilidades
cadena={}
def player(prev_opponent_play,
          opponent_history=[]
          ):

      
    
    n = 4

    hist = opponent_history
    opponent_history.append(prev_opponent_play)
    
    if len(hist) <= n:
      prediction = random.choice(["R","P","S"])
     
    if len(hist) > n:
        pattern = "".join(hist[-n:]) ### cadena  de largo n
        # print("".join(hist[-(n + 1):]))
        # print(pattern)
        if "".join(hist[-(n + 1):]) in cadena.keys():
            cadena["".join(hist[-(n + 1):])] += 1 ## cuantas veces aparece la cadena le sumo 1
        else:
            cadena["".join(hist[-(n + 1):])] = 1  ## sino esta antes en cadena es que no aparecio antes

        posibles = [pattern + "R", pattern + "P", pattern + "S"]
        # print(cadena.keys())
        ### sino no estan los posibles en el diccionario cadena le pongo 0
        for i in posibles:
            if not i in cadena.keys():
                cadena[i] = 0
        
        # print(posibles)
        # print(posibles.keys(),posibles.values())
        ### retorna el maximo de posibles en la cadena, si hay varios maximos va a devolver el primero que encuentre
        prediction = max(posibles, key=lambda key: cadena[key])[-1:]
        

       

    
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
    
    