#this games the user has to pick a secret number set by a magician. The user has to guess the correct number or he/she will be stuck in a forever loop.
#good luck and have fun. 
secret_number = int(input("Magecian Enter a number: "))
print(
"""
+=========================================+
| Welcome to my guessing game, muggle!    |
| Enter an integer number                 |
| and guess what number I've              |
| picked for you.                         |
| So, what is the secret number?          |
+=========================================+
""")
num = int(input("Muggle guess the number? moowaahhhhaaahhh "))
while num != secret_number:
    print ("Ha ha! You're stuck in my loop!")
    num = int(input("Try again: "))

print ("Well done, muggle! You are free now. Thanks for playing!")
