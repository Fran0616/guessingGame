# guessingGame

**Objective**

This games the user has to pick a secret number set by a magician. The user has to guess the correct number or he/she will be stuck in a forever loop.

**Software Overview**

1. The code will prompt the magiaciant to enter the secret number. 
2. The muggle will attempt to guess the secret number.
3. The muggle will be promted to try again if he/she guess the secret number wrong
   - The game will end when the muggle guess the secret number correctly
 

**Test Data**

```
Magician Enter a number: 2

+=========================================+

| Welcome to my guessing game, muggle!    |

| Enter an integer number                 |

| and guess what number I've              |

| picked for you.                         |

| So, what is the secret number?          |

+=========================================+


Muggle guess the number? moowaahhhhaaahhh 4

Ha ha! You're stuck in my loop!

Try again: 3

Ha ha! You're stuck in my loop!

Try again: 4

Ha ha! You're stuck in my loop!

Try again: 2

Well done, muggle! You are free now. Thanks for playing!
```

Source Code

Click [here]() to view the code
```
#this games the user has to pick a secret number set by a magician. The user has to guess the correct number or he/she will be stuck in a forever loop.
#good luck and have fun. 
secret_number = int(input("Magician Enter a number: "))
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


```
