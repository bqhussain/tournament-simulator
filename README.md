# Tennis Tournament Simulator

### Assumptions
- The code simulates a single elimination tournament
- There are 3 or 5 Sets, and each set consists of 6 games.
- The scoring is done with 0s and 1s. 4 is considered a game point; whoever wins 4 points first wins the game. If both players score 3, then it is a deuce.
- The code only works for the power of 2 number of players in-order to do the match scheduling equally.
- There code works for 3 or 5 sets
- There are 6 rounds in each set.
- The player who wins the most number of rounds wins the set.
- The player who wins the most number of sets wins the match and qualifies to the next stage.
- If there is a tie between rounds, a tie-breaker round decides the winner.

### Overview
- `createPlayers(n)` takes an integer which should be the power of 2 and returns a list of players who will be competing against each other in the tournament.
- `playGame(playerObj1,playerObj2)` expects two-player objects as parameters to play against each other. This is an essential function, and it simulates how the game works in tennis. A p1ServeFlag is defined, which helps switch the serve between players, so a different player serves each game. Firstly, one player takes a shot and the program checks if he scores or misses; if he misses, the second player takes a shot back, which continues unless someone scores. The game continues until one player scores a game point, i.e. score 4 points, and there is no deuce condition, and that player is then declared the winner for the game, and then the next game starts. This continues for 6 rounds. If both players have 3 points, there is a deuce, and one player needs to score 2 consecutive points to win the game.  Therefore, a condition that checks for deuce and then increases the game-ending condition and continues the matching until a player scores 2 consecutive points. The function returns the player who won the game.
- `playMatch(playerObj1,playerObj2)` simulates the set by calling `playGame(playerObj1,playerObj2)` and finally returns the result for one set.
- `playSet(playerObj1,playerObj2)` calls `playMatch(playerObj1,playerObj2)` and simulates the game 6 times for each set. If there are 3 sets then 18 games are played.
- `simulateTournament(list)` takes the output of `createPlayers(n)` and starts the tournament. This function is recursively called until the final winner is decided. The function starts by calling getPairs(list) which returns a shuffled list of tuples, where each tuple contains two player objects who will play against each other. Then, it loops over the list of tuples, picking one tuple at a time and calling playSet(playerobj1,playerobj2), which simulates one set a time by calling `playMatch(playerObj1,playerObj2)`. `playMatch(playerObj1,playerObj2)` simulates 6 round by calling `playGame(playerObj1,playerObj2)` for each game. `playGame(playerObj1,playerObj2)` returns the winner for each game.
- `changeServerFlag(flag)` changes the player who is serving after each game.
- `getPairs(list)` returns the list of tuples, where each tuple has 2 player objects.
- `writeMatchFixtures()` writes the fixtures and results to a file.
