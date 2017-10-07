import character
import json
import pprint

class Player(object):
    def __init__(self):
        self.id = 0
        self.champs = []
        self.chosen = []
        self.added = 0

    def load(self, file):
        with open(file) as data_file:
            data = json.load(data_file)
            self.id = data['id']
            for datum in data['champs']:
                if 'attack' in datum:
                    self.champs.append(character.Character(datum['name'], datum['class'], datum['pi'], datum['stars'], datum['attack']))
                else:
                    self.champs.append(character.Character(datum['name'], datum['class'], datum['pi'], datum['stars']))

            self.champs = sorted(self.champs, key=lambda champ: champ.pi, reverse=True)


    def power(self):
        power = 0
        for i in self.chosen:
            power += i['pi']
        return power

    def __str__(self):
        temp = 'Player ' + self.id + '\n'
        temp += pprint.pformat(self.chosen, indent=5)
        temp += '\n\tPower: %d' % self.power()
        temp += '\n'
        # for champ in self.champs:
        #         temp += champ.__str__()
        return temp
