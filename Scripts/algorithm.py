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

file_input = open("Scripts/INPUT/input.txt", "r")
input = file_input.readline()
n = int(input)
file_input.close()

file_output = open("Scripts/OUTPUT/output.txt", "w")
primes = get_primes(n)
print(primes)
result = sums_up_to(n)
count = len(result)
max = max_num(result)

table = []
for i in range(2, max+1):
    file_output.write(str('-'*16+ f"Suma {str(i)} liczb dajaca wynik {str(n)}" +'-'*16 +"\n"))
    table.append([])
    for r in result:
        if len(r) == i:
            file_output.write(str(r) + "\n")   
            table[i-2].append(r)

file_output.close()