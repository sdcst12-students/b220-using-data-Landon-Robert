import random

x = random.randint(2,12)
if x <= 4:
    SP = "A"; NB = False; SB = False; GG = True
elif x <= 6:
    SP = "B"; NB = False; SB = False; GG = True
elif x == 7:
    SP = "C"; NB = False; SB = True; GG = True
elif x == 8:
    SP = "C"; NB = True; SB = True; GG = True
elif x == 9:
    SP = "D"; NB = True; SB = True; GG = True
elif x <= 11:
    SP = "E"; NB = True; SB = True; GG = False
else:
    SP = "X"; NB = True; SB = True; GG = False

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
name = random.choice(alphabet) + random.choice(alphabet) + str(random.randint(1,10000))
size = random.randint(2,12) - 2
atmosphere = 

stats = {"Star Port: ": SP, "Naval Base: ": NB, "Scout Base: ": SB, "Gas Giant: ": GG, "Name: ": name, "Size": size, }
print(stats)