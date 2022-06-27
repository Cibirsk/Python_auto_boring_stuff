import string

def all_my_cats():
    cats = []
    while True:
        input_cats = input('name of your cat: ')
        if input_cats == '' :
            break
        else:
            cats.append(input_cats)
    print('The names of the cat are: ')
    for cat in cats:
        print(cat)

all_my_cats()