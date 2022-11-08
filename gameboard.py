class gameboard:
    def __init__(self):
        self.gameboard = []

    def isEmpty(self):
        return self.gameboard == []

    def addFront(self, item):
        self.gameboard.append(item)

    def addRear(self, item):
        self.gameboard.insert(0, item)

    def removeFront(self):
        return self.gameboard.pop()

    def removeRear(self):
        return self.gameboard.pop(0)

    def add(self, domino):
        a, b = domino.split("|")
        if len(self.gameboard) == 0:
            self.gameboard.append(domino)
        else:
            number = self.gameboard[len(self.gameboard) - 1]
            last = int(number.split("|")[1])
            if int(b) == last: self.gameboard.append(f"{b}|{a}")
            else: self.gameboard.append(domino)

    def __str__(self):
        return str(self.gameboard)

    def last_number(self, index):
        number = self.gameboard[index]
        return int(number.split("|")[1])

    def length(self):
        return int(len(self.gameboard))

    def refresh(self):
        self.gameboard = []
