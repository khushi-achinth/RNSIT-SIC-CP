number_of_oranges = int(input())
oranges=[]
input_line = input()

for value in input_line.split():
    oranges.append(int(value))
k = 0

for i in range(number_of_oranges-1):
    if(oranges[i] <= oranges[number_of_oranges-1]):
        oranges[i],oranges[k] = oranges[k],oranges[i]
        k += 1
oranges[number_of_oranges-1], oranges[k] = oranges[k], oranges[number_of_oranges-1]

for orange in oranges:  
    print(orange, end=' ')