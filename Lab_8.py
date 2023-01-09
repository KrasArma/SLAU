from datetime import datetime
with open('For_Lab_8.txt', 'r', encoding='utf-8') as file:
    f = file.readlines()
    oll, m = [], []
    b = list(map(int, f[-1].split()))
    for i in f:
        s = i[:len(i)-1]
        oll.append((i[:len(i)-1]).split())
    for i in range(1, len(oll)-2):
        m.append(list(map(int, oll[i])))

def minor(m,shag):
    result = []
    for r in m[1:]:
        row = []
        for j in range(len(r)):
            if j != shag:
                row.append(r[j])
        result.append(row)
    return result

def det(m):
    len_m = len(m)
    if len_m == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    result = 0
    znak = 1
    for i in range(len_m):
        result += znak * m[0][i] * det(minor(m,i))
        znak =-znak
    return result

def kramer(m, svobod):
    m_fix = tuple(m)
    result = []
    for i in range(len(m_fix)):
        m_trans = list(zip(*m))
        m_trans[i] = svobod
        result.append(det(list(zip(*m_trans)))/det(m_fix))
        m = list(m_fix)
    return result
print(kramer(m, b))

def gauss_delenie(A, B, row, num):
    A[row] = [a / num for a in A[row]]
    B[row] /= num

def gauss_rows(m, svobod, row_1, row_2):
    m[row_1], m[row_2] = m[row_2], m[row_1]
    svobod[row_1], svobod[row_2] = svobod[row_2], svobod[row_1]

def gauss_preobrz(A, B, row, ishod_row, koeff):
    A[row] = [(a + k * koeff) for a, k in zip(A[row], A[ishod_row])]
    B[row] += B[ishod_row] * koeff

def Gauss(A, B):
    stolbets = 0
    while (stolbets < len(B)):
        n_row = None
        for r in range(stolbets, len(A)):
            if n_row is None or abs(A[r][stolbets]) > abs(A[n_row][stolbets]):
                 n_row = r
        if n_row is None:
            return "Нет решений"
        if n_row != stolbets:
            gauss_rows(A, B, n_row, stolbets)
        gauss_delenie(A, B, stolbets, A[stolbets][stolbets])
        for r in range(stolbets + 1, len(A)):
            gauss_preobrz(A, B, r, stolbets, -A[r][stolbets])
        stolbets += 1
    itog = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        itog[i] = B[i] - sum(x * a for x, a in zip(itog[(i + 1):], A[i][(i + 1):]))
    return itog

print(Gauss(m, b))

def for_file(itog):
    s = ""
    for i in range(len(itog)):
        s += f'x{str(i+1)} =  {str(round(itog[i], 1))} \n'
    return s

with open('Ansver_Lab_8.txt', 'a', encoding='utf-8') as file:
    file.write(f'Дата вычисления: \n{datetime.now()}\n')
    file.writelines(f)
    file.write('\nРезультат решения по методу Гаусса: \n')
    file.write(for_file(Gauss(m, b)))
    file.write('Результат решения по методу Крамера: \n')
    file.write(for_file(kramer(m, b)))

