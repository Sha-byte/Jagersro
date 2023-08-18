import pickle as pkl
import random

outdic = []
markers = [1000, 500, 200, 100]

for i in range(1000000):
    tempdic = {"röd": 0, "svart": 0, "gul": 0, "vit": 0, "blå": 0}
    for mark in markers:
        check = random.uniform(0,1)
        if check < 0.2:
            tempdic["röd"] += mark
        elif 0.2 < check and check < 0.4:
            tempdic["svart"] += mark
        elif 0.4 < check and check < 0.6:
            tempdic["gul"] += mark
        elif 0.6 < check and check < 0.8:
            tempdic["vit"] += mark
        else:
            tempdic["blå"] += mark
    if not tempdic in outdic:
        outdic.append(tempdic)



pkl.dump(outdic, open( "bet.p", "wb" ) )
