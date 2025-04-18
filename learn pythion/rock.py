import random
store ={
    1: "Rock",
    2: "Paper", 
    3: "Scissors"
}
print("==================Rock Paper Scissors===================")
select = int(input("Select your choice: 1) Rock 2) Paper 3) Scissors\n"))
computer = random.randint(1,3)
print(f"you selected {store[select]}")
print(f"computer selected {store[computer]}")
if select == computer:
    print("It's a tie!")
elif select == 1 and computer == 2:
    print("You lose!")
elif select == 1 and computer == 3:
    print("You win!")
elif select == 2 and computer == 1:
    print("You win!")
elif select == 2 and computer == 3:
    print("You lose!")
elif select == 3 and computer == 1:
    print("You lose!")
elif select == 3 and computer == 2:
    print("You win!")   
elif select == 4:
    print("Goodbye!")