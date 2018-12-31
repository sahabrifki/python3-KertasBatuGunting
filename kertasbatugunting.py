from random import randint
while True:
    try:
        playerInput = int(input("masukan pilihan anda 1. kertas 2. batu 3. gunting : "))
    except ValueError:
        print ("MAAF, input harus merupakan angka 1,2 atau 3")
        continue
    if playerInput > 3:
        print("anda harus memilih angka 1 2 atau 3")
    else:
        break

if playerInput == 1:
    playerChoice = "Kertas"
elif playerInput == 2:
    playerChoice = "Batu"
elif playerInput == 3:
    playerChoice = "Gunting"
    
random = randint(1,3)
if random == 1:
    computer = "Kertas"
elif random == 2:
    computer = "Batu"
elif random == 3:
    computer = "Gunting"

print(playerChoice, "VS", computer)



if playerChoice == computer:
    print ("permainan seri")

elif playerChoice == "Kertas":
    if computer == "Batu":
        print ("Player Win")
    elif computer == "Gunting":
        print ("Computer Win")


elif playerChoice == "Batu":
    if computer == "Kertas":
        print ("Computer Win")
    elif computer == "Gunting":
        print ("player win")

elif playerChoice == "Gunting":
    if computer == "Kertas":
        print ("Player Win")
    elif computer == "Batu":
        print ("Computer Win")