def collatz():
    try:
        numb = int(input('give me a number: '))
        while numb != 1:
            if numb % 2 == 0:
                numb = numb // 2
                print(numb)
            else:
                numb = numb * 3 + 1
                print(numb)
    except ValueError:
        print('not an int but a string !')


collatz()
        