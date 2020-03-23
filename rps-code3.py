#!/usr/bin/env python3
import random
import time
import math
import tournament
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']
beat_moves = [
    'Spock smashes Scissors',
    "Spock vaporizes Rock",
    "Scissors cuts Paper",
    "Scissors decapitates Lizard",
    "Lizard eats Paper",
    "Lizard poisons Spock",
    "Rock crushes Scissors",
    "Rock crushes Lizard",
    "Paper disproves Spock",
    "Paper covers Rock"
]

"""The Player class is the parent class for all of the Players
in this game"""

# To print out the waht beat what text in the Game play_round()


def beat_text(one, two):
    for index in beat_moves:
        if one in index.lower() and two in index.lower():
            return index

# To check who won, player on or player two


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'rock' and two == 'lizard') or
            (one == 'scissors' and two == 'paper') or
            (one == 'scissors' and two == 'lizard') or
            (one == 'paper' and two == 'spock') or
            (one == 'paper' and two == 'rock') or
            (one == 'lizard' and two == 'spock') or
            (one == 'lizard' and two == 'paper') or
            (one == 'spock' and two == 'scissors') or
            (one == 'spock' and two == 'rock'))

# Print, linebreak, pause.


def printn(text, t=1):
    print(text+"\n")
    time.sleep(t)

# Choose the game type/rules/quit.


def choose_and_play():
    bot_players = [ReflectPlayer,
                   RandomPlayer,
                   CyclePlayer]
    while True:
        game_mode = input("1: Normal Game\n"
                          "2: Tournament Mode\n"
                          "3: Rules of the game\n"
                          "4: Quit from the game.\n"
                          "\n"
                          "Choose a game: ")
        print("")
        if game_mode == "1":
            opponent = random.choice(bot_players)()
            game = Game(HumanPlayer(), opponent)
            return game.play_game()
        elif game_mode == "2":
            return Tournament(bot_players)
        elif game_mode == "3":
            for line in beat_moves:
                printn(line)
        elif game_mode == "4":
            exit()


# Default player class, only plays rock


class Player:
    def __init__(self):
        self.def_name = "RockPlayer"

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# The RandomPlayer class, just random take a choice from the
# moves list (rock, paper,scissors)


class RandomPlayer(Player):
    def __init__(self):
        self.def_name = "RandomBot"

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass

# Copies the opponent last move, on the first round just takes a random choice
# after that copies the opponent moves


class ReflectPlayer(Player):
    def __init__(self):
        self.def_name = "ReflectBot"

    def move(self):
        try:
            return self.opponent_moves
        except AttributeError:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_moves = my_move
        self.opponent_moves = their_move


# Cycles trought the remaining moves, never plays the same move till all of
# them is played. First plays a random choice, and the rest at random


class CyclePlayer(Player):
    def __init__(self):
        self.def_name = "Cyclebot"
        self.cycle = []

    def move(self):
        if len(self.cycle) <= 1:
            self.cycle = ['rock', 'paper', 'scissors',
                          'spock', 'lizard']
            return random.choice(self.cycle)
        else:
            self.cycle.remove(self.my_moves)
            return random.choice(self.cycle)

    def learn(self, my_move, their_move):
        self.my_moves = my_move
        self.opponent_moves = their_move

# The HumanPlayer class, With input control to handle flase inputs
# With naming option


class HumanPlayer(Player):
    def __init__(self):
        self.def_name = "You"
        self.my_name()

    def move(self):
        while True:
            call = input(",".join(moves)+"? >")
            print("")
            if call.lower() in moves:
                return call.lower()

    def learn(self, my_move, their_move):
        pass

    def my_name(self):
        while True:
            name = input("What is your name(max 10 char):")
            print("")
            name = ''.join(name.split())
            if len(name) > 10:
                printn("Max 10 char long")
            elif len(name) == 0:
                printn("Type you name in(max 10 char)")
            else:
                self.def_name = name
                break

