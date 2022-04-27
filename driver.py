from wsgiref.validate import validator
import board

#Tabuleiro a ser manipulado


slots = int(input("Número de espaços no tabuleiro(ixj): "))

b = board.Board(slots)

#retorna TRUE se o tabuleiro existir a possibilidade de N queens e deixa b.queenspaces completas com espaço apropriado FALSE caso o contrario
def placeMoves():

    for move in b.getPossibleMoves():

        b.makeMove(move)

        if len(b.queenSpaces) == b.n:
            return True
        else:

            retVal = placeMoves()

            if retVal:
                return True

            else:
                b.removeMove(move)

    return False


#definido recursivamente
#três funcoes utilizadas
# - getPossibleMoves
# - makeMove
# - removeMove


if __name__ == "__main__":
    placeMoves()
    b.print()
