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



b1max = bg.BG()
b1max.load('data/bg1.json')
b1max.theoretical()
print(b1max)

b2max = bg.BG()
b2max.load('data/bg2.json')
b2max.theoretical()
print(b2max)

b3max = bg.BG()
b3max.load('data/bg3.json')
b3max.theoretical()
print(b3max)
print(b1max.power() + b2max.power() + b3max.power())
print(round(b1max.countDuplicates()) + round(b2max.countDuplicates()) + round(b3max.countDuplicates()) )


print(bg1.power() + bg2.power() + bg3.power())
print(round(bg1.countDuplicates(True)) + round(bg2.countDuplicates(True)) + round(bg3.countDuplicates(True)) )

print("BG1: ", bg1.power(), bg1.power()/10.0, " per player");
print("BG2: ", bg2.power(), bg2.power()/10.0, " per player");
print("BG3: ", bg3.power(), bg3.power()/10.0, " per player");

print("BG1: ", b1max.power(), b1max.power()/10.0, " per player");
print("BG2: ", b2max.power(), b2max.power()/10.0, " per player");
print("BG3: ", b3max.power(), b3max.power()/10.0, " per player");


# test = player.Player()
# test.load('data/drdew.json')
# print(test)
