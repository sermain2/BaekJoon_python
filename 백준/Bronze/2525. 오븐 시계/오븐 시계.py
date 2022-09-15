h, m1 = map(int, input().split())
m2 = int(input())

a = (m1 + m2)//60
b = (m1 + m2)%60

if (m1 + m2 >= 60):
    if (h+a >= 24):
        h = h - 24
    h = a + h
    print(h, b)

else:
    if(h >= 24):
        h = h - 24
    print(h, m1+m2)
