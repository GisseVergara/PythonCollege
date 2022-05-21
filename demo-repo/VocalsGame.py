vocals=["a","A","e","E","i","I","o","O","u","U"]

while(True):
  cont=0
  word=input("\n Enter your word: ")
  for i in word:
    for j in vocals:
      if(i==j):
        cont=cont+1

  if(cont<=2):
    print("Your word has: ",cont,"vocals, YOU LOST ")
  if(cont>=3 and cont<=5):
    print("Your word has: ",cont,"vocals, ALMOST WIN")
  if(cont>5):
    print("Your word has: ",cont,"vocals, YOU WIN")
  
  ask=input("\n Do you want to keep playing?: (s/n)")
  if(ask=="s" or ask=="S"):
    print("...LET'S CONTINUE...")
    continue
  else:
    print("...YOU'VE ENDED THE GAME...")
    break