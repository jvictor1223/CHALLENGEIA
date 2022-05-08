from wsgiref.validate import validator

import board

#Tabuleiro a ser manipulado


#slots = int(input("Número de espaços no tabuleiro(ixj): "))
slots = 4

#retorna TRUE se o tabuleiro existir a possibilidade de N queens e deixa b.queenspaces completas com espaço apropriado FALSE caso o contrario
def placeMoves(response):
    
    for move in b.getPossibleMoves():
        
        response['sumIterations'] = response['sumIterations'] + 1
        b.makeMove(move)

        if len(b.queenSpaces) == b.n:
            return  response
        else:

            retVal = placeMoves(response)

            if retVal['status']:
                return response

            else:
                b.removeMove(move)

    response['status'] = False
    return response


#definido recursivamente
#três funcoes utilizadas
# - getPossibleMoves
# - makeMove
# - removeMove

numberOfExecutions = 10
sumAllIteractions = 0
for x in range(numberOfExecutions):
    b = board.Board(slots)
    if __name__ == "_main_":
        response = {'status': True, 'sumIterations': 0}
        response = placeMoves(response)
        sumAllIteractions += response['sumIterations']
        print('Number of iteractions', response['sumIterations'])
        b.print()


print('Average iterations ', sumAllIteractions/numberOfExecutions)