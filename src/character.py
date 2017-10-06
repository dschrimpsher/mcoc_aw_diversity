class Character:
    def __init__(self, name, classType, pi, stars):
        self.name = name
        self.classType = classType
        self.pi = pi
        self.stars = stars

    def __str__(self):
        padding = 25 - len(self.name)

        temp = "\t" + self.name
        for j in range(padding):
            temp += " "
        temp += "(" + self.classType + "):"
        padding = 10 - len(self.classType)
        for j in range(padding):
            temp += " "
        temp +=  "%d " % self.pi
        for i in range(self.stars):
            temp += "*"
        temp += '\n'
        return temp
