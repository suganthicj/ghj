
number = int(input("Please Enter any Number: "))

print("The List of Natural Numbers from 1 to {0} are".format(number)) 

for i in range(1, number + 1):
    print (i, end = '  ')
