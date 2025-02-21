import sys

def even_place_odd_numbers():
    for i in range(len(sys.argv[1])):
        if i%2 == 0 and int(sys.argv[1][i])%2 != 0:
            print(sys.argv[1][i])

even_place_odd_numbers()

