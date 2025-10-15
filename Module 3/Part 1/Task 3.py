start = int(input("Number start:"))
end =  int(input("Number end:"))

for n in list(range(start, end)):
    n = int(n)
    if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)