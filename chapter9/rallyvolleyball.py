# rallyvolleyball.py

# volleyball.py
from random import random, randrange


def print_intro():
    print("This program simulates a game of volleyball between two teams "
          "called \"A\" and \"B\". The ability of each team is indicated "
          "by a probability (a number between 0 and 1) that the team wins "
          "the point when serving. Team A always has the first serve.")


def get_inputs():
    a = float(input("What is the probability team A wins a serve? "))
    b = float(input("What is the probability team B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def game_over(a, b):
    return (a == 30 or b == 30) and abs(a - b) >= 2


def sim_one_game(prob_a, prob_b):
    total_prob = prob_a + prob_b
    score_a = 0
    score_b = 0
    while not game_over(score_a, score_b):
        if (random() * total_prob) < prob_a:
            score_a += 1
        else:
            score_b += 1
    return score_a, score_b


def sim_n_games(n, prob_a, prob_b):
    wins_a = wins_b = shutouts_a = shutouts_b = 0
    for i in range(n):
        score_a, score_b = sim_one_game(prob_a, prob_b)
        if score_a > score_b:
            print("Game %d: A wins. Score for A: %d. Score for B: %d."
                  % (i + 1, score_a, score_b))
            wins_a += 1
            if score_b == 0:
                shutouts_a += 1
        else:
            print("Game %d: B wins. Score for A: %d. Score for B: %d."
                  % (i + 1, score_a, score_b))
            wins_b += 1
            if score_a == 0:
                shutouts_b += 1

    return wins_a, wins_b, shutouts_a, shutouts_b


def print_summary(wins_a, wins_b, shutouts_a, shutouts_b):
    n = wins_a + wins_b
    print("\nGames simulated: %d" % n)
    if wins_a > 0:
        print("Wins for A: %d (%0.1f%%). Shutouts for A: %d (%.1f%% of wins)."
              % (wins_a, float(wins_a) * 100 / n, shutouts_a,
                 float(shutouts_a) * 100 / wins_a))
    else:
        print("Wins for A: %d (%.1f%%). Shutouts for A: 0 (0.0%% of wins)."
              % (wins_a, float(wins_a) * 100 / n))
    if wins_b > 0:
        print("Wins for B: %d (%.1f%%). Shutouts for B: %d (%.1f%% of wins)."
              % (wins_b, float(wins_b) * 100 / n, shutouts_b,
                 float(shutouts_b) * 100 / wins_b))
    else:
        print("Wins for B: %d (%.1f%%). Shutouts for B: 0 (0.0%% of wins)."
              % (wins_b, float(wins_b) * 100 / n))


def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b, shutouts_a, shutouts_b = sim_n_games(n, prob_a, prob_b)
    print_summary(wins_a, wins_b, shutouts_a, shutouts_b)


if __name__ == '__main__':
    main()
