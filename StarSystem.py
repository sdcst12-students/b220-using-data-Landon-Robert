import random

SPr = random.randint(2,12)
if SPr <= 4:
    SP = "A"
elif SPr <= 6:
    SP = "B"
elif SPr <= 8:
    SP = "C"
elif SPr == 9:
    SP = "D"
elif SPr <= 11:
    SP = "E"
else:
    SP = "X"


if SP == "C" or SP == "D" or SP == "E" or SP == "X"
    NB = "N/A"
else:
    NB = random.randint(2,12)
    if NB >= 8:
        NB = True
    else:
        NB = False


if SP == "D":
    SB = random.randint(2,12)
elif SP == "C":
    SB = random.randint(2,12) - 1
elif SP == "B":
    SB = random.randint(2,12) - 2
elif SP == "A":
    SB = random.randint(2,12) - 3
else:
    SB = "N/A"

if SB == "N/A":
    pass
elif SB >= 7:
    SB = True
else:
    SB = False

GGr = random.randint(2,12)
if GGr <= 9:
    GG = True
else:
    GG = False


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
name = random.choice(alphabet) + random.choice(alphabet) + str(random.randint(1,10000))
size = random.randint(2,12) - 2
if size == 0:
    atmos = 0
else:
    atmos = random.randint(2,12) - 7 + size

HG = random.randint(2,12) - 7
pop = random.randint(2,12) - 2
gov = random.randint(2,12) - 7 + pop
LL = random.randint(2,12) - 7 + gov

stats = {"Star Port: ": SP, "Naval Base: ": NB, "Scout Base: ": SB, "Gas Giant: ": GG, "Name: ": name, "Size": size, "Atmosphere": atmos}
print(stats)