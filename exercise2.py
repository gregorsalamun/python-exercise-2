print ("Odd, even number checker" + "\n")
number = int(input("Your number: "))
if number % 4 == 0:
	print ("Number is multiple of 4")
if number % 2 == 0:
	print ("Number is even")
elif number % 2 != 0:
	print ("Number is odd")

num = int(input("Enter number to check if it is divisible by next number: "))
check = int(input("Enter number to devide previouslyx enetered number: "))
if num % check == 0:
	print (str(num) + " is divisible by " + str(check))
else:
	print (str(num) + " is not divisible by " + str(check))