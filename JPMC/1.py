def getFinalData(data, updates):
    n = len(data)
    diff = [0] * (n + 2)
    for l, r in updates:
        diff[l] += 1
        diff[r + 1] -= 1
    curr = 0
    for i in range(1, n + 1):
        curr += diff[i]
        if curr % 2 == 1:
            data[i - 1] *= -1
    return data