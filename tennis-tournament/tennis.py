from player import Player
from statistics import mode
import logging
from random import sample

roundCounter = 1
p1ServeFlag = False
setCounter = 1
logging.basicConfig(filename='tournamentSummary.log',
                    level=logging.INFO, format='%(message)s')
stageCount = 1

# Input n can be any string or list.
# writeMatchFixtures writes match fixtures and results to a fix.txt file.


def writeMatchFixtures(n):

    global stageCount

    with open('fix.txt', 'a') as f:

        if type(n) == list:

            f.write(f'Stage {stageCount}')
            f.write("\n")
            f.write("\n")

            for i in n:
                f.write(f'{i.name}')
                f.write("\n")

            f.write("\n")
            stageCount += 1
            f.write("\n")

        else:

            f.write(n)
            f.write("\n")


# Input format playersList = [a,b,c]
# getPairs takes a list and make tuples and returns a list of tuples with 2 elements in each tuple.
# Returned format # [(a,b), (c,d)]
def getPairs(playersList):

    pairs = zip(playersList[::2], playersList[1::2])
    return list(pairs)


# Expected input value for n = 2 or 4 or 8 or 16 or 32 or 64
# createPlayers takes an integer n and returns a shuffled list of n number of player objects.
# Returned format #[obj1,obj2,obj3]
def createPlayers(n):

    playersList = [Player(f'Player{player+1}') for player in range(n)]
    return sample(playersList, len(playersList))


# Input p1 and p2 are the player objects
# playGame simulates a game of tennis
# this function returns winner of each round.
def playGame(p1, p2):

    p1score = 0
    p2score = 0
    n = 4
    deuce = 3
    p1PointsTable = []
    p2PointsTable = []

    gameFlag = False
    global p1ServeFlag

    logging.info('---Round Starts---')

    while gameFlag == False:

        if (p1score == deuce and p2score == deuce):
            logging.info('----------')
            logging.info('DEUCE')
            logging.info('Points Table for Deuce')
            logging.info(f'{p1.name}:{p1PointsTable}')
            logging.info(f'{p2.name}:{p2PointsTable}')
            logging.info('----------')
            deuce += 1
            n = n+1

        if p1score == n and p2score < n or sum(p1PointsTable) == n:

            logging.info(f'{p1.name} wins Round {roundCounter} ')
            logging.info(f'Round {roundCounter} Results')
            logging.info(f'{p1.name}: {p1PointsTable}')
            logging.info(f'{p2.name}:{p2PointsTable}')
            logging.info(f"{p1.name} score: {p1score}")
            logging.info(f"{p2.name} score: {p2score}")
            p1PointsTable.clear()
            p2PointsTable.clear()

            gameFlag = True
            return p1

        if p2score == n and p1score != n or sum(p2PointsTable) == n:

            logging.info(f'{p2.name} wins Round {roundCounter} ')
            logging.info(f'Round {roundCounter} Results')
            logging.info(f'{p1.name}: {p1PointsTable}')
            logging.info(f'{p2.name}:{p2PointsTable}')
            logging.info(f"{p1.name} score: {p1score}")
            logging.info(f"{p2.name} score: {p2score}")
            p2PointsTable.clear()
            p1PointsTable.clear()

            gameFlag = True

            return p2

        if p1ServeFlag == False:

            if(p1.scorePoints() == 1):
                p1score += 1
                p1PointsTable.append(1)
                p2PointsTable.append(0)
                continue

            if (p2.scorePoints() == 1):
                p2score += 1
                p2PointsTable.append(1)
                p1PointsTable.append(0)
        else:

            if (p2.scorePoints() == 1):
                p2score += 1
                p2PointsTable.append(1)
                p1PointsTable.append(0)
                continue
            if (p1.scorePoints() == 1):
                p1score += 1
                p1PointsTable.append(1)
                p2PointsTable.append(0)


def changeServeFlag():

    global p1ServeFlag
    if p1ServeFlag == False:
        p1ServeFlag = True
    elif p1ServeFlag == True:
        p1ServeFlag = False


def playMatch(p1, p2):

    rounds = 6
    gameresults = []
    numOfWinsP1 = 0
    numOfWinsP2 = 0
    global roundCounter

    for i in range(rounds):
        logging.info(f'Round No: {roundCounter}')

        gameResult = playGame(p1, p2)
        changeServeFlag()
        roundCounter += 1

        if gameResult.name == p1.name:
            numOfWinsP1 += 1
        else:
            numOfWinsP2 += 1
        gameresults.append(gameResult)

    if numOfWinsP1 == numOfWinsP2:  # If both win equal number of rounds
        logging.info(f'Round No: {roundCounter}')
        roundCounter += 1
        gameresults.append(playGame(p1, p2))
        changeServeFlag()

    logging.info(f"End of Set {setCounter} ")

    logging.info(f"Set {setCounter} Results ")

    counter = 1
    for game in gameresults:
        logging.info(f'Round {counter} Results {game.name}')
        counter += 1
    roundCounter = 1
    return mode(gameresults)


def playSet(p1, p2):
    global setCounter
    set = 3
    setResults = []

    for i in range(0, set):
        logging.info(f'Starting Set {setCounter}')
        setResults.append(playMatch(p1, p2))
        setCounter += 1

    winner = mode(setResults)
    logging.info(f'{winner.name} Is the Winner for this match')
    writeMatchFixtures(f'{winner.name} Qualified')

    return winner


def simulateTournament(qualifiedplayers):

    writeMatchFixtures(qualifiedplayers)
    playersQualified = []
    logging.info('Start of Phase')
    for players in getPairs(qualifiedplayers):
        writeMatchFixtures(
            f'Match against: {players[0].name}  VS {players[1].name}')
        logging.info(f'Match against: {players[0].name} VS {players[1].name}')
        playersQualified.append(playSet(players[0], players[1]))
    logging.info('End of Phase')
    if len(playersQualified) != 1:

        return simulateTournament(playersQualified)

    elif len(playersQualified) == 1:
        logging.info('End of Tournament')
        win = f'The Winner of the Tournament is {playersQualified[0].name}'
        logging.info(win)
        writeMatchFixtures(win)


def main():

    # Only works for powers of 2

    participants = createPlayers(8)
    simulateTournament(participants)


main()
