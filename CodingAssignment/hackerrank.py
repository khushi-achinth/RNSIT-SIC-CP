arrangements = []
def arrange(boys, girls):
    res = boys + girls
    res.sort()
    flag = 0
    for i in range(len(res)-1):
        if ((res[i] in boys and res[i] not in girls) and (res[i+1] in boys and res[i+1] not in girls)) or ((res[i] in girls and res[i] not in boys) and (res[i+1] in girls and res[i+1] not in boys)):
            flag = flag + 1
            break
    arrangements.append('YES') if flag == 0 else arrangements.append('NO')
    
n = int(input())
for _ in range(n):
    number_of_boys_and_girls = int(input())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    arrange(boys, girls)

for a in arrangements:
    print(a)
