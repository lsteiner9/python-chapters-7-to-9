# comparevolleyball.py
from chapter9 import rallyvolleyball
from chapter9.volleyball import sim_n_games


def compare_scores(a, b, wins_a, wins_b, r_wins_a, r_wins_b):
    if a > b:
        print("\nWins for A in normal scoring: %d. In rally scoring: %d." % (wins_a, r_wins_a))
        if wins_a > r_wins_a:
            print("A is the better team. Rally scoring reduces their game advantage.")
        elif wins_a == r_wins_a:
            print("A is the better team. Rally scoring does nothing to their game advantage.")
        else:
            print("A is the better team. Rally scoring magnifies their game advantage.")
    else:
        print("\nWins for B in normal scoring: %d. In rally scoring: %d." % (wins_b, r_wins_b))
        if wins_b > r_wins_b:
            print("B is the better team. Rally scoring reduces their game advantage.")
        elif wins_b == r_wins_b:
            print("B is the better team. Rally scoring does nothing to their game advantage.")
        else:
            print("B is the better team. Rally scoring magnifies their game advantage.")


def main():
    print("This program compares simulations of volleyball games played with two different scoring systems.")
    n = int(input("How many games to simulate: "))
    a = float(input("What is the skill level of team A? "))
    b = float(input("What is the skill level of team B? "))
    print("Normal scoring: ")
    wins_a, wins_b, shutouts_a, shutouts_b = sim_n_games(n, a, b)
    print("Rally scoring: ")
    r_wins_a, r_wins_b, r_shutouts_a, r_shutouts_b = rallyvolleyball.sim_n_games(n, a, b)
    compare_scores(a, b, wins_a, wins_b, r_wins_a, r_wins_b)


if __name__ == '__main__':
    main()
