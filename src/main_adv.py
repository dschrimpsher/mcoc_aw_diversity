import player
import bg_adv


bg1 = bg_adv.BG()
bg1.load('data/bg1.json')
bg1.optimize()
print(bg1)

bg2 = bg_adv.BG()
bg2.load('data/bg2.json')
bg2.optimize()
print(bg2)

bg3 = bg_adv.BG()
bg3.load('data/bg3.json')
bg3.optimize()
print(bg3)



print("BG1: ", bg1.power(), bg1.power()/10.0, " per player");
print("BG2: ", bg2.power(), bg2.power()/10.0, " per player");
print("BG3: ", bg3.power(), bg3.power()/10.0, " per player");

