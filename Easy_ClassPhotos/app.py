redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]

def classPhotos(redShirtHeights, blueShirtHeights):
    
    rSHSorted = sorted(redShirtHeights)
    bSHSorted = sorted(blueShirtHeights)
    out = []

    for i in range(len(redShirtHeights)):
        if rSHSorted[i] < bSHSorted[i]:
            out.append(0)
        elif rSHSorted[i] > bSHSorted[i]:
            out.append(1)
        else:
            out.append(2 * len(redShirtHeights))
    
    if sum(out) == 0 or sum(out) == len(redShirtHeights):
        return True

    return False

result = classPhotos(redShirtHeights, blueShirtHeights)
print(result)
