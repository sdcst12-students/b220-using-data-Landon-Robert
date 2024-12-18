import random
DMs = 0
SPr = random.randint(2,12)
if SPr <= 4:
    SP = "A"; DMs = DMs + 6
elif SPr <= 6:
    SP = "B"; DMs = DMs + 4
elif SPr <= 8:
    SP = "C"; DMs = DMs + 2
elif SPr == 9:
    SP = "D"
elif SPr <= 11:
    SP = "E"
else:
    SP = "X"; DMs = DMs - 4


if SP == "C" or SP == "D" or SP == "E" or SP == "X":
    NB = "N/A"
else:
    NB = random.randint(2,12)
    if NB >= 8:
        NB = "Yes"
    else:
        NB = "N/A"


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
    SB = "Yes"
else:
    SB = "No"

GGr = random.randint(2,12)
if GGr <= 9:
    GG = "Yes"
else:
    GG = "No"


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZΓΔΘΛΞΠΣΦΨΩϘБДЖИЛЦЧШЩЮЯ"
name = random.choice(alphabet) + random.choice(alphabet) + str(random.randint(1,10000))
size = random.randint(2,12) - 2

if size == 0:
    atmos = 0
else:
    atmos = random.randint(2,12) - 7 + size

if 4 >= size >= 2:
    DMs = DMs + 1
elif size < 2:
    DMs = DMs + 2
else:
    pass

if (0 <= atmos <= 3) or (10 <= atmos <= 14):
    DMs = DMs + 1
else:
    pass


HG = random.randint(2,12) - 7
pop = random.randint(2,12) - 2
gov = random.randint(2,12) - 7 + pop
LL = random.randint(2,12) - 7 + gov
TL = random.randint(1,6) + DMs
stats = {"Star Port: ": SP, "Naval Base: ": NB, "Scout Base: ": SB, "Gas Giant: ": GG, "Name: ": name, "Size": size, "Atmosphere": atmos}
print(stats)