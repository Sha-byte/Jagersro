import collections
from random import shuffle
import pickle as pkl
import copy
import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("bet.txt", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass

sys.stdout = Logger()
win_percentage = []

horses = {}
horses["Rigoletto"]=(2, "gul", [3,2,3,4,4,2,3,1,1,3,2,4,3,2,3,4,4,2,3,1,1,3,2,4])
horses["Tristan"]=(2, "svart", [4,3,2,2,2,3,2,4,2,3,1,4,4,3,2,2,2,3,2,4,2,3,1,4])
horses["Figaro"]=(2, "vit", [4,3,2,3,2,3,4,1,4,3,2,1,4,3,2,3,2,3,4,1,4,3,2,1])
horses["Isolde"]=(2, "röd", [4,1,2,3,3,4,2,3,1,4,2,3,4,1,2,3,3,4,2,3,1,4,2,3])
horses["Caruso"]=(2, "blå", [1,2,3,3,4,2,4,3,1,3,2,4,1,2,3,3,4,2,4,3,1,3,2,4])
horses["Rusch"]=(3, "röd", [4,5,1,2,3,4,4,5,3,2,1,2,4,5,1,2,3,4,4,5,3,2,1,2])
horses["Comet"]=(3, "gul", [5,3,4,2,1,5,1,3,2,4,5,1,5,3,4,2,1,5,1,3,2,4,5,1])
horses["Rapid"]=(3, "svart", [5,2,1,3,4,1,5,2,4,3,5,1,5,2,1,3,4,1,5,2,4,3,5,1])
horses["Vitesse"]=(3, "vit", [3,4,5,2,1,3,2,4,5,1,2,4,3,4,5,2,1,3,2,4,5,1,2,4])
horses["Orkan"]=(3, "blå", [2,3,5,4,1,3,2,4,5,1,2,4,2,3,5,4,1,3,2,4,5,1,2,4])
horses["RoseRoom"]=(4, "röd", [3,3,3,3,3,3,6,6,3,3,6,1,3,3,3,3,3,3,6,6,3,3,6,1])
horses["Avalon"]=(4, "blå", [1,3,5,2,4,6,4,3,6,2,1,6,1,3,5,2,4,6,4,3,6,2,1,6])
horses["Whispering"]=(4, "svart", [2,3,4,5,6,1,1,2,3,4,5,6,2,3,4,5,6,1,1,2,3,4,5,6])
horses["SweetSue"]=(4, "gul", [6,6,5,5,3,3,2,1,1,2,4,4,6,6,5,5,3,3,2,1,1,2,4,4])
horses["Solitude"]=(4, "vit", [6,1,3,3,5,5,2,2,4,4,6,1,6,1,3,3,5,5,2,2,4,4,6,1])
horses["Rigel"]=(5, "gul", [6,6,6,1,3,6,4,5,6,2,3,4,6,6,6,1,3,6,4,5,6,2,3,4])
horses["Aldebaran"]=(5, "vit", [6,2,3,3,4,4,5,5,6,6,6,2,6,2,3,3,4,4,5,5,6,6,6,2])
horses["Castor"]=(5, "svart", [1,1,4,6,5,5,5,5,3,5,5,3,1,1,4,6,5,5,5,5,3,5,5,3])
horses["Pollux"]=(5, "röd", [1,1,4,6,5,5,5,5,5,5,5,1,1,1,4,6,5,5,5,5,5,5,5,1])
horses["Cassiopeja"]=(5, "blå", [3,4,5,6,3,3,4,5,6,3,3,3,3,4,5,6,3,3,4,5,6,3,3,3])

# chansk = []
# Bolag
# chans.append("(Gäller alla)\nBetala 3,000 per häst till\ninnehavaren av AB Tränartjänst.\n Ta lån om du inte har kontanter\n. Om ingen äger bolaget betalar du till banken")
# chans.append("(Gäller alla)\nBetala 2,000 per häst till\ninnehavaren av AB Galoppstall.\n Ta lån om du inte har kontanter\n. Om ingen äger bolaget betalar du till banken")
# chans.append("(Gäller alla)\nBetala 2,000 per häst till\ninnehavaren av AB Galoppförsäkring.\n Ta lån om du inte har kontanter\n. Om ingen äger bolaget betalar du till banken")
# chans.append("(Gäller ej övriga spelare)\nBetala 10,000 per bolag till banken")
# chans.append("(Gäller ej övriga spelare)\nDina bolag lämnar\nvardera 10,000 i vinst genom banken")
# chans.append("Gäller endast lopp 9 & 10 och inte övriga spelare\nBetala 20,000 till banken")
#-----------------------------
# chansk.append("Vill du köpa en häst?")
# chansk.append("Din dyraste häst som inte är med i loppet blir köpt för 10,000")
# chansk.append("Din dyraste häst som inte är med i loppet blir köpt för 10,000")
# chansk.append("Banan måste repareras\nUnder lopp 1-6 alla betalar 2,000.\nUnder lopp 7-10 alla betalar 10,000")
# chansk.append("Banken köper en av dina hästar\nsom inte är med i loppet och som inte\nhar startförbud, till fulla värdet")
# chansk.append("Kvittera ut 5,000 i banken")
# chansk.append("Du har vunnit en 3-åring\neller om alla är sålda 3,000")
# chansk.append("Vill du göra en försäljning?\nVad som helst får säljas utom\nhäst på bana.")
# chansk.append("Köp en häst!\nGäller endast om du har kontanter")
# chansk.append("Gör en affär!\nGör en valfri\naffärstransaktion enligt\nreglerna.")
# chansk.append("Spela 1,000 på en blå\nhäst, om den är med i\nloppet och du har\nkontanter. Spara kortet\ntills loppet är slut!")
# chansk.append("Spela 1,000 på en vit\nhäst, om den är med i\nloppet och du har\nkontanter. Spara kortet\ntills loppet är slut!")
# chansk.append("Spela 1,000 på en svart\nhäst, om den är med i\nloppet och du har\nkontanter. Spara kortet\ntills loppet är slut!")
# chansk.append("Spela 1,000 på en röd\nhäst, om den är med i\nloppet och du har\nkontanter. Spara kortet\ntills loppet är slut!")
# chansk.append("Spela 1,000 på en gul\nhäst, om den är med i\nloppet och du har\nkontanter. Spara kortet\ntills loppet är slut!")
# chansk.append("(Gäller alla)\nUnder lopp 1-5: Betala 1,000 per 3-åring.\nUnder lopp 6-7: Betala 2,000 per 4-åring")
# chansk.append("(Gäller alla)\nFördubbla dina kontanter genom\nuttag från banken, dock högst 25,000")
# chansk.append("Ta ett lån!\nGäller inte om du har 80,000\neller mer i skuld.")
# chansk.append("Alla dina hästar, som inte\när på banan, är förkylda\noch kan inte starta nästa lopp.\nDe får inte säljas förän nästa lopp\nhar börjat. Spara kortet till dess.\nOm du har betalt försäkringen\nfår du 2,000 av banken för varje\nsjuk häst.")
# chansk.append("Du får köpa en häst för\nhalva priset, om du har kontanter.")
# shuffle(chansk)

galoppk = []




placering = ["","",[0,0,0,0,0,0,0,1,2,3,4,5,6,36,66,67,97,127,128,129,130,131,132,133,134,135,165,195,196,226,256,257,258,259,260,261,262,263], [0,0,0,0,0,0,0,1,2,3,4,5,6,26,46,66,67,87,107,127,128,129,130,131,132,133,134,135,155,175,195,196,216,236,256,257,258, 259, 260, 261, 262, 263], [0,0,0,0,0,0,0,1,2,3,4,5,6,21,36,51,66,67,82,97,112,127,128,129,130,131,132,133,134,135,150,165,180,195,196,211,226,241,256,257,258, 259, 260, 261, 262, 263],[0,0,0,0,0,0,0,1,2,3,4,5,6,18,30,42,54,66,67,79,91,103,115,127,128,129,130,131,132,133,134,135,147,159,171,183,195,196,208,220,232,244,256,257,258, 259, 260, 261, 262, 263]]

turn = 0





def main(start):
    global turn
    global galoppk
    global money
    global bet
    global win_percentage
    global galopp_counter
    global galopp_shuffle

    galoppk = []
    galoppk.append("Dålig galopp!")
    galoppk.append("Protest!")
    galoppk.append("Hästen går utmärkt!")
    galoppk.append("Manar på!")
    galoppk.append("Snabb galopp!")
    galoppk.append("Skräp i ögat!")
    galoppk.append("Hästen snavar!")
    galoppk.append("Fin drivning!")
    galoppk.append("Jämn fart!")
    galoppk.append("Stark framryckning!")
    galoppk.append("Driv inte hästen för hårt!")
    galoppk.append("Snabb galopp!")
    galoppk.append("Fin inhämtning!")
    galoppk.append("Hästen halt!")
    galoppk.append("Svag finish!")
    galoppk.append("Snabb galopp!")
    galoppk.append("Snabb galopp!")
    galoppk.append("Snabb galopp!")
    galoppk.append("Hästen tröttnar!")
    galoppk.append("Hästen tröttnar!")

    galopp_shuffle = len(galoppk)

    galopp_counter = 0
    shuffle(galoppk)

    turn=0
    plhor = []
    pl=[[],[],[],[],[]]
    for hast in start:
        if hast.owner==1:
            pl[0].append(hast)
        elif hast.owner==2:
            pl[1].append(hast)
        elif hast.owner==3:
            pl[2].append(hast)
        elif hast.owner==4:
            pl[3].append(hast)
        elif hast.owner==5:
            pl[4].append(hast)
    lenpl = len(pl)
    for ind in range(lenpl):
        if pl[ind]:
            pass
        else:
            del pl[ind:]
            break

    while True:

        for player in pl:

            for hast in player:
                print("\n" + hast.name)
                if hast.skip:
                    hast.skip = False
                    hast.turn += 1
                    if hast.trottnar:
                        galoppk.append("Hästen tröttnar!")
                        hast.trottnar = False
                    continue

                if hast.bakomvarande:
                    if hast.bakomvarande == ["skip"]:
                        hast.turn += 1
                        print("Hästen är fast! p.g.a \"Dålig galopp\"")
                        continue
                    else:
                        try:
                            while True:
                                hast.bakomvarande.remove(None)
                        except ValueError:
                            pass
                        if hast.bakomvarande == []:
                            hast.bakomvarande = ["skip"]
                            print("Hästen är fast! p.g.a \"Dålig galopp\"")
                            hast.turn += 1
                            continue
                        check = True
                        for hor in hast.bakomvarande:
                            if hast.placering <= hor.placering:
                                check = False
                                break
                        if check:
                            hast.turn += 1
                            print("Hästen är fast! p.g.a \"Dålig galopp\"")
                            continue
                        else:
                            galoppk.append("Dålig galopp!")
                            hast.bakomvarande = []

                if 0 <= hast.steg[turn]+hast.left and not hast.jamnfart:
                    temp = hast.left
                    out = galopp(hast, player, pl)
                    if not out:
                        continue
                    if hast.bakomvarande != []:
                        hast.turn += 1
                        continue
                    if temp != hast.left:
                        store = -1
                        while store  != hast.placering:
                            store = hast.placering
                            out = True
                            if hast.placering == 259:
                                out = galopp(hast, player, pl)
                                if not out:
                                    break
                        if not out:
                            continue
                        if hast.bakomvarande != []:
                            hast.turn += 1
                            continue
                aft_mov = move(hast, player, pl)
                if not aft_mov:
                    continue

                if 0 <= hast.left:
                    check = []
                    for _player in pl:
                        for _hast in _player:
                            if _hast:
                                check.append(_hast.placering)
                                print(_hast.name + " av spelare "+ str(_hast.owner) +" har " + str(_hast.left) + " steg kvar")
                    print(hast.name + " av spelare "+ str(hast.owner) +" vinner!")
                    check.sort(reverse=True)
                    n = len(bet)
                    if 1 < len(check):
                        if check[1] == 263:
                            for ind in range(n):
                                money[ind] += bet[ind][hast.farg]*20
                        if check[1] == 262:
                            for ind in range(n):
                                money[ind] += bet[ind][hast.farg]*10
                        if check[1] == 261:
                            for ind in range(n):
                                money[ind] += bet[ind][hast.farg]*5
                        if check[1] == 260:
                            for ind in range(n):
                                money[ind] += bet[ind][hast.farg]*4
                        if check[1] == 259:
                            for ind in range(n):
                                money[ind] += bet[ind][hast.farg]*3
                        if check[1] <= 258:
                            for ind in range(n):
                                money[ind] += bet[ind][hast.farg]*2
                    else:
                        for ind in range(n):
                            money[ind] += bet[ind][hast.farg]*2

                    win_percentage.append(hast.name)
                    return


            try:
                while True:
                    player.remove(None)
            except ValueError:
                pass
            for ind in player:
                if ind.bakomvarande:
                    player.append(ind)
                    player.remove(ind)


        if turn == 23:
            win_percentage.append("")
            return
        turn += 1



def move(hast, player, pl):
    global galoppk
    if hast.jamnfart:
        hast.left = 4 + hast.left
        hast.turn += 1
        hast.placering = placering[hast.age][hast.left]
    elif hast.skip:
        hast.skip = False
        hast.turn += 1
        if hast.trottnar:
            galoppk.append("Hästen tröttnar!")
            hast.trottnar = False
        print("Omgång " + str(hast.turn + 1) + ", det är " + str(hast.left) + " steg kvar.")
        return True
    else:
        hast.left = hast.steg[turn] + hast.left
        hast.turn += 1
        hast.placering = placering[hast.age][hast.left]
        store = -1
        while store  != hast.placering:
            store = hast.placering
            out = True
            if hast.placering == 2:
                out = galopp(hast, player, pl)
            elif hast.placering == 6:
                out = galopp(hast, player, pl)
            elif hast.placering == 128:
                out = galopp(hast, player, pl)
            elif hast.placering == 133:
                out = galopp(hast, player, pl)
            elif hast.placering == 196:
                out = galopp(hast, player, pl)
            elif hast.placering == 259:
                out = galopp(hast, player, pl)
            if not out:
                return False

    assert hast.turn == turn
    if hast.jamnfart:
        print("P.g.a jämn fart:")
    print(str(hast.steg[hast.turn])+ " steg omgång " + str(hast.turn + 1) + ", det är " + str(hast.left) + " steg kvar.")
    return True



galopp_counter = 0

def galopp(hast, player, pl):
    global galoppk
    global galopp_counter

    if galoppk[0] == "Fin inhämtning!":
        print("Galoppkort \"Fin inhämtning!\"")
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        if turn != hast.turn:
            pass
        else:
            if leder(hast, pl):
                pass
            else:
                hast.left = hast.left + hast.steg[turn]
                hast.placering = placering[hast.age][hast.left]
    elif galoppk[0]=="Skräp i ögat!":
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        print("Galoppkort \"Skräp i ögat!\"")
        hast.left = hast.left-1
        hast.placering = placering[hast.age][hast.left]

    elif galoppk[0]=="Driv inte hästen för hårt!":
        print("Galoppkort \"Driv inte hästen för hårt!\"")
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        if turn != hast.turn and not hast.stjk:
            hast.skip = True
        else:
            pass

    elif galoppk[0]=="Hästen halt!":
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        print("Galoppkort \"Hästen halt!\"")
        if hast.forsakring == True:
            print("Ta 10,000 från banken p.g.a försäkring")
        else:
            print("Hästen är ej försäkrad du får inget")
        index = player.index(hast)
        player[index] = None
        return False

    elif galoppk[0]=="Svag finish!":
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        print("Galoppkort \"Svag finish!\"")
        if turn != hast.turn:
            hast.steg[turn] = min(2, hast.steg[turn])

    elif galoppk[0] == "Hästen går utmärkt!":
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        print("Galoppkort \"Hästen går utmärkt!\"")
        hast.left = hast.left + 5
        hast.placering = placering[hast.age][hast.left]

    elif galoppk[0]=="Snabb galopp!":
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        print("Galoppkort \"Snabb galopp!\"")
        hast.left = hast.left + 2
        hast.placering = placering[hast.age][hast.left]

    elif galoppk[0]=="Fin drivning!":
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        print("Galoppkort \"Fin drivning!\"")
        hast.left = hast.left + 4
        hast.placering = placering[hast.age][hast.left]

    elif galoppk[0]=="Hästen snavar!":
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        print("Galoppkort \"Hästen snavar!\"")
        if hast.age == 2:
            hast.left = max(hast.left - 3, -32)
        elif hast.age == 3:
            hast.left = max(hast.left - 3, -36)
        elif hast.age == 4:
            hast.left = max(hast.left - 3, -40)
        elif hast.age == 5:
            hast.left = max(hast.left - 3, -44)
        hast.placering = placering[hast.age][hast.left]

    elif galoppk[0] == "Jämn fart!":
        galoppk.pop(0)
        galopp_cntr()
        hast.steg[turn+1:] = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
        print("Galoppkort \"Jämn fart!\"")
        hast.jamnfart = True

    elif galoppk[0] == "Manar på!":
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        print("Galoppkort \"Manar på!\"")
        hast.left = hast.left + 1
        hast.placering = placering[hast.age][hast.left]

    elif galoppk[0] == "Dålig galopp!":
        print("Galoppkort \"Dålig galopp!\"")
        if not hast.stjk:
            if turn != hast.turn and not leder(hast, pl):
                pass
            else:
                narmast_bakomvarande(hast, pl)
                galoppk.pop(0)
        else:
            galoppk.append(galoppk[0])
            galoppk.pop(0)
        galopp_cntr()


    elif galoppk[0] == "Stark framryckning!":
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        print("Galoppkort \"Stark framryckning!\"")
        if turn != hast.turn:
            pass
        else:
            efter_ledaren(hast, pl)

    elif galoppk[0] == "Hästen tröttnar!":
        galoppk.pop(0)
        galopp_cntr()
        hast.trottnar = True
        print("Galoppkort \"Hästen tröttnar!\"")
        hast.skip = True

    elif galoppk[0] == "Protest!":
        galoppk.append(galoppk[0])
        galoppk.pop(0)
        galopp_cntr()
        print("Galoppkort \"Protest!\"")
        if hast.stjk:
            pass
        else:
            index = player.index(hast)
            player[index] = None
            return False
    return True

galopp_shuffle = 20
def galopp_cntr():
    global galoppk
    global galopp_counter
    global galopp_shuffle
    galopp_counter += 1

    if galopp_counter % galopp_shuffle == 0:
        shuffle(galoppk)
        galopp_shuffle = len(galoppk)

def efter_ledaren(hast, pl):
    first = 0
    for player in pl:
        for _hast in player:
            if _hast == None:
                continue
            if first < _hast.placering:
                first = _hast.placering
    ind0 = -1
    while first <= placering[hast.age][ind0]:
        ind0 -= 1
    if first != hast.placering:
        hast.left = ind0
        hast.placering = placering[hast.age][hast.left]


def narmast_bakomvarande(hast, pl):
    for player in pl:
        for _hast in player:
            if _hast == None:
                continue
            if _hast.placering < hast.placering:
                hast.bakomvarande.append(_hast)

    if hast.bakomvarande == []:
        hast.bakomvarande = ["skip"]




def leder(hast, pl):
    for player in pl:
        for _hast in player:
            if _hast == None:
                continue
            if hast.placering < _hast.placering:
                return False
    return True


class Horse:
    def __init__(self, name, owner, age, farg, steg, stjk = False, forsakring = False):
        self.name = name
        self.owner = owner
        self.age = age
        self.farg = farg
        self.steg = steg
        self.skip = False
        self.stjk = stjk
        self.forsakring = forsakring
        self.jamnfart = False
        if self.age == 2:
            self.left = -32
        elif self.age == 3:
            self.left = -36
        elif self.age == 4:
            self.left = -40
        elif self.age == 5:
            self.left = -44
        self.turn = -1
        self.placering = 0
        self.bakomvarande = []
        self.trottnar = False

def inlist(inp, ref):
    while True:
        count = 0
        if inp != []:
            for el in inp:
                if not el in ref:
                    count += 1
                    print("Du skrev fel")
                    inp = input().split()
                    break
            if 0 == count:
                break
        else:
            return []
    return inp

def user(iterationer):
    inn = []
    for i in range(1,6):
        inp_data(i, inn)
        if i == 1 and inn == []:
            return
    names = []
    for hor in inn:
        names.append(hor.name)
    print("Vilka hästar ska starta före de andra?")
    hasthcp = input().split()
    hasthcp = inlist(hasthcp, names)
    if hasthcp:
        print("Hur många steg?")
        steg = input().split()
        steg = inlist(steg, ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
        if steg == []:
            steg = 0
        else:
            steg = int(steg[0])
        for hor in inn:
            if hor.name in hasthcp:
                hor.left = hor.left + steg
                hor.placering = placering[hor.age][hor.left]

    inn2 = copy.deepcopy(inn)
    for i in range(iterationer):
        main(inn)
        inn = copy.deepcopy(inn2)
    hearner = max(money)
    index = money.index(hearner)
    out = bet[index]
    n = len(money)
    for i in range(n):
        temp = ""
        for key in bet[i]:
            temp += str(bet[i][key]) + " på " + key + " häst, "
        print(temp[:-2])
        print("ger " + str(money[i]) + " efter " + str(iterationer) + " spelade spel\n")
    print("\n")
    namnare = len(win_percentage)
    for s in inn2:
        print(s.name + " vann " + str(win_percentage.count(s.name)/namnare*100) + "% av loppen")
    print(str(win_percentage.count("")*100/namnare) + "% av loppen blev det oavgjort, dvs ingen vann")
    print("Bästa betet:")
    for k in out:
        print(str(out[k]) + " på " + k + " häst")
    print("det ger " + str(hearner) + " efter " + str(iterationer) + " spelade spel\n")

def inp_data(spelare, inn):
    print("Spelare " + str(spelare) + ", skriv namnen på dina hästar (ett ord)")
    hast1 = input().split()
    hast1 = inlist(hast1, horses.keys())
    if hast1 == []:
        return
    print("Vilka har stjärnjockey?")
    stjk1 = input().split()
    stjk1 = inlist(stjk1, hast1)
    print("Vilka har försäkring?")
    forsk = input().split()
    forsk = inlist(forsk, hast1)
    for hor in hast1:
        stj = False
        fors = False
        if hor in stjk1:
            stj = True
        if hor in forsk:
            fors = True
        inn.append(Horse(hor, spelare, horses[hor][0], horses[hor][1], horses[hor][2], stj, fors))


money = []
bet = pkl.load( open ("bet.p", "rb") )
for i in bet:
    money.append(0)


user(1000)
