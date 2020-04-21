class tuple:
    def __init__(self):
        self.var = ""
        self.val = 0

def lastOccurence(teks, pattern):
    variation = varChar(teks)
    lo = []
    
    for i in range (len(variation)):
        item = tuple()
        item.var = variation[i]
        item.val = last(pattern, variation[i])
        lo.append(item)
    
    return lo


# mencari last occurance
def last(list, char):
    ret = -1
    found = False
    i = len(list)-1
    while i >= 0 and not(found):
        if (list[i] == char):
            ret = i
            found = True
        i -= 1
    return ret


# mengembalikan variasi character di teks
def varChar(teks):
    var = []
    for i in range (len(teks)):
        ret = findVar(var ,teks[i])
        if (ret == -1):
            var.append(teks[i])
    return var


# mencari index di varchar sudah ada atau belum
def findVar(var, findvar):
    ret = -1
    for i in range(len(var)):
        if (var[i] == findvar):
            ret = i
    return ret

# mencari nilai char di Lo
def valueLo(char, lo):
    for i in range (len(lo)):
        if (lo[i].var == char):
            return lo[i].val


def BM(T, P):
    lo = lastOccurence(T, P)
    result = []
    n = len(T)
    m = len(P)
    j = m-1 # for pattern
    i = j # for teks
    
    while(i < n):
        while(j < m and i < n):
            if (j == 0 and T[i] == P[j]):
                result.append(i)
                i = i + m
                j = m-1
            elif (T[i] == P[j]):
                i-=1
                j-=1

            # missmatch
            elif (T[i] != P[j]): 
                # kasus ketiga
                if (valueLo(T[i], lo) == -1):
                    j = m-1
                    i = i + m
                # kasus pertama
                elif (valueLo(T[i], lo) < j):
                    j = m-1
                    i = i + m - (valueLo(T[i], lo) + 1)
                # kasus kedua
                elif (valueLo(T[i], lo) > j):
                    i = i + m - j
                    j = m-1
    
    return result
            
                
def main():
    # f = open ("text.txt", "r")
    # T = f.read()
    # T = T.lower()
    
    T = "saya adalah fauzan keren, memang fauzan keren, sudah tentu fauzan keren"
    P = "fauzan"

    print(BM(T,P))
    
    

if __name__ == "__main__":
    main()