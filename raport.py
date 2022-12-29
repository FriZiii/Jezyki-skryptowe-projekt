from tabulate import tabulate
from datetime import datetime
import python

file = open('E:/Studia/Jezyki-skryptowe/Projekt/Jezyki-skryptowe-projekt/raport.html', 'w',  encoding="utf-8")
html =""

now = datetime.now()
now = now.strftime("%d/%m/%Y %H:%M:%S")

html += (f"<html lang=\"pl\"><head><meta charset=\"utf-8\"><title>Raport z dnia {now}</title></head><body>")
html +=(f"<h1>Raport z dnia {now}</h1>")
for idx, val in enumerate(python.table):
    if(len(val) != 0):
        html +=(f"<h2>Sumy {str(idx+2)} liczb dająca wynik {str(python.n)}</h2>")
        html +=(tabulate(val, tablefmt='html'))
    else:
        html +=(f"<h2>Sumy {str(idx+2)} liczb dająca wynik {str(python.n)}</h2><br>")
        html +=(f"Brak sum {str(idx+2)} liczb spełniających warunek<br>")

html+=("</body></html>")

file.write(html)
file.close()