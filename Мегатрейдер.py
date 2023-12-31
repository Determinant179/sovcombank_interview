'''
Допустим, что на рынке существует некое множество облигаций с номиналом 1000
условных единиц, по которым каждый день выплачивается купон размером 1 уе.
Погашение номинала облигации (то есть выплата 1000 условных единиц) происходит в
конце срока.
Каждая облигация на рынке характеризуется названием (некая строка) и ценой, цена
выражается в виде процентов от номинала, то есть цена 98.5 соответствует цене
98,5% * 1000 = 985 условных единиц.
У некоего трейдера есть информация о том какие предложения по облигациям будут
на рынке в ближайшие N дней. По каждому дню он знает, какие лоты будут
представлены на бирже: название облигации, цену и количество в штуках. Каждый
день на рынке может быть от 0 до M лотов. Трейдер располагает суммой денежных
средств в количестве S.
Необходимо определить какие лоты в какие дни нужно купить, чтобы получить
максимальный доход с учетом следующих условий:
1. Трейдер может только покупать облигации. Купленные облигации не продаются.
2. Трейдер может купить только весь лот целиком при наличии доступных денежных
средств.
3. Выплаченные купоны по купленным облигациям не реинвестируются, то есть не
увеличивают сумму доступных денежных средств .
4 . Все купленные облигации будут погашены в день N+30.
5 . Доход рассчитывается на день N+30, то есть после погашения облигаций .
'''

def maxProfit(v, w, W):

    n = len(v)
 
    T = [[0 for w in range(W + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if w[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(T[i - 1][j], T[i - 1][j - w[i - 1]] + v[i - 1])

    findPath(n, W, T, w)

    return T[n][W]

profitPath = []

def findPath(i, j, T, w):
    if T[i][j] == 0:
        return
    if T[i - 1][j] == T[i][j]:
        findPath(i - 1, j, T, w)
    else: 
        findPath(i - 1, j - w[i - 1], T, w)
        profitPath.append(i - 1)

N, M, S = input().split()

bonds = []
v = []
w = []
bond = True

while bond:
    bond = input().split()
    if bond:
        bonds.append(bond)

        bondProfit = round(int(bond[3]) * (30 + int(N) - int(bond[0]) - 10 * (float(bond[2]) - 100)))
        bondPrice = round(int(bond[3]) * float(bond[2]) * 10)
        v.append(bondProfit)
        w.append(bondPrice)

res = maxProfit(v, w, int(S))

print(res)
for i in profitPath:
    print(' '.join(bonds[i]))


