facil = ['a', 'b', 'C', 'd', '3', 'f', 'g', '#', '|', 'j', 'K', '1', '|\/|', 'n', '0',
         '|>', 'Q', 'Я', '$', '7', 'ü', 'v', 'W', 'x', '¥', 'z']

medio = ['@', 'B', '[', '|)', '3', 'ph', '[;', '|-|', '|', 'J', '|{', '1', '|\/|', 'n', '0',
         '|>', 'Q', 'Я', '$', '7', 'ü', 'v', 'W', 'x', '¥', 'z']

dificil = ['4', '|3', '[', '|)', '3', 'ph', '[;', '|-|', '|', 'j', '|{', '1', '|\/|', '|\|', '0',
         '|>', 'Q', 'Я', '$', '7', 'ü', 'v', 'W', 'X', '¥', 'z']

def leFrase():
    s = input("Frase: ")
    return s.upper()

def ascii(letra):
    return ord(letra)-65

def leet(sM, leetId):
    for i in range(len(sM)):
        cod = ascii(sM[i])

        if 0 <= cod <= 25:
            print(leetId[cod], end="")
        else:
            print(sM[i], end="")


# MAIN
sM = leFrase()
print('\n' * 2)
leet(sM, facil)
print('\n' * 2)
leet(sM, medio)
print('\n' * 2)
leet(sM, dificil)





