print("Welcome to uhm 8ball thing")
x = input("Ask a question.")
Answer = ("x")
A1 = ("Probably")
A2 = ("Yeppadoodle")
A3 = ("NO!!!!!!!!!!!!!")
A4 = ("Ask again")
A5 = ("Idk go ask ur mom")
A6 = ("Definaly not! (✿◡‿◡)")
A7 = ("Yes!")
A8 = ("ㄟ( ▔, ▔ )ㄏ")
import random
Answer = random.randint(1,8)
print("Your Quseton was", x)
print(  )
if Answer == 1:
    print("The answer is", A1)
elif Answer == 2:
    print("The answer is", A2)
elif Answer == 3:
    print("The answer is", A3)
elif Answer == 4:
    print("The answer is", A4)
elif Answer == 5:
    print("The answer is", A5)
elif Answer == 6:
    print("The answer is", A6)
elif Answer == 7:
    print("The answer is", A7)
elif Answer == 8:
    print("The answer is", A8)
else:
    print("Guess who's the reason for the devorce?? You are!!! Yes you are!!!")