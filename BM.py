class tuple:
    def __init__(self):
        self.var = ""
        self.val = 0

def lo(teks, pattern):
    variance = varChar(teks)
    lo = []
    
    for i in range (len(pattern)):
        ret = findLo(lo, teks[i])
        if (ret != -1):
            lo[ret].val = i
        else:
            t = tuple()
            t.var = teks[i]
            t.val = i
            lo.append(t)
    
    return lo

# mencari char di lo sudah ada atau belum
def findLo(lo, findvar):
    ret = -1
    for i in range(len(lo)):
        if (lo[i].var == findvar):
            ret = i
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
            

def main():
    f = open ("text.txt", "r")
    T = f.read()
    T = T.lower()

    # print(varChar(T))
    # lo = LO(T)
    # for i in range (len(lo)):
    #     print(lo[i].var + " " + str(lo[i].val))
    


if __name__ == "__main__":
    main()