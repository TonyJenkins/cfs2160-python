from random import randint

def generate_account_number ():

    number = ''

    for d in range (8):
        number += str (randint (0, 10))

    return number

if __name__ == '__main__':

    print (generate_account_number())
