from pixelsquare import *

def mystery(Dim, First, Second):
    enigma = PixelSquare(Dim)
    for i in range(0,Dim//2):
        print("test")
        num = Dim - 2*i - 1
        if i % 2 == 0:
            PixelSquare.rectangle(enigma, i, i, num, num, First)
            print(i)
            print(num)
        else:
            PixelSquare.rectangle(enigma, i, i, num, num, Second)
            print(i)
            print(num)
        print(enigma)

    return enigma


print(mystery(1,"a","b"))
