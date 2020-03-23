# Udacity - Intro the Programming Python - rock-paper-scissors Project

The second project for Udacity Intro to Programming Nanodegree python part. A rock-paper-scissor game with extra features.

## Rules of th Game

Rock - Paper - Scissors - Spock - Lizard 

- Spock smashes Scissors
- Spock vaporizes Rock
- Scissors cuts Paper
- Scissors decapitates Lizard
- Lizard eats Paper
- Lizard poisons Spock
- Rock crushes Scissors
- Rock crushes Lizard
- Paper disproves Spock
- Paper covers Rock

## To Play
Run the *rps-code3.py* python file.

Files needed:
- rps-code3.py
- tournament.py (To draw the tournament bracket)

## Bots:
- **RandomBot** (Plays a random move)
- **ReflectBot** (First move is random, after that it will play what the opponent played in the previous round)
- **CycleBot** (First move is random, after that it cycles trough from the rest moves at random. When it run our of moves it will start over.)

## Modes:

### Normal game (1 vs 1 game mode) 
Is a player versus bot games. The bot will be choosen from(**RandomBot, ReflectBot, CycleBot**)

### Game Types:

#### 3 Round Game:
A **simple 3 round game**, the winner will be decided from 3 rounds. If it's end with a tie there will be a tie breaker game.
**Someone has to win!**

#### Self choosen round game:
You can set the **number of rounds** do you want to play. 
If it's end with a tie there will be a tie breaker game. **Someone has to win!**

#### Play for 3 point lead:
You will play for a 3 point lead, there is no round limitation, you just have to **get a 3 point lead** on your opponent.

## Torunamet Mode
It is a **16 player** bracket torunament game mode. A random tournament bracket of bot and human players.
**Be the Best** and win to get the Tournament winner Trophy -> :trophy:
