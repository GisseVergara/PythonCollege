arr=[]
while(True):
    aux=[] #auxiliar to save [rut or ID, name, lastname] in each loop
    print("\n MENU:")
    print("1) Login user")
    print("2) Show client by rut or ID ")
    print("3) Exit")
    option=int(input("Enter option: "))
    if(option==1):
        rut=int(input("Enter rut or ID: "))
        aux.append(rut)
        name=input("Enter name: ")
        aux.append(name)
        lastname=input("Enter lastname: ")
        aux.append(lastname)
        arr.append(aux) #I keep the helper(aux) in the list(arr)

  
    if(option==2):
        rut2=int(input("Enter rut or ID to check: "))
        for i in range(len(list)):
            if(rut2==arr[i][0]): #Search in the first position [[arr[0][0],name,lastname],[arr[1][0],name2,lastname2],...]
                print(arr[i][0]) 
                print(arr[i])

    if(option==3):
        print("Bye bye!, have a nice day")
        break
    
    else:
        print("Please, choose a valid option")
        continue