# The game Class to play the game


class Game:
    def __init__(self, p1, p2, t_game=False):
        self.tournament_game = t_game
        self.p1 = p1
        self.p2 = p2
        self.end_print = 0.2

# Choose the game type from the given list or quit, with input control

    def choose_game(self):
        if self.tournament_game is False:
            while True:
                type = input("Choose game type:\n"
                             "1: 3 Round game\n"
                             "2: Self choosen round game.\n"
                             "3: Play for 3 point lead.\n"
                             "4: Back to main menu\n"
                             "\n"
                             "Choose one: ")
                print("")
                if type == "1":
                    return self.simple_round_game()
                elif type == "2":
                    return self.round_game()
                elif type == "3":
                    return self.for_game()
                elif type == "4":
                    choose_and_play()
        else:
            self.simple_round_game()

# Play round method

    def play_round(self):
        move1 = self.p1.move().lower()
        move2 = self.p2.move().lower()
        printn(f"Round {self.round+1}:")
        printn(f"{self.p1.def_name} played: ----------> {move1}")
        printn(f"{self.p2.def_name} played: ----------> {move2}")
        if beats(move1, move2) is True:
            printn(beat_text(move1, move2))
            printn(f"{self.p1.def_name} Win!")
            self.points_p1 += 1
        elif beats(move2, move1) is True:
            printn(beat_text(move2, move1))
            printn(f"{self.p2.def_name} Win!")
            self.points_p2 += 1
        else:
            printn("Its a TIE!!!")
            self.tie += 1
        printn(f"Score : {self.p1.def_name}: {self.points_p1} points --- "
               f"{self.p2.def_name}: {self.points_p2} points")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

# Starting the game, setting up the variables for a fresh game. call the
# choose_game() to select the game type.
# if the game is fininshed call the game_end()

    def play_game(self):
        self.loser = Player()
        self.winner = Player()
        self.finished = False
        self.round = 0
        self.points_p1 = 0
        self.points_p2 = 0
        self.tie = 0
        printn("Rock -- Paper -- Scissors -- Spock -- Lizard")
        printn("Game start!")
        printn(f"Player 1: {self.p1.def_name}")
        printn(f"Player 2: {self.p2.def_name}")
        self.choose_game()
        self.game_end()

# The round_game mode, you can type in how many round do you want to play
# with input check was has to be a number

    def round_game(self):
        while True:
            rounds = input("How many rounds do you want?: ")
            print("")
            try:
                play_rounds = int(rounds)
                break
            except ValueError:
                printn("That's not a number")
        for index in range(play_rounds):
            self.play_round()
            self.round += 1

# Just a 3 round game.

    def simple_round_game(self):
        for index in range(3):
            self.play_round()
            self.round += 1

# The tie_breaker for prevent games to end witha tie.
# There has to be a winner!

    def tie_breaker(self):
        printn("-------------------The Game is Over-------------------------",
               self.end_print)
        printn("------------------------------------------------------------",
               self.end_print)
        printn("------------------***BUT ITS A TIE! ***---------------------",
               self.end_print)
        printn("------------------------------------------------------------",
               self.end_print)
        printn("--------------You have to play the TIE BREAKER!-------------",
               self.end_print)
        if isinstance(self.p1, ReflectPlayer):
            del self.p1.opponent_moves
        elif isinstance(self.p2, ReflectPlayer):
            del self.p2.opponent_moves
        self.play_round()
        self.round += 1

# The for_game, it is runing till one of the player have a 3 points lead

    def for_game(self):
        while self.finished is False:
            if abs(self.points_p1-self.points_p2) == 3:
                self.finished = True
            else:
                self.play_round()
                self.round += 1

