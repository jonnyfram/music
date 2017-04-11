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
class Drummer(Musician):
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

    def hire(self, new_hire, instrument):
        #new_hire = input("What is the new hire called?")
        #instrument = input("What kind of musician are they?") #removed for faster testing
        
        if instrument == "Drummer":
            self.members[new_hire] = Drummer()
            
        elif instrument == "Guitarist":
            self.members[new_hire] = Guitarist()
            
        elif instrument == "Bassist":
            self.members[new_hire] = Bassist()
            
            #How to pass information to method within class?:
            #example : one_hit_wonder.hire("BongoBob", "Drummer") from outside class

        
    def fire(self):
        who_to_fire = input("Who do you want to fire?")
        del self.members[who_to_fire]
        print(who_to_fire+" was booted from the band!")
        
    def play(self, length):
        have_drummer = False

        #everyone play solo
        for all in self.members.values():
            # isinstance is a check that requires the 'object' and the class to check against?
            if isinstance(all,Drummer):
                all.count()
                #example of calling combustion
                #all.combust()
                have_drummer = True
            
        if have_drummer == True:
            for all in self.members.values():
                all.solo(length)

        else:
            print("we have no drummer...")
#What would be a better way to sort through the self.members and call specific methods based on their instrument type?
#I feel like I should be able to use a for loop to check each member



#fabricate the band:
one_hit_wonder = Band()

#hire a 3 piece
print("Hiring...")
one_hit_wonder.hire("bob", "Drummer")
one_hit_wonder.hire("jo", "Guitarist")
one_hit_wonder.hire("ju", "Bassist")

#check we have the 3 piece
print(one_hit_wonder.members.items())

#play
print("Playing")
one_hit_wonder.play(3)

#fire someone
print("The band isn't working out...")
one_hit_wonder.fire()



