import re
from BM import BM
from KMP import KMP
from nltk.tokenize import sent_tokenize

#
def removal(the_list, val):
    return [value for value in the_list if value != val]

# return string date in teks
def regexDate(teks):
    x = re.findall("[senin|Senin|Selasa|selasa|Rabu|rabu|Kamis|kamis|Jum'at|jumat|Sabtu|sabtu|Minggu|minggu|kemarin|Kemarin]*.*[\d]{1,2}[/ -][abdefgijklmnoprstuvyABDEFGIJKLMNOPRSTYUV0123456789]\w*[/ -][\d]{4}", teks)
    if (x):
        return x

# return list of number in teks
def regexJumlah(teks):
    x = re.finditer("[\d/.]+ ", teks)
    return x

# find nearest number to the pattern
def findJumlah(T, P):
    pIndex = BM(T,P)
    vStart = 999
    vEnd = 999
    x = regexJumlah(T)
    hasil = []
    temp2 = 999

    for match in x:
        temp = match.start() - pIndex[0]
        if (abs(temp) < abs(temp2)):
            temp2 = temp
            vStart = match.start()
            vEnd = match.end()
    
    for i in range (vStart, vEnd):
        hasil.append(T[i])
    
    return ''.join(hasil)


def getContain(teks, pattern):
    allSentences = sent_tokenize(teks)
    contain = []
    for i in range(len(allSentences)):
        ret = KMP(allSentences[i], pattern)
        if ret: #if not empty
            contain.append(allSentences[i])
    return contain


def extractInfo(contain, teks, pattern):
    kalimat = []
    jumlah = []
    waktu = []
    for i in range(len(contain)):
        kalimat.append(contain[i])

        if not(findJumlah(contain[i],pattern)): # kalo ganemu angka
            jumlah.append("0")
        else:
            jumlah.append(findJumlah(contain[i],pattern))
        
        if (regexDate(contain[i])): # kalo nemu tanggal
             waktu.append(regexDate(contain[i])[0])
        else:
            waktu.append("-")
    
    return kalimat, jumlah, waktu


def main():
    f = open("text.txt", "r")
    teks = f.read()
    pattern = "terkonfirmasi positif"
    T = teks.lower()
    P = pattern.lower()


    contain = getContain(T,P)
    kalimat, jumlah, waktu = extractInfo(contain,T,P)

    for i in range (len(kalimat)):
        print("")
        print("kalimat")
        print(kalimat[i])
        print("jumlah")
        print(jumlah[i])
        print("waktu")
        print(waktu[i])

    
    
if __name__ == "__main__":
    main()