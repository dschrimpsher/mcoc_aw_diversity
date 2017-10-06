import player
import json
import pprint

class BG(object):
    def __init__(self):
        self.id = 0
        self.players = []
        self.chosen = []

    def load(self, file):
        with open(file) as data_file:
            data = json.load(data_file)
            self.id = data['id']
            for datum in data['players']:
                newPlayer = player.Player()
                newPlayer.load(datum['filename'])
                self.players.append(newPlayer)

    def __str__(self):
        temp = 'BG ' + self.id + '\n'
        temp += pprint.pformat(self.chosen)
        temp += '\n'
        for p in self.players:
                temp += '  ' + p.__str__()
        temp += '\n'
        temp += 'Power Rating: %d' % self.power()
        return temp

    def power(self):
        power = 0
        for i in self.chosen:
            power += i['pi']
        return power

    def optimize(self):
        while (len(self.chosen) < len(self.players) * 5):
            for p in self.players:
                 if (p.added < 5):
                    for c in p.champs:
                        exists = list(filter(lambda existingCharacter: existingCharacter["character"] == c.name, self.chosen))
                        if len(exists) == 0:
                            self.chosen.append({
                                "character": c.name,
                                "player": p.id,
                                "pi": c.pi
                            })
                            p.added += 1
                            if p.added == 5:
                                break;
                        else:
                            if (c.pi > exists[0]['pi']):
                                self.chosen[:] = [d for d in self.chosen if d.get('character') != c.name]
                                #remove added from the player
                                otherPlayer = list(filter(lambda otherPlayer: otherPlayer.id == exists[0]['player'], self.players))
                                otherPlayer[0].added -= 1

                                self.chosen.append({
                                    "character": c.name,
                                    "player": p.id,
                                    "pi": c.pi
                                })
                                p.added += 1
                                if p.added == 5:
                                    break;
