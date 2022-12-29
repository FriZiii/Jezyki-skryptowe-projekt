import time

def check_prime(n):
    for i in range(2, n):
        if (n%i) ==0:
            return None
    else:
        return n

def get_primes(a):
    collection = []
    for num in range (2, a):
        if check_prime(num) == None:
            continue
        else:
            collection.append(check_prime(num))
    return collection

def sums_up_to(start):
    result = []
    def helper(current, pool, route):
        if current < 0:
            return
        if current == 0:
            result.append(route)
        for idx, val in enumerate(pool):
            helper(current - val, pool[idx+1:], [*route, val])
    helper(start, primes, [])
    return result

def max_num(result):
    max = 0
    for i in result:
        if len(i) > max:
            max = len(i)
    return max

#file = open('E:/Studia/Jezyki-skryptowe/Projekt/Jezyki-skryptowe-projekt/results.txt', 'w')

#file.write("Zadanie 4 - \"Liczby Pierwsze\", Algorytmion 2012  \n")
#file.write("Program wyznacza wszystkie sumy roznych liczb pierwszych rowne n \n\n" )

n = int(input("Podaj n: "))
primes = get_primes(n)

#file.write(f"Rozpatrywane liczby pierwsze dla n = {n} to ")
#file.write(str(primes) + "\n")

result = sums_up_to(n)
max = max_num(result)
#file.write(f"Najwiecej liczb roznych liczb dajacych wynik {n} to {str(max)} \n\n")

table = []
for i in range(2, max+1):
    #file.write(str('-'*16+ f"Suma {str(i)} liczb dajaca wynik {str(n)}" +'-'*16 +"\n"))
    table.append([])
    for r in result:
        if len(r) == i:
            #file.write(str(r) + "\n")   
            table[i-2].append(r)