import random

counter = 0
first_dice = 12
domino_num = 1
dict_dominos = {}

def arrange_dominos_doubles_first(counter, first_dice):
    global domino_num
    for i in range(first_dice, -1, -1):
        second_dice = first_dice - counter
        for j in range(counter + 1):
            dict_dominos[domino_num] = (str(second_dice) + '|' + str(i))
            second_dice += 1
            domino_num += 1
        counter += 1


arrange_dominos_doubles_first(counter, first_dice)


def visited(a, b, DICTIONARY_DOMINOS):
    for key in DICTIONARY_DOMINOS:
        if DICTIONARY_DOMINOS[key] == f'{a}|{b}' or DICTIONARY_DOMINOS[
                key] == f'{b}|{a}':
            DICTIONARY_DOMINOS.pop(key)
            return f'{a}|{b}'


class dominos:
    def __init__(self):
        self.player = []

    def pick_domino(self):
        while True:
            domino = visited(random.randint(1, 12), random.randint(1, 12),
                             dict_dominos)
            if domino != None:
                self.player.append(domino)
                break

    def length(self):
        return len(self.player)

    def __str__(self):
        return str(self.player)

    def show_pile(self):
        return len(dict_dominos)

    def remove(self, index):
        return self.player.pop(index)

    def doubles(self):
        temp = 0
        for i in self.player:
            a, b = i.split("|")
            if a == b:
                temp = int(a)
        return temp

    def score(self):
        temp = 0
        for i in self.player:
            a, b = i.split("|")
            temp += int(a) + int(b)
        return temp

    def index(self, number):
        for i in range(0, len(self.player)):
            if self.player[i] == number:
                return i

    def lastnum(self, num):
        valid = []
        for i in self.player:
            a, b = i.split("|")
            if int(a) == num:
                valid.append(i)
            if int(b) == num and a != b:
                valid.append(i)
        return [i for i in valid]

    def refresh(self):
        self.player = []
        dict_dominos = {}
        arrange_dominos_doubles_first(counter, first_dice)
