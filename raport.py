from tabulate import tabulate

table = [['one','two','three'],['four','five','six'],['seven','eight','nine']]

print(tabulate(table, tablefmt='html'))