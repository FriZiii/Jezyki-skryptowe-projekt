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

html += f"<html lang=\"pl\"><head><meta charset=\"utf-8\"><title>Raport z dnia {now}</title><link rel=\"stylesheet\" href=\"style.css\"></head><body>"

html +="<div class = \"container\">"
html +="<div class = \"child\"><div class = \"raport\"><img src =\"plot.png\", alt=\"graph\"></div></div>"

html +=(f"<div class = \"child\">")
html +=(f"<div class = \"raport\"><h1>Raport z dnia {now}</h1></div>")
html += (f"<div class = \"data\"><h2>Wartość wejsciowa</h2><h2 class = \"text-data\">{algorithm.n}</h2>")
html += (f"<h2>Rozpatrywane liczby pierwsze: </h2><h2 class = \"text-data\">{algorithm.primes}</h2>")
html += (f"<h2>Ilość kombinacji licz pierwszych, których suma daje wynik {algorithm.n} </h2><h2 class = \"text-data\"> {algorithm.count}</h2>")
html += "</div></div>"

html +="</div>"
html +="<div class = \"container\">"
for idx, val in enumerate(algorithm.table):
    html+= (f"<div class = \"table\">")
    html+=(f"<div class = \"main\">Suma {idx+2} liczb dająca wartość {algorithm.n}</div>")
    if(len(val) == 0):
                html+=(f"<div class = \"no-value\">Brak {idx+2} liczb spełniających warunek </div>")
    for i in val:
        html+=(f"<div class = \"value\">{i}</div>")
    html += "</div>"
html += "</div>"
html+= "<div class = \"footer\"><h2 class = \"name\">"
html+= "<a href = \"https://github.com/FriZiii/Jezyki-skryptowe-projekt\">@Mateusz Sawosz</a></h2>"
html += "</div>"

html+=("</body></html>")
file.write(html)
file.close()