'''
Дан набор из N долей, представленных в виде N рациональных. 
Необходимо представить эти доли в процентном выражении 
c точностью до трех знаков после запятой.
'''

num = int(input())
sum = float(0)

shares = []

for i in range(num):
    share = float(input())
    shares.append(share)
    sum += share

for i in range(num):
    print(round(shares[i]/sum, 3))

