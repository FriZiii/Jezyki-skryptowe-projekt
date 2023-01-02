import matplotlib.pyplot as plt
from algorithm import table, n

with plt.rc_context({
                    "xtick.color":"white",
                    "ytick.color":"white",
                    "axes.titlecolor":"white",
                    "axes.labelcolor":"white",
                    "axes.edgecolor":"white"
}):
    amount = []
    name = []
    for i in table:
        amount.append(len(i))

    for i in range(len(table)):
        name.append(i+2)

    plt.bar(name, amount, color = "#ee4036")
    plt.xlabel("N")
    plt.ylabel("ILOŚĆ KOMBINACJI")
    plt.title(f"LICZBA KOMBINACJI N LICZB PIERWSZYCH KTÓRYCH SUMA DAJE WYNIK {n}")