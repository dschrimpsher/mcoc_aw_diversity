import player
import bg

bg1 = bg.BG()
bg1.load('data/bg1.json')
bg1.optimize()
print(bg1)

bg2 = bg.BG()
bg2.load('data/bg2.json')
bg2.optimize()
print(bg2)

bg3 = bg.BG()
bg3.load('data/bg3.json')
bg3.optimize()
print(bg3)

# test = player.Player()
# test.load('data/drdew.json')
# print(test)
