num1 = int(input('Enter the beginning of the range:'))
num2 = int(input('Enter the end of the range:'))
even_number = []
odd_number = []
multiple_of_9 = []

for n in list(range(num1, num2+1)):
    if n % 9 == 0:
        multiple_of_9.append(n)
        n = int(n)
        len_9 = len(multiple_of_9)
        summ_9 = sum(multiple_of_9)
        arithmetic_mean_9 = summ_9 / len_9
    if n % 2 == 0:
        even_number.append(n)
        n = int(n)
        len_even = len(even_number)
        summ_even = sum(even_number)
        arithmetic_mean_even = summ_even / len_even
    if n % 2 != 0:
        odd_number.append(n)
        n = int(n)
        len_odd = len(odd_number)
        summ_odd = sum(odd_number)
        arithmetic_mean_odd = summ_odd / len_odd

print (f"Sum of even ones: {summ_even}, sum of odd ones: {summ_odd}, sum of multiples of 9: {summ_9}.\n The arithmetic mean of even numbers:{arithmetic_mean_even}, the arithmetic mean of odd numbers:{arithmetic_mean_odd}, the arithmetic mean of the multiples of 9:{arithmetic_mean_9}" )