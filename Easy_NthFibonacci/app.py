n1 = 2
n2 = 6

def getNthFib(n):

    fib = {
        "0": 0,
        "1": 1,
    }

    if f"{n-1}" in fib:
        out = fib[f"{n-1}"]
    else:
        out = getNthFib(n - 2) + getNthFib (n - 1)
        fib[f"{n-1}"] = out

    return out

result = getNthFib(n2)
print(result)
