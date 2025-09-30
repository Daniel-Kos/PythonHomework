tariff = {
    'T2':{'T2 other' : 9, "T2 to T2" : 3},
    'Beeline':{'Beeline to Beeline' : 3.21, 'Beeline other': 4.18},
    'MTS':{'MTS to MTS': 6.4, 'MTS other': 10.3}}

call_from = str(input('Enter your operator:'))
call_to = str(input("Enter your interlocutor's operator:"))
price_call = int(input('Enter your price: '))

if call_from in tariff:
    pass
else:
    print('Error')

if call_to in tariff:
    pass
else:
    print('Error')

if call_from == call_to and call_from == 'T2':
    Result = tariff['T2']['T2 to T2'] * price_call
    print(Result)

elif call_from == call_to and call_from == 'MTS':
    Result = tariff['MTS']['MTS to MTS'] * price_call
    print(Result)

elif call_from == call_to and call_from == 'Beeline':
    Result = tariff['Beeline']['Beeline to Beeline'] * price_call
    print(Result)

elif call_from != call_to and call_from == 'T2':
    Result = tariff['T2']['T2 other'] * price_call
    print(Result)

elif call_from != call_to and call_from == 'Beeline':
    Result = tariff['Beeline']['Beeline other'] * price_call
    print(Result)

elif call_from != call_to and call_from == 'MTS':
    Result = tariff['MTS']['MTS other'] * price_call
    print(Result)