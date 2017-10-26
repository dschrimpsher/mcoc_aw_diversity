class Character:
    def __init__(self, name, classType, pi, stars, attack=False, defense=False):
        self.name = name
        self.classType = classType
        self.pi = pi
        self.stars = stars
        self.attack = attack
        self.defense = defense

    def __str__(self):
        padding = 25 - len(self.name)

        temp = "\t" + self.name
        for j in range(padding):
            temp += " "
        temp += "(" + self.classType + "):"
        padding = 10 - len(self.classType)
        for j in range(padding):
            temp += " "
        temp += "%d " % self.pi
        for i in range(self.stars):
            temp += "*"
        if (self.attack == True):
            temp += ' \tAttacker\n'
        elif (self.defense == True):
            temp += ' \tDefender\n'
        else:
            temp += '\n'
        return temp

    def convertToCsv(self):
        temp = [self.name,   self.classType, self.pi, self.stars,  self.attack, self.defense]
        return temp
