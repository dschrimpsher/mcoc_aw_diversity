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
        self.players = sorted(self.players, key=lambda player: player.id, reverse=False)


    def __str__(self):
        temp = 'BG ' + self.id + '\n'
        # temp += pprint.pformat(self.chosen)
        # temp += '\n'
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

    def countDuplicates(self, printout=False):
        number = 0
        for i in self.chosen:
            exists = list(filter(lambda existingCharacter: existingCharacter["character"] == i["character"], self.chosen))
            if len(exists) > 1:
                if (printout == True):
                    print('Duplicate', i["character"], ' in ', self.id, ' by ', i['player'])
                number += 1/len(exists);
        return number


    def theoretical(self):
        while (len(self.chosen) < len(self.players) * 5):
            for p in self.players:
                    p.champs = sorted(p.champs, key=lambda champ:(-champ.pi))
                    for c in p.champs:
                        if (p.added < 5):
                            self.chosen.append({
                                "character": c.name,
                                "player": p.id,
                                "pi": c.pi,
                                "defender": c.defense
                            })
                            p.chosen.append({
                                "character": c.name,
                                "player": p.id,
                                "pi": c.pi
                            })
                            p.added += 1
        self.chosen = sorted(self.chosen, key=lambda chosen: chosen['player'], reverse=False)

    def optimize(self, duplicates=False):
        while (len(self.chosen) < len(self.players) * 5):
            for p in self.players:
                    for c in p.champs:
                        if (p.added < 5):
                            if (c.defense == True):
                                print(c.name + ' ' + 'Defender')
                            if (c.attack == True):
                                continue
                            else:
                                exists = list(filter(lambda existingCharacter: existingCharacter["character"] == c.name, self.chosen))
                                if len(exists) == 0:
                                    self.chosen.append({
                                        "character": c.name,
                                        "player": p.id,
                                        "pi": c.pi,
                                        "defender": c.defense
                                    })
                                    p.chosen.append({
                                        "character": c.name,
                                        "player": p.id,
                                        "pi": c.pi
                                    })
                                    p.added += 1
                                else:
                                    if (c.pi > exists[0]['pi'] or c.defense == True):

                                        otherPlayer = list(filter(lambda otherPlayer: otherPlayer.id == exists[0]['player'], self.players))
                                        otherCharacter = list(filter(lambda otherCharacter: otherCharacter.name == c.name, otherPlayer[0].champs))

                                        #make sure other player isn't a defender
                                        if ( (c.defense == True and otherCharacter[0].defense == True) or
                                             (duplicates == True)):
                                            #add both
                                            p.chosen.append({
                                                "character": c.name,
                                                "player": p.id,
                                                "pi": c.pi
                                            })
                                            self.chosen.append({
                                                "character": c.name,
                                                "player": p.id,
                                                "pi": c.pi,
                                                "defender": c.defense
                                            })
                                            p.added += 1
                                        elif (otherCharacter[0].defense == True):
                                            #don't add keep going
                                            continue
                                        else:
                                            #remove added from the player
                                            self.chosen[:] = [d for d in self.chosen if d.get('character') != c.name]
                                            otherPlayer[0].added -= 1
                                            otherPlayer[0].chosen[:] = [d for d in otherPlayer[0].chosen if d.get('character') != c.name]

                                            p.chosen.append({
                                                "character": c.name,
                                                "player": p.id,
                                                "pi": c.pi
                                            })
                                            self.chosen.append({
                                                "character": c.name,
                                                "player": p.id,
                                                "pi": c.pi,
                                                "defender": c.defense
                                            })
                                            p.added += 1
        self.chosen = sorted(self.chosen, key=lambda chosen: chosen['player'], reverse=False)
