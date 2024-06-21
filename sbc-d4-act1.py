#HUMPYANG
from random import randint

user_choice = int(input("Enter 0 (hayang) or 1 (kulob): ")) # To input the user choices 0 or 1 to convert the input the user choices into integer 

c1, c2 = randint(0, 1), randint(0, 1)                       # generating the two variable random choices for C2 and c3 using the randint variable function

choices = ["hayang", "kulob"]                               # to list the corresponding choices to 0 and 1 in 
print(f"Me: {choices[user_choice]}")                        # To print the respond of the user choice 
print(f"C2: {choices[c1]}")                                 # To print the respond of the c2 choice
print(f"C3: {choices[c2]}")                                 # To print the respond of the c3 choice

if user_choice == c1 == c2:                                 # Checking the result of the choices if it is the same or draw the result
    print("It's a draw!")                                   # print the result of the choices 
elif user_choice == 0 and c1 == c2 == 1:                    # Checking the result of the user if not the same of the two player are same choices
    print("You win!")                                       # print you win mean the user are win                      
elif user_choice == 1 and c1 == c2 == 0:                    # Checking the result of the user if not the same of the two player are same choices
    print("You win!")                                       # print you win mean the user are win
elif user_choice == c1 and c2 != user_choice:               # Checking the user choice if they have the same result or draw
    print("C3 wins!")                                       # print the result of the choices
else:                                                      
    print("C2 wins!")                                       # print the result if the none of the above are met the condtion, authomatically C2 wins..
