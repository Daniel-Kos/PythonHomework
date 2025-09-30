Sales1 = int(input('Enter a Alucard sales: '))
Sales2 = int(input('Enter a Anderson sales: '))
Sales3 = int(input('Enter a Roman sales: '))

managers = {
    'Alucard':{'Sales': Sales1},
    'Anderson':{'Sales': Sales2},
    'Roman':{'Sales': Sales3}}

if Sales1 < 500:
    Salary_Al = Sales1 * 0.03
elif 500 <= Sales1 < 1000:
    Salary_Al = Sales1 * 0.05
elif Sales1 >= 1000:
    Salary_Al = Sales1 * 0.08

if Sales2 < 500:
    Salary_And = Sales2 * 0.03
elif 500 <= Sales2 < 1000:
    Salary_And = Sales2 * 0.05
elif Sales2 >= 1000:
    Salary_And = Sales2 * 0.08

if Sales3 < 500:
    Salary_Rom = Sales3 * 0.03
elif 500 <= Sales3 < 1000:
    Salary_Rom = Sales3 * 0.05
elif Sales3 >= 1000:
    Salary_Rom = Sales3 * 0.08

print(f'Salary Alucard: {Salary_Al+200}',f'Salary Anderson: {Salary_And+200}',f'Salary Roman: {Salary_Rom+200}')

if Sales1 > Sales2 and Sales1>Sales3:
    print('Employee of the Month Alucard')
elif Sales2 > Sales3 and Sales2 > Sales1:
    print('Employee of the Month Anderson')
elif Sales3 > Sales1 and Sales3 > Sales2:
    print('Employee of the Month Roman')