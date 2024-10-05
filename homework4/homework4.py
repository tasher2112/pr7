x = ""

def transfer(i):
    global x
    if i == 0:
        return 0
    else:
        transfer(i // 13)
        g = i % 13
        if g < 10:
            x += str(g)
        else:
            if i % 13 == 10:   
                x += str("A")
            elif i % 13 == 11:
                x += str("B")
            else:
                x += str("C")
transfer(int(input("Введите цифру: ")))
print("Результат перевода в тринадцатеричную систему: ", x)
