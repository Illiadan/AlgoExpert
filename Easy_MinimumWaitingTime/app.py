queries = [3, 2, 1, 2, 6]

def minimumWaitingTime(queries):

    queriesSorted = sorted(queries)
    waitingTime = []

    preTime = 0
    for time in queriesSorted:
        waitingTime.append(preTime)
        preTime += time
    
    return sum(waitingTime)

result = minimumWaitingTime(queries)
print(result)
