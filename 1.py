SyndromS=["000", "001", "010", "011", "100", "101", "110", "111"]
SymbolOshibki=["нет ошибки","r3", "r2", "i3", "r1", "i2", "i1", "i4"]
PosledSym=["r1", "r2", "i1", "r3", "i2", "i3", "i4"]

print("Введите 7-ми значное число в двоичной сс:")
chislo=input()
elements=list(str(chislo))
if (chislo.isdigit()==False) or(int(chislo) >=10000000) or (int(chislo) <1000000) or ("2" in elements) or ("3" in elements) or ("4" in elements) or ("5" in elements) or ("6" in elements) or ("7" in elements) or ("8" in elements) or ("9" in elements):
    print("Ошибка")
else:
    s1=(int(elements[0])+int(elements[2])+int(elements[4])+int(elements[6]))%2
    s2=(int(elements[1])+int(elements[2])+int(elements[5])+int(elements[6]))%2
    s3=(int(elements[3])+int(elements[4])+int(elements[5])+int(elements[6]))%2
    S=str(s1*100+s2*10+s3)
    if len(S)==2:
        S="0"+S
    if len(S)==1:
        S="00"+S

    PozS=SyndromS.index(S)
    if PozS!=0:
        Osh=PosledSym.index(SymbolOshibki[PozS])

        if str(elements[Osh])=="0":
            elements[Osh]="1"
        else:
            elements[Osh]="0"
        prav=int(elements[2])*1000+int(elements[4])*100+int(elements[5])*10+int(elements[6])
        print(prav, SymbolOshibki[PozS])
    else:
        print("Ошибок нет")