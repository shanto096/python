def namota (n):
    namotasari =''
    for i in range(1,11):
        namotasari += f'{n} x {i} = {n*i}\n'
    with open(f'table/table{n}.txt','w') as f:
        f.write(namotasari)

for i in range(2,10):
    namota(i)