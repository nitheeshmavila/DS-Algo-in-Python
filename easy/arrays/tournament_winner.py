#0(N) N is the no of competitons
# 0(d) space where d is the no of teams

def tournament_winner(competitions, results):

    current_best_team = ""
    current_best_score = 0
    points = {}

    for idx, competition in enumerate(competitions):

        result = results[idx]

        winner = competition[0] if result == 1 else competition[1]

        points[winner] = points.get(winner, 0) + 1

        if points[winner] > current_best_score:
            current_best_team = winner
            current_best_score = points[winner]
    return current_best_team

