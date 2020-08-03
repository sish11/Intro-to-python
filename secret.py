secret_number = 42  #create  number in progam
guess = 0             #variable to store user`guess 

# as long as we have not found the secret number
while guess != secret_number :
    # get a new guess from user
    guess = eval(input("? "))
    # check if guess it too low
    if guess < secret_number:
      print ("please try again")
    # or too high
    elif guess > secret_number:
      print ("please try again")
print ("congratulations, you have guessed the secret number!")     #print message indicating success

