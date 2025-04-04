import random
class starsystem:
    def spaceport(self):
        SPr = random.randint(1,6) + random.randint(1,6)
        if SPr <= 4:
            self.SP = "A"
        elif SPr <= 6:
            self.SP = "B"
        elif SPr <= 8:
            self.SP = "C"
        elif SPr == 9:
            self.SP = "D"
        elif SPr <= 11:
            self.SP = "E"
        else:
            self.SP = "X"

    def navalBase(self):
        if self.SP == "C" or self.SP == "D" or self.SP == "E" or self.SP == "X":
            NB = "N/A"
        else:
            NB = random.randint(1,6) + random.randint(1,6)
            if NB >= 8:
                NB = "Yes"
            else:
                NB = "N/A"  

    def scoutBase(self):
        if self.SP == "D":
            SB = random.randint(1,6) + random.randint(1,6)
        elif self.SP == "C":
            SB = random.randint(1,6) + random.randint(1,6) - 1
        elif self.SP == "B":
            SB = random.randint(1,6) + random.randint(1,6) - 2
        elif self.SP == "A":
            SB = random.randint(1,6) + random.randint(1,6) - 3
        else:
            SB = "N/A"
        if SB == "N/A":
            pass
        elif SB >= 7:
            SB = "Yes"
        else:
            SB = "No"
        return SB
    
    def gasGiant(self):
        GGr = random.randint(1,6) + random.randint(1,6)
        if GGr <= 9:
            GG = "Yes"
        else:
            GG = "No"
        return GG
    
    def name(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZΓΔΘΛΞΠΣΦΨΩϘБДЖИЛЦЧШЩЮЯ"
        name = random.choice(alphabet) + random.choice(alphabet) + str(random.randint(1,10000))
        return name
    
    def size(self):
        size = random.randint(1,6) + random.randint(1,6) - 2
        return size
    
    def atmos(self):
        if self.size() == 0:
            atmos = 0
        else:
            atmos = random.randint(1,6) + random.randint(1,6) - 7 + self.size()
        return atmos
    
    def DM(self):
        DMs = 0
        if self.SP == "A":
            DMs = DMs + 6
        elif self.SP == "B":
            DMs = DMs + 4
        elif self.SP == "C":
            DMs = DMs + 2
        else:
            DMs = DMs - 4
            
        if 4 >= self.size() >= 2:
            DMs = DMs + 1
        elif self.size() < 2:
            DMs = DMs + 2
        else:
            pass

        if 0 <= self.atmos() <= 3 or 10 <= self.atmos() <= 14:
            DMs = DMs + 1
        else:
            pass
        
        return DMs
    
    def hydrographics(self):
        return random.randint(1,6) + random.randint(1,6) - 7
    
    def population(self):
        return random.randint(1,6) + random.randint(1,6) - 2
    
    def govLevel(self):
        return random.randint(1,6) + random.randint(1,6) - 7 + self.population()

    def lawLevel(self):
        return random.randint(1,6) + random.randint(1,6) - 7 + self.govLevel()

    def techLevel(self):
        return random.randint(1,6) + self.DM()

SS = starsystem()
stats = {"Star Port": SS.spaceport(), "Naval Base": SS.navalBase(), "Scout Base": SS.scoutBase(), "Gas Giant": SS.gasGiant(), "Name": SS.name(), "Size": SS.size(), "Atmosphere": SS.atmos(), "Hydrographics": SS.hydrographics(), "Population": SS.population(), "Government Level": SS.govLevel(), "Law Level": SS.lawLevel(), "Tech Level": SS.techLevel()}
print(stats)

