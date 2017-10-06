class Character:
    def __init__(self, name, classType, pi):
        self.name = name
        self.classType = classType
        self.pi = pi

    def __str__(self):
        temp = "\t" + self.name + " (" + self.classType + "): %d\n" % self.pi
        return temp
