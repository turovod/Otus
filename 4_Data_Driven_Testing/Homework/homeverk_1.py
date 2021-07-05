with open('data.txt', 'rb', ) as f:
    data = f.read()

    data = data.decode('utf-8').replace('\r', '').replace('\n', '').replace('\xa0', '') \
        .replace('1', '').replace('0', '')

    ls = data.split(',')

    for item in ls:
        if item == '':
            ls.remove(item)

        if item == '':
            ls.remove(item)

        if item == '':
            ls.remove(item)

    ls = ls[5:]

    ls_pipol_citis = []
    sw: str

for i in range(len(ls) - 1):
    if i % 2 == 0:
        sw = ls[i + 1], ls[i]
        ls_pipol_citis.append(','.join(sw))

for i in range(len(ls_pipol_citis)):
    ls_pipol_citis[i] = ls_pipol_citis[i].replace(',', ' ')
print(ls_pipol_citis)
s = '-+'

gen = (i + ' ' + j + ' ' + k + ' ' + f for i in ls_pipol_citis for j in s for k in s for f in s)

with open('result.txt', 'w', encoding='utf-8') as f:
    for i in range(100):
        f.write(next(gen) + '\n')
