import csv
import bg

import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

if len(sys.argv) < 3:
    print('File and target directory to convert is required');
    exit(-1)
else:
    myBg = bg.BG()
    myBg.load(sys.argv[1])

    for otherPlayer in myBg.players:
        f = open(sys.argv[2] + '/' + otherPlayer.id + '.csv', 'w', newline='')
        writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Champ', 'Class', 'PI', 'Stars', 'Attack', 'Defense'])
        for c in otherPlayer.champs:
            writer.writerow(c.convertToCsv())
        f.close()
