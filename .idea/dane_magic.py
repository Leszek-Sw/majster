import sqlite3


def dodaj_dane(id_tabeli):
    kursor.execute("INSERT INTO 'branch" + id_tabeli + "' VALUES( Null ,'rura 1c', '' , 29.5 ,'mb')")


def new_table_branch(nazwa_tabeli):
    kursor.execute("INSERT INTO table_branch VALUES( Null,'" + nazwa_tabeli + "')")
    kursor.execute('CREATE TABLE IF NOT EXISTS "branch' + str(seek_id_table_branch(nazwa_tabeli)) + '" (id_item INTEGER PRIMARY KEY AUTOINCREMENT,nazwa,kod,cena REAL,jm)')


def drop_table_branch(id_tabeli):
    kursor.execute("DROP TABLE branch" + str(id_tabeli))
    kursor.execute("DELETE FROM table_branch where id_table =" + str(id_tabeli))


def seek_id_table_branch(nazwa):
    kursor.execute("SELECT id_table FROM table_branch WHERE nazwa='" + nazwa + "'")
    w_temp = kursor.fetchall()
    return (w_temp[0])['id_table']

def new_table_project(nazwa_project):
    kursor.execute("INSERT INTO table_project VALUES( Null,'" + nazwa_project + "')")
    kursor.execute('CREATE TABLE IF NOT EXISTS "projec' + str(seek_id_table_project(nazwa_project)) + '" (id_item_use INTEGER PRIMARY KEY AUTOINCREMENT, id_item INTEGER, quantity REAL, line )')


def drop_table_project(id_tabeli ):
    kursor.execute("DROP TABLE projec" + str(id_tabeli))
    kursor.execute("DELETE FROM table_project where id_project =" + str(id_tabeli))


def seek_id_table_project(nazwa):
    kursor.execute("SELECT id_project FROM table_project WHERE project='" + nazwa + "'")
    w_temp = kursor.fetchall()
    return (w_temp[0])['id_project']


conn = sqlite3.connect('dane_m.db')
conn.row_factory = sqlite3.Row
kursor =conn.cursor()
#kursor.execute('DROP TABLE lista_rury')
#new_table_project("Nakło")
#dodaj_dane()
#select_tabele("table_branch")
#new_table_branch('zawory')
#drop_table_branch(seek_id_table_branch('zawory'))
drop_table_project(seek_id_table_project('Nakło'))

wybierz = "SELECT  * FROM table_project"
kursor.execute(wybierz)
wynik = kursor.fetchall()

for row in wynik:
#    print(row['id_table'], row['nazwa'])
    print(row['id_project'], row['project'])
conn.commit()

