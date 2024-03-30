redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    
    rSSSorted = sorted(redShirtSpeeds)
    if fastest:
        bSSSorted = sorted(blueShirtSpeeds, reverse=True)
    else:
        bSSSorted = sorted(blueShirtSpeeds)

    totalSpeed = 0
    for i in range(len(redShirtSpeeds)):
        totalSpeed += max(rSSSorted[i], bSSSorted[i])
    
    return totalSpeed

result = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
print(result)
