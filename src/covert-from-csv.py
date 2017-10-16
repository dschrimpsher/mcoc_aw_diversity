import csv
import sys
import os
import json

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

if len(sys.argv) < 2:
    print('Target directory to convert is required')
    exit(-1)
else:

    files = os.listdir(sys.argv[1])
    for nextfile in files:
        player = {
            "id": nextfile.split('.')[0],
            "champs": []
        }
        f = open(sys.argv[1] + '/' + nextfile, 'r')
        reader = csv.reader(f)
        header = True
        for row in reader:
            if header == False:
                temp =  {
                    "name": row[0],
                    "class": row[1],
                    "pi": row[2],
                    "stars": 4,
                    "attack": row[3].lower(),
                    "defense": row[4].lower()
                }
                player['champs'].append(temp)
            else:
                header = False
        print(player)

        f.close()
