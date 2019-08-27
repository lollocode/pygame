import os
print('Salve, benvenuto al supermercato! \n')
print('accedi con le tue credenziali \n')

spesa = {'arance':1, 
        'limoni':2, 
        'uva':3, 
        'pesche':4} 

carrello = {
  
}

def aggiungo():
  os.system('cls')
  visualizza(spesa)
  novità = input('cosa aggiungiamo oggi?')
  if novità in spesa:
    print('ce lo abbiamo già')
  else: 
    costo = int(input('a che prezzo?'))
    spesa[novità]= costo
  visualizza(spesa)
  
def cambio():
  os.system('cls')
  visualizza(spesa)
  cambio= input('di quale alimento cambiamo il prezzo?')
  if cambio in spesa:
    costo2 = input('a quale prezzo?')
    spesa[cambio] = costo2
    visualizza(spesa)
  else:
    print('Non è in magazzino capo!')

def visualizza(lista):
  for x,y in lista.items():
    print(x,y)


with open('pypy.txt', 'r') as file:
  while True:
    admin = file.readline()
    lista = admin.split()
    break
file.close()

user = str(input('username:'))
password = str(input('password:'))

if user == lista[0] and password == lista[1] :
  print('Bentornato amministratore')
  while True:
    print('0 per aggiungere un prodotto, 1 per cambiare un prezzo, 2 per terminare le operazioni')
    azione2 = int(input('cosa vuoi fare?'))
    if azione2 == 0:
      aggiungo()
    elif azione2 == 1:
      cambio()
    elif azione2 == 2:
      exit('A domani capo!')
else:
  print('Benvenuto')






def visualizza(lista):
  for x,y in lista.items():
    print(x,y)

def acquista():
  os.system('cls')
  print('questo è quello che offriamo',)
  visualizza(spesa)
  acquisto = input('cosa ti interessa? ')
  if acquisto in spesa:
    quantità= int(input('quante ne vuoi? '))
    carrello[acquisto] = 0
    carrello[acquisto] = carrello[acquisto] + quantità
    
  
    visualizza (carrello)
  else:
    print('Non è disponibile')


def rimuovi():
  os.system('cls')
  print('questo è quello che hai comprato ',)
  visualizza(carrello)
  rimozione = input('cosa vuoi rimuovere? ')
  if rimozione in carrello and carrello[rimozione] > 0:
    numerorim = int(input('quante ne vuoi rimuovere? '))
    if carrello[rimozione] - numerorim < 0:
      print('non puoi farlo')
    else:
      carrello[rimozione] -= numerorim
      
    visualizza(carrello)
  else:
    print('Non è nel carrello')

def prezzo():
  ammontare = 0
  for x,y in carrello.items():
    ammontare = ammontare + y * spesa[x]
  print('hai speso ', ammontare, 'euro')

while True:
  print('0 per acquistare, 1 per rimuovere, 2 per terminare, 3 per resoconto')
  azione = int(input('cosa vuoi fare?'))
  
  if azione == 0 :
    acquista()
  elif azione == 1 :
    rimuovi() 
  elif azione == 2 : 
    prezzo()
    exit('arrivederci')
  elif azione == 3 :
    prezzo()


