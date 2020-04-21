class tuple:
    def __init__(self):
        self.var = ""
        self.val = 0

def lo(teks, pattern):
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
            

def main():
    # f = open ("text.txt", "r")
    # T = f.read()
    # T = T.lower()
    
    T = "bddcbdacb"
    P = "abacab"
    
    

if __name__ == "__main__":
    main()