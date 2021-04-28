# rball.py
from random import random


def print_intro():
    print("This program simulates a game of racquetball between two players "
          "called \"A\" and \"B\". The abilities of each player is indicated "
          "by a probability (a number between 0 and 1) that the player wins "
          "the point when serving. Player A always has the first serve.")


def get_inputs():
    a = float(input("What is the probability player A wins a serve? "))
    b = float(input("What is the probability player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def game_over(a, b):
    return a == 15 or b == 15


def sim_one_game(prob_a, prob_b):
    a_serving = True
    score_a = 0
    score_b = 0
    while not game_over(score_a, score_b):
        if a_serving:
            if random() < prob_a:
                score_a += 1
            else:
                a_serving = False
        else:
            if random() < prob_b:
                score_b += 1
            else:
                a_serving = True
    return score_a, score_b


def sim_n_games(n, prob_a, prob_b):
    wins_a = wins_b = 0
    for i in range(n):
        score_a, score_b = sim_one_game(prob_a, prob_b)
        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1
    return wins_a, wins_b


def print_summary(wins_a, wins_b):
    n = wins_a + wins_b
    print("\nGames simulated: %d" % n)
    print("Wins for A: %d (%0.1f%%)" % (wins_a, float(wins_a) / n))
    print("Wins for B: %d (%0.1f%%)" % (wins_b, float(wins_b) / n))


def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = sim_n_games(n, prob_a, prob_b)
    print_summary(wins_a, wins_b)


if __name__ == '__main__':
    main()
