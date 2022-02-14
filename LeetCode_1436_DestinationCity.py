def solution(paths):
    departure = set()
    for city in paths:
        departure.add(city[0])
    for city in paths:
        if city[1] in departure:
            continue
        else:
            return city[1] 

print(solution([["B","C"],["D","B"],["C","A"]]))