# If the game is fiished check for tie, and print out the stats
# and the winner name

    def game_end(self):
        if self.points_p1 == self.points_p2:
            self.tie_breaker()
            self.game_end()
        else:
            printn("---------------------------------------------------------",
                   self.end_print)
            printn("--------------------Game Breaker!!!----------------------",
                   self.end_print)
            printn("---------------------------------------------------------",
                   self.end_print)
            printn(f"Round played: {self.round}", self.end_print)
            printn(f"Player 1 points: {self.points_p1}", self.end_print)
            printn(f"Player 2 points: {self.points_p2}", self.end_print)
            printn(f"Tie played: {self.tie}", self.end_print)
            if self.points_p1 > self.points_p2:
                printn(f"{self.p1.def_name} Won!", self.end_print)
                self.loser = self.p2
                self.winner = self.p1
            else:
                printn(f"{self.p2.def_name} Won!", self.end_print)
                self.loser = self.p1
                self.winner = self.p2
            printn("Game over!", self.end_print)
            input("Press enter to continue")
            if self.tournament_game is False:
                choose_and_play()

# THe tournamet class to play a tournamet game.


class Tournament:
    def __init__(self, bots):
        self.draw = tournament
        self.game_round = 8
        self.opponent = bots
        self.players = []
        self.player_names = []
        self.pairs = []
        self.human_players()

# Define how many human player want to play the tournamet

    def human_players(self):
        while True:
            players = input("How many Human Player want to play? ")
            print("")
            try:
                human_nr = int(players)
                if human_nr < 17:
                    break
                else:
                    printn("The player number is max 16")
            except ValueError:
                printn("That is not a number")

        for player in range(int(human_nr)):
            printn(f"Player {player+1} name:")
            human_players = HumanPlayer()
            self.players.append(human_players)
        self.randombots_and_groups()

# After the human players are given, fill up the rest spots with bots

    def randombots_and_groups(self):
        players_number = 16-len(self.players)

        for count in range(players_number):
            bot = random.choice(self.opponent)()
            bot.def_name = f"{bot.def_name} P{count+1}"
            self.players.append(bot)

        random.shuffle(self.players)
        self.bracketpairs(8)
        self.draw.draw_tour(self.player_names)
        self.play_tournament()

# Make player pairs to play each other in the tournament
# self.player_names are needed for the imported tournamet printing

    def bracketpairs(self, pair_number):
        for pair in range(pair_number):
            index = pair * 2
            p1 = self.players[index]
            p2 = self.players[index+1]
            self.player_names.append(p1.def_name)
            self.player_names.append(p2.def_name)
            self.pairs.append([p1, p2])

# Start to play the torunamet games

    def play_tournament(self):
        self.winner_names = []
        self.game_counter = 1
        for games in range(4):
            self.tour_play_games(self.pairs, self.game_round)
            self.game_round //= 2
        self.tournament_end()

# When the tournamet is finished print out the winner and restart the game

    def tournament_end(self):
        name_len = len(self.players[0].def_name)
        name = self.players[0].def_name
        line = math.ceil((58-name_len)//2)
        printn("----------------------------------------------------------")
        printn("--------------------Congratulations!!!--------------------")
        printn(line * "-" + name + line * "-")
        printn("-------------You Are The Tournament Winner!!!-------------")
        printn("----------------------------------------------------------")
        choose_and_play()

# Play the tournamet pair rounds, remove the loster from the players list
# make the new pairs from the winners
# the self.winner_names are neede for the imported tournamet printing

    def tour_play_games(self, players, round):
        for game_count in range(round):
            p1 = players[game_count][0]
            p2 = players[game_count][1]
            printn(f"\n---------------------Game {self.game_counter}--------"
                   "----------------")
            play = Game(p1, p2, True)
            play.play_game()
            self.winner_names.append(play.winner.def_name)
            self.players.remove(play.loser)
            self.game_counter += 1
        self.draw.draw_tour(self.player_names, self.winner_names)
        self.pairs = []
        self.bracketpairs(round//2)


if __name__ == '__main__':
    choose_and_play()
