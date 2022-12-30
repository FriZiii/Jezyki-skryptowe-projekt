from tabulate import tabulate
from datetime import datetime
import algorithm
from graph import plt

plt.savefig("Raport/plot.png", transparent=True)

path = "raport/raport.html"
file = open(path, 'w',  encoding="utf-8")
html =""

now = datetime.now()
now = now.strftime("%d/%m/%Y %H:%M:%S")

html += (f"<html lang=\"pl\"><head><meta charset=\"utf-8\"><title>Raport z dnia {now}</title><link rel=\"stylesheet\" href=\"style.css\"></head><body>")

html +="<div class = \"container\">"
html +="<div class = \"child\"><div class = \"raport\"><img src =\"plot.png\", alt=\"graph\"></div></div>"

html +=(f"<div class = \"child\">")
html +=(f"<div class = \"raport\"><h1>Raport z dnia {now}</h1></div>")
html += (f"<div class = \"data\"><h2>Wartość wejsciowa: {algorithm.n}</h2>")
html += (f"<h2>Rozpatrywane liczby pierwsze: </h2><h2>{algorithm.primes}</h2>")
html += (f"<h2>Ilość kombinacji dająca wynik {algorithm.n} to: {algorithm.count}</h2>")
html += "</div></div>"

html +="</div>"
for idx, val in enumerate(algorithm.table):
    if(len(val) != 0):
        html +=(f"<h2>Sumy {str(idx+2)} liczb dająca wynik {str(algorithm.n)}</h2>")
        html +=(tabulate(val, tablefmt='html'))
    else:
        html +=(f"<h2>Sumy {str(idx+2)} liczb dająca wynik {str(algorithm.n)}</h2><br>")
        html +=(f"Brak sumy {str(idx+2)} liczb spełniających warunek<br>")

html+=("</body></html>")
file.write(html)
file.close()