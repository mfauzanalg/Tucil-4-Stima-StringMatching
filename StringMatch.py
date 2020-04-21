from copy import deepcopy

def KMP (teks, pattern):
    


def borderFunction(pattern):
    j = len(pattern);
    bf = []
    for i in range (j):
        bf.append(calculateBF(pattern, i))
    return bf

def calculateBF(pattern, j):
    ret = 0
    stop = False
    pref = []
    suf = []

    # calculate pref
    input = []
    for i in range (0, j, 1):
        input.append(pattern[i])
        pref.append(deepcopy(input))

    # calculate suf
    input.clear()
    for i in range (j-1, 0, -1):
        input.insert(0,pattern[i])
        suf.append(deepcopy(input))

    # looking for b[k]
    i = len(suf)-1
    while i >= 0 and not(stop):
        if (pref[i] == suf[i]):
            ret = len(pref[i])
            stop = True
        i -= 1

    return ret

def main():
    f = open ("text.txt", "r")
    T = f.read()
    print(borderFunction("ababababca"))


if __name__ == "__main__":
    main()