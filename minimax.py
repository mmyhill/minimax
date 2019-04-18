class node:
    def __init__(self, boardConfig):
        self.config = boardConfig[0]:boardConfig[boardConfig.find(" ") #string produced giving board config
        self.board = chess.Board().set_board_fen(boardConfig)
        self.val = self.calcValue()
        self.downs = []
    def calcValue(self):
        # 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
        total = 0
        #white
        total += self.config.count("p") * 10
        total += self.config.count("r") * 50
        total += self.config.count("n") * 30
        total += self.config.count("b") * 30
        total += self.config.count("q") * 90
        total += self.config.count("k") * 100
        #black
        total += self.config.count("P") * -10
        total += self.config.count("R") * -50
        total += self.config.count("N") * -30
        total += self.config.count("B") * -30
        total += self.config.count("Q") * -90
        total += self.config.count("K") * -100

    def addDowns(self, nodes):
        for x in range(len(nodes)):
            self.addDowns.append(nodes[x])

class gameTree:
    def.__init__(self):
        self.board = chess.Board()
        self.root = (node(board.fen())

    def calcBestMove(self):
        scoreToBeat = self.board.calcValue()
        queue[]
        self.addLevel()
        moveFound = False
        while(!moveFound):
            if(queue[0].calcValue() < scoreToBeat): #move to take has been found
                self.board = queue[0]
                moveFoond = True
            if(len(queue) == 0):
                addLevelRecurse(self.root)
            queue.pop()


    def addLevelRecurse(self, node):
        if(len(node.downs)) == 0):
            self.addChildrens(node)
        else:
            for child in node.downs:
                self.addLevelRecurse(child)


    def addChildrens(self, node):
        for move in node.board.legal_moves:
            node.board.push_san(move)
            new = node(node.board.fen())
            node.board.pop()
            node.addDowns(new)

    def play(self):
        while(!self.root.board.is_game_over):
            if(self.board.turn):#as of right now, will always be white
                self.calcBestMove()
            else:
                use = random.randint(0, len(board.legal_moves))
                board.push_san(board.legal_moves[use])#correct syntax?
            self.boardVisual()

    def player(self):
        while(!self.root.board.is_game_over):
            if(self.board.turn):#white is true, black is false. as of right now, will always be white
                self.calcBestMove()
            else:
                in = raw_input("what move would you like to make? (use chess algebraic notation)")
                self.board.push_san(in)
            self.boardVisual()


    def boardVisual(self): #print unicode chars in python print u'\u0420\u043e\u0441\u0441\u0438\u044f' >
        return = ""
        # 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
        for char in self.board.board_fen():
            if(char == 'r'): return += "\u2656" + " "
            elif(char == 'n'): return += "\u2658" + " "
            elif(char == 'b'): return += "\u2657" + " "
            elif(char == 'q'): return += "\u2655" + " "
            elif(char == 'k'): return += "\u2654" + " "
            elif(char == 'p'): return += "\u2659" + " "

            elif(char == 'R'): return += "\u265C" + " "
            elif(char == 'N'): return += "\u265E" + " "
            elif(char == 'B'): return += "\u265D" + " "
            elif(char == 'Q'): return += "\u265B" + " "
            elif(char == 'K'): return += "\u265A" + " "
            elif(char == 'P'): return += "\u265F" + " "

            elif(char.is_digit()):
                for x in range(int(char)):
                    return += "* "

            else: #char is /
                return += "\n"

        print(return)

#user interface
def main():
    in = raw_input("Would you like to play or simply observe the algorithm's actions against random moves?(y/n)")
    if(in == 'y'):
        gameTree.player()
    else:
        gameTree.play()

if __name__ == "__main__":
        main()
