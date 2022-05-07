class Board():

    ##########################################
    ####      Constroi o tabuleiro        ####
    ##########################################
    def __init__(self, n):
        self.n = n
        self.spaces = n * n

        #mostra os passos possiveis no começo 
        self.constraints = [0 for i in range(self.spaces)]

        #mantem o espaço final das rainhas
        self.queenSpaces = []


    ##########################################
    ####   Funções de movimento           ####
    ##########################################

    #Retorna os movimentos que não quebram restrições
    def getPossibleMoves(self):
        possibleMoves = []
        for move, numConstraints in enumerate(self.constraints):
            if numConstraints == 0:
                possibleMoves.append(move)
        return possibleMoves

    def makeMove(self, space):


        # Coloca a rainha
        self.queenSpaces.append(space)

        # Adiciona as condições de restição
        self.addOrRemoveConstraints(space)


    def removeMove(self, space):

        #remove a rainha
        self.queenSpaces.remove(space)

        #remove conflitos dependentes
        self.addOrRemoveConstraints(space, add=False)


    ##########################################
    ####   Logica das restrições n-queen  ####
    ##########################################

    #adiciona e remove as restrições nas linhas, colunas, e diagonais de um movimento
    def addOrRemoveConstraints(self, move, add=True):

        #escolher quando usar ou remover a função
        if (add):
            mutationFx = self.addConstraint
        else:
            mutationFx = self.removeConstraint

        row = move // self.n
        col = move % self.n
        rdStartRow = row + col
        ldStartRow = row - col

        for i in range(self.n):

            #linha
            mutationFx(self.rcToSpace(row, i))

            #coluna
            mutationFx(self.rcToSpace(i, col))

            # / diagonal
            if rdStartRow > -1:
                mutationFx(self.rcToSpace(rdStartRow, i))
                rdStartRow -= 1

            # \ diagonal
            if ldStartRow < self.n:
                mutationFx(self.rcToSpace(ldStartRow, i))
                ldStartRow += 1

    #adicione 1 ao contador de restrições
    def addConstraint(self, move):
        if not move == -1:
            self.constraints[move] += 1

    #remove 1 ao contador de restrições
    def removeConstraint(self, move):
        if not move == -1:
            self.constraints[move] -= 1

    ##########################################
    ####   Funções de utilidade          #####
    ##########################################

    #retorna o espaço correspondente # com base na linha e coluna indexada-0
    #retorna -1 se o espaço esta fora do tabuleiro
    # e.g.
    # rcToSpace(3,4) # espaço linha 3, coluna 4
    # > 28           # espaço correspondente em um 8x8
    def rcToSpace(self, row, col):
        space = row * self.n + col
        if space >= self.spaces or space < 0:
            return -1
        else:
            return space


    def print(self):
        for r in range(self.n):
            row = ""
            for c in range(self.n):
                if(self.rcToSpace(r,c) in self.queenSpaces):
                    row += "Q"
                else:
                    row += "-"
                row += "  "
            print(row)

