from random import randrange
print("Game doan so")
while True:
    so = randrange(1, 101)
    solandoan = 0
    win = False
    while solandoan < 7:
        solandoan += 1
        songuoi=int(input("May doan 1 den 100, moi ban doan: "))
        if so==songuoi:
            print("Chuc mung ban da doan dung, so may la = ", so)
            win = True
            break
        if so<songuoi:
            print("Ban doan sai, so may < so ban")
        elif so > songuoi:
            print("Ban doan sai, so may > so ban")
        if win == False:
            print("Ban da doan sai, so may la: ", so)
        hoi=input("Ban co muon choi tiep khong? (c/k)")
        if hoi == "k":
            break
    print("Cam on ban da choi game")