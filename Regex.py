import re
from BM import BM
from KMP import KMP
from nltk.tokenize import sent_tokenize

# return string date in teks
def regexDate(teks):
    x = re.findall("[senin|Senin|Selasa|selasa|Rabu|rabu|Kamis|kamis|Jum'at|jumat|Sabtu|sabtu|Minggu|minggu|kemarin|Kemarin]*.*[\d]{1,2}[/ -][abdefgijklmnoprstuvyABDEFGIJKLMNOPRSTYUV0123456789]\w*[/ -][\d]{4}", teks)
    if (x):
        return x
    x = re.findall("[senin|Senin|Selasa|selasa|Rabu|rabu|Kamis|kamis|Jum'at|jumat|Sabtu|sabtu|Minggu|minggu|kemarin|Kemarin]*.*[\d]{1,2}[/ -][abdefgijklmnoprstuvyABDEFGIJKLMNOPRSTYUV0123456789]*[/ -][1234567890]{2}", teks)
    if (x):
        return x

# return list of number in teks
def regexJumlah(teks):
    x = re.finditer("[\d/.]+ ", teks)
    return x

# find nearest number to the pattern
def findJumlah(T, P):
    pIndex = KMP(T,P)
    vStart = 999
    vEnd = 999
    x = regexJumlah(T)
    hasil = []

    for match in x:
        temp = match.start() - pIndex[0]
        if (abs(temp) < vStart):
            vStart = match.start()
            vEnd = match.end()
    
    for i in range (vStart, vEnd):
        hasil.append(T[i])
    
    return ''.join(hasil)

def getSentences(teks, pattern):
    allSentences = sent_tokenize(teks)
    contain = []
    for i in range(len(allSentences)):
        ret = KMP(allSentences[i], pattern)
        if ret: #if not empty
            contain.append(allSentences[i])
    
    return contain



def main():
    f = open("text.txt", "r")
    teks = f.read()
    pattern = "COVID-19"
    # teks = "Kemarin, 13-Apr-2019 dari 421 kasus tersebut, 40.2 orang meninggal dunia dengan keterangan terpapar COVID-19 apa mau fauzan"
    # pattern = "meninggal dunia"
    T = teks.lower()
    P = pattern.lower()

    print(getSentences(T, P))



    # print("Kalimat : " + teks)
    # print("Keyword : " + pattern)
    # print("Jumlah : " + findJumlah(T,P))
    # print("Waktu : " + regexDate(teks)[0])
    
    
if __name__ == "__main__":
    main()