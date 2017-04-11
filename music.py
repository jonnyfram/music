class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()

class Bassist(Musician):
    def __init__(self):
        #call the init method of the parent class
        super().__init__(["thrummerwummer", "thwommmm", "dwong"])

class Guitarist(Musician):
    def __init__(self):
    #call the init method of the parent class
        super().__init__(["zing", "tring","paching"])
        
    def tune(self):
        print("Be with you in a moment")
        print("Twoing, sproing, splang")
        
#Extended to add Drummer class
def Drummer(Musician):
    def __init__(self):
        super().__init__(["duff", "daff", "te", "fwaaaaaa"])
    
    def count(self):
        print("One...Two...Three..Four")
        
    def combust(self):
        print("Drummer spontaeneously combusts. Crowd goes wild.")

#Bands should be able to hire and fire musicians, and have the musicians play 
#their solos after the drummer has counted time.   

class Band(object):
    def __init__(self):
        self.members = {}
    
    def hire(self, name, instrument):
        new_hire = name
        
        if instrument == "Drummer":
            self.members[new_hire] = Drummer()
            print(self.members)
        elif instrument == "Guitarist":
            self.members[new_hire] = Guitarist()
            
        elif instrument == "Bassist":
            self.members[new_hire] = Bassist()
        
    def fire(self):
        
        who_to_fire = raw_input("Who do you want to fire?")
        
        self.members.pop(who_to_fire)
        
        print(who_to_fire+" was booted from the band!")
        
    def play(self):
        self.members[Drummer].count()
        pass
    
one_hit_wonder = Band()

#hire a 3 piece
print("Hiring...")
one_hit_wonder.hire("BongoBob", "Drummer")
#one_hit_wonder.hire("TwangyJoe", "Guitarist")
#one_hit_wonder.hire("ThrummyJum", "Bassist")

#fire someone
print("The band isn't working out, who do we need to fire?")
one_hit_wonder.fire()



