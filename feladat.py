#1
def beolvasas():
 with open ("./info.txt", "r" ,encoding="UTF-8") as fm:
    for sor in fm:
        print(sor,file=fm)

#2     
def szavak_szama(mondat):
    with open("./info.txt", "r", encoding="UTF-8") as fm:
        for sor in fm:
            print(sor)  

    szavak = mondat.split() 
    return len(szavak)  


mondat = "Ez egy példa mondat."
 

#3
def szöveg_visszafelé(szöveg):
    with open("./info.txt", "r", encoding="UTF-8") as fm:
        teljes_szöveg = fm.read()
        fordított_szöveg = teljes_szöveg[::-1]
        print(fordított_szöveg)

    return szöveg[-1]


#4
def listaban_a_szavak(mondat):
    with open("./info.txt", "r", encoding="UTF-8") as fm:
        szavak = fm.read().split()

    print(szavak)  
    return szavak  
    


print(szavak_szama(mondat))
print(szöveg_visszafelé(szöveg="info.txt"))

 




