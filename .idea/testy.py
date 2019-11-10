import sqlite3


conn = sqlite3.connect('dane_m.db')
#conn.row_factory = sqlite3.Row
kursor =conn.cursor()
kursor.execute("SELECT name FROM sqlite_master WHERE type='table'ORDER BY name;")

#wybierz = "SELECT  * FROM table_branch"
#kursor.execute(wybierz)
wynik = kursor.fetchall()
lista_tabel = []
n=0
for row in wynik:
    ciag1 = ""
    ciag1 = row[0]
#    print(row[0])
#    print(ciag1[0:6])
    if ciag1[0:6]=="branch":
#        print(ciag1[6])
        lista_tabel.append(ciag1[6])
#        print(lista_tabel[n])
    n=n+1


kursor.execute("SELECT id_table FROM table_branch")
wynik = list(kursor.fetchall())
if len(wynik)==len(lista_tabel):print("Sukcess branch: długość tabeli = ilości tabel")
for w in range(len(wynik)):
    for m in lista_tabel:
        if (wynik[w])[0] == int(m):
            print("sukces branch zgodna tabela " + str(m))

print("koniec testu branch --------------------")

conn.commit()

