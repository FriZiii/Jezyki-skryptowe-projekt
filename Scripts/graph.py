import matplotlib.pyplot as plt
from algorithm import table, n

amount = []
name = []
for i in table:
    amount.append(len(i))

for i in range(len(table)):
    name.append(i+2)

    plt.bar(name, amount)
    plt.xlabel("N")
    plt.ylabel("ILOŚĆ KOMBINACJI")
    plt.title(f"LICZBA KOMBINACJI N LICZB PIERWSZYCH DAJĄCA WYNIK {n}")