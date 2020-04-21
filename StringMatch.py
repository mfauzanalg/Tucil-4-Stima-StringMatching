from copy import deepcopy

def KMP (T, P):
    bf = borderFunction(P)
    result = []
    n = len(T)
    m = len(P)

    i = 0 # for teks
    j = 0 # for pattern
    temp = j
    while (i < n):
        while (j < m and i < n):
            if (j == -99):
                j = temp+1
                i += 1
            if (j == m-1 and P[j] == T[i]):
                result.append(i-m+1)
            if (T[i] == P[j]):
                i += 1;
                j += 1;
            else: # miss match
                temp = j
                j = bf[j]
        i+=1

    return result

def borderFunction(pattern):
    j = len(pattern);
    bf = []
    for i in range (j):
        bf.append(calculateBF(pattern, i))
        bf[0] = -99
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
    # f = open ("text.txt", "r")
    # T = f.read()
    # P = "COVID-19"
    # T = "abacaabaccabacabaabb"
    # P = "abacab"
    T = "saya adalah fauzan keren, memang fauzan keren"
    P = "fauzan"
    print(KMP(T,P))
    # print(borderFunction(P))


if __name__ == "__main__":
    main()