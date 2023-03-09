for myNumber in range(1,32):

  if((myNumber % 3 == 0) and (myNumber % 15 != 0)):
    print("Fizz")

  if((myNumber % 5 == 0) and (myNumber % 15 !=0)):
    print("Buzz")

  if((myNumber % 15 == 0)):
    print("FizzBuzz")

  if((myNumber % 5 != 0) and (myNumber % 3 != 0)):
    print(myNumber)

