n1 = int(input('Enter a number:'))
n2 = int(input('Enter a number:'))
if n1<n2:
    small=n1
else:
    small=n2

d=2
while d<=small:
    if n1%d==0 and n2%d==0:
        print('L.C.D is ',d)
        break
    d=d+1

else:
    print('There is no LCD:')
