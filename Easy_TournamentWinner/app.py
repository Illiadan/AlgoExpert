competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 1, 1]

def tournamentWinner(competitions, results):
    
    out = []
    compIdx = 0
    resIdx = 0
    while compIdx < len(competitions) and resIdx < len(results):
        matchWinner = competitions[compIdx][abs(results[resIdx] - 1)]
        out.append(matchWinner)
        compIdx += 1
        resIdx += 1
    
    return max(set(out), key = out.count)

result = tournamentWinner(competitions, results)
print(result)
