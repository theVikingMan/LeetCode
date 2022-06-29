import collections

def tournamentWinner(competitions, results):
    res = ''
    points = collections.defaultdict(int)
    resAmount = 0

    for teams, winner in zip(competitions, results):
        home, away = teams[0], teams[1]
        if winner == 0:
            points[away] += 1
            if points[away] > resAmount:
                res = away
                resAmount = points[away]
        else:
            points[home] += 1
            if points[home] > resAmount:
                res = home
                resAmount = points[home]
    return res

print(tournamentWinner([["HTML", "C#"],["C#", "Python"],["Python", "HTML"]], [0,0,1]))