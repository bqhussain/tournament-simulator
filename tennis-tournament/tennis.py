from player import Player
import numpy as np
from statistics import mode
import itertools
# short set format


def getPairs(playerslist):
    # playerslist.append(None) # To ensure that all elements are included, you could simply extend the list by None.
    pairs = zip(playerslist[::2], playerslist[1::2])
    #[(a,b), (c,d)]
    return list(pairs)


def createPlayers(n):
    participants = {}
    k = 0 #  Counter to check the condition
    # while k < n:
    for k in range(n):
        key = f'Player{k}'
        participants[key] = Player(f'Player{k}')
        
    matchmaking = list(participants.items())
    np.random.shuffle(matchmaking)
    matched = dict(matchmaking)
    return matched
    # {
    # 'Player1':'Player()
    # }


def playGame(p1, p2):

    p1score = 0
    p2score = 0
    p1game = 0
    p2game = 0

    n = 4
    deuce = 3
    p1PointsTable = []
    p2PointsTable = []
    gameFlag = False

    while True:

        while gameFlag == False:
            # and p2score > 3 and p1score > 3

            if (p1score == deuce and p2score == deuce):
                print('###########')
                print('There is a DEUCE')
                print(f'{p1.name}', p1PointsTable)
                print(f'{p2.name}', p2PointsTable)
                print('###########')
                # p1score-=2
                # p2score-=2
                deuce += 1
                n = n+1

            if p1score == n and p2score < n or sum(p1PointsTable) == n:

                print(f'{p1.name} wins the game ')
                print(f'{p1.name}', p1PointsTable)
                print(f'{p2.name}', p2PointsTable)
                # print("Player 1 score:", p1score)
                # print("Player 2 score:", p2score)
                p1PointsTable.clear()
                p2PointsTable.clear()
                p1game += 1

                gameFlag = True
                return p1
                
            

            if p2score == n and p1score != n or sum(p2PointsTable) == n:
                print(f'{p2.name} wins the game ')
                print(f'{p1.name}', p1PointsTable)
                print(f'{p2.name}', p2PointsTable)
                # print("Player 1 score:", p1score)
                # print("Player 2 score:", p2score)
                p2PointsTable.clear()
                p1PointsTable.clear()
                p2game += 1
                gameFlag = True
                return p2
                

            if(p1.scorePoints() == 1):
                p1score += 1
                p1PointsTable.append(1)
                p2PointsTable.append(0)
                break

            if (p2.scorePoints() == 1):
                p2score += 1
                p2PointsTable.append(1)
                p1PointsTable.append(0)
                break

        if gameFlag == True:

            break

            # elif p2score ==4 and p1score==4:
            #     p2score-=2
            #     p1score-=2

            # elif p1game==4 and p1game>p2game and p1game-p2game==2:
            #     print(f'{p1.name} wins the match ')
            #     break
            # elif p2game==4 and p2game>p1game and p2game-p1game>=2:
            #     print(f'{p2.name} wins the match ')
            #     break
            # elif p1game ==4 and p2game ==4 and p1game-p2game !=2:
            #     p1game-=2
            #     p2game-=2
            # elif p1score or p2score >10:
            #     print('Something Wrong')


def playMatch(p1, p2):
    rounds = 6
    gameresults = []
    for i in range(0, rounds):
        gameresults.append(playGame(p1, p2))

    # print(mode(gameresults))
    print("End of Set ")
    return mode(gameresults)


def playSet(p1, p2):
    set = 3
    setResults = []
    for i in range(0, set):
        setResults.append(playMatch(p1, p2))

    print(setResults[0].name, 'Is the Winner')
    return mode(setResults)


def simulateTournament(participants):

    next_round = []
    while True:
        out = dict(itertools.islice(participants.items(), 2))

        p1 = out[next(iter(out))]
        out.pop(next(iter(out)))
        participants.pop(next(iter(participants)))
        p2 = out[next(iter(out))]
        participants.pop(next(iter(participants)))
        out.pop(next(iter(out)))
        print(p1.name, " VS ", p2.name)
        next_round.append(playSet(p1, p2))

        if participants == {}:
            break

    return next_round


def simulateRound(qualifiedplayers):

    playersQualified = []
    # while len(qualifiedplayers)!=1:
    for i in getPairs(qualifiedplayers):
        print("Different Round")
        print((i[0].name, "VS", i[1].name))
        playersQualified.append(playSet(i[0], i[1]))
    # print(playersQualified,'YOOOO')
    if len(playersQualified) != 1:
        #     getPairs(playersQualified)
        #     print(playersQualified, 'YOOOO')
        return simulateRound(playersQualified)
        # playersQualified.clear()
        # simulateRound(getPairs(playersQualified))
    elif len(playersQualified) == 1:
        return playersQualified
    # pass


participants = createPlayers(4)
# print(participants)
results = simulateTournament(participants)
print(results, 'results')
print(simulateRound(results))

# while len(results)!=1:
#     pass

# print(participants)
# out = dict(itertools.islice(participants.items(), 2))
#
# print(out)
# out.pop(next(iter(out)))
# out.pop(next(iter(out)))
# print(out)
# simulateTournament(participants)

# p1=Player('John')
# p2=Player('Rodger')
#
# playSet(p1,p2)


# print('Enter number of players between 2-64: ')
# noOfPlayers = int(input())
# print(createPlayers(noOfPlayers))


# listOfPlayers=[]
# for i in range(0,noOfPlayers):
#     listOfPlayers.append(f'Player{i+1}')
# listOfPlayers=random.sample(listOfPlayers, noOfPlayers)


# random.shuffle(listOfPlayers)
