import time

def check_prime(n):
    for i in range(2, int(n/2)+1):
        if (n%i) ==0:
            return None
    else:
        return n

def get_primes(a, b):
    collection = []
    for num in range (a, b):
        if check_prime(num) == None:
            continue
        else:
            collection.append(check_prime(num))
    return collection

def different(args):
    collection = []
    for i in args:
        if i not in collection:
             collection.append(i)
        else:
            return None
    return collection

def sum(numbers):
    numbers = different(numbers)
    sum_of_num = 0
    if numbers != None:
        COUNT = len(numbers)  
        for n in range(0, COUNT):
            sum_of_num +=numbers[n]
    
    if sum_of_num == 100:
        return sorted(numbers)

def add_numb(arg, collection):
    n_sum = sum(arg)
    if n_sum != None:
        if n_sum not in collection:
            collection.append(n_sum)
    
    return collection

def sum_is_small(numbers):
    sum_of_num = 0
    for n in numbers:
        sum_of_num += n
    if sum_of_num > 100:
        return False
    else:
        return True

def get_num(primes):
    num = [[], [], [], [], [], [], [], []]

    b_primes = primes[1:]
    c_primes = primes[2:]
    d_primes = primes[3:]
    e_primes = primes[4:]
    f_primes = primes[5:]
    g_primes = primes[6:]
    h_primes = primes[7:]
    i_primes = primes[8:]
    for a in primes:
        for b in b_primes:
            num[0] = add_numb([a, b], num[0])
            if sum_is_small([a, b]) == True:
                for c in c_primes:
                    num[1] = add_numb([a, b, c], num[1])
                    if sum_is_small([a, b, c]) == True:
                        for d in d_primes:
                            num[2] = add_numb([a, b, c, d], num[2])
                            if sum_is_small([a, b, c, d]) == True:
                                for e in e_primes:
                                    num[3] = add_numb([a, b, c, d, e], num[3])
                                    if sum_is_small([a, b, c, d, e]) == True:
                                        for f in f_primes:
                                            num[4] = add_numb([a, b, c, d, e, f], num[4])
                                            if sum_is_small([a, b, c, d, e, f]) == True:
                                                for g in g_primes:
                                                    num[5] = add_numb([a, b, c, d, e, f, g], num[5])
                                                    if sum_is_small([a, b, c, d, e, f, g]) == True:
                                                        for h in h_primes:
                                                            num[6] = add_numb([a, b, c, d, e, f, g, h], num[6])
                                                            if sum_is_small([a, b, c, d, e, f, g, h]) == True:
                                                                for i in i_primes:
                                                                    num[7] = add_numb([a, b, c, d, e, f, g, h, i], num[7])
                                                            else:
                                                                break
                                                    else:
                                                        break
                                            else:
                                                break
                                    else:
                                        break
                            else:  
                                break           
                    else:
                        break        
            else:
                break      
                
    return num


start_time = time.time()
primes = get_primes(2,101)
file = open('results.txt', 'w')
for i in range(8):
    print(f'Calculation for {i+2} numbers')
    file.write(str(get_num(primes)[i]) + 2*'\n')
file.close()
time = time.time() - start_time
print('-' * 28 + f'{time} seconds' + '-' * 28)