# Team 1 BCE 4.2
# Quin Alexander, Annie Ho, Buki James, Joseph Santhosh, Jason Sun

# 1. Define four classes: Hammer, Pliers, Knife, Screwdriver. Each has only one method: used_for(). 
# The method must return ‘pounds things’ (for Hammer), ‘pulls things’ (for Pliers), ‘cuts things’ (for Knife), and ‘screws things’ (for Screwdriver).
class Hammer:

    def __init__(self):
        self.purpose = 'pounds things'

    def used_for(self):
        return(self.purpose)

class Pliers:

    def __init__(self):
        self.purpose = 'pulls things'

    def used_for(self):
        return(self.purpose)

class Knife:

    def __init__(self):
        self.purpose = 'cuts things'

    def used_for(self):
        return(self.purpose)

class Screwdriver:

    def __init__(self):
        self.purpose = 'screws things'

    def used_for(self):
        return(self.purpose)

# 2. Define the class Toolbelt that has one instance of each of these. 
# It also has a used_for() method, but his one returns what the Toolbelt’s component objects are used for. 
class Toolbelt:

    def __init__(self):
        self.hammer = Hammer()
        self.pliers = Pliers()
        self.knife = Knife()
        self.screwdriver = Screwdriver()

    def used_for(self):
        return(self.hammer.purpose + ', ' + self.pliers.purpose + ', ' + self.knife.purpose + ', ' + self.screwdriver.purpose)

# 3. Create enough code to create object instances to show how the classes can be used with different instantiations.
h = Hammer()
p = Pliers()
k = Knife()
s = Screwdriver()
t = Toolbelt()
print('hammer', h.used_for())
print('pliers', p.used_for())
print('knife' , k.used_for())
print('screwdriver', s.used_for())
print('toolbet', t.used_for())

