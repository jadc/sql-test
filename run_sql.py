import sqlite3, sys, os.path

# Feel free to modify the code in this function.
def sandbox(db):
    #ex(db, "INSERT INTO musicPerson VALUES (1600, 'Lil Uzi Vert', 1928)")
    #ex(db, "INSERT INTO musicPerson VALUES (2900, 'Playboi Carti', 1995)")
    #ex(db, "INSERT INTO singer VALUES (2900)")
    ex(db, "INSERT INTO music VALUES ('my song', 2020, 60)")
    ex(db, "INSERT INTO music VALUES ('new song', 2021, 65)")
    #ex(db, "INSERT INTO singerOf VALUES (2900, 'rapper', 'my song', 2020)")
    #ex(db, "DELETE FROM musicPerson WHERE pid = 2900")
    ex(db, "INSERT INTO genres VALUES ('rock', 'my song', 2020)")
    ex(db, "INSERT INTO genres VALUES ('rck', 'my song', 2020)")
    preview(db, 'music')
    preview(db, 'genres')

def ex(db, query):
    query = ' '.join(query.split())
    try: return db.execute( query )
    except Exception as e: print(f"!!! Error in: '{query}'\n--> {e.__class__.__name__}: {e}"); exit(1);

def preview(db, table):
    print( table, ex(db, 'SELECT * FROM ' + table ).fetchall() )

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            db = sqlite3.connect(":memory:")
            db = db.cursor()
            db.execute('PRAGMA foreign_keys=ON')

            with open(sys.argv[1], 'r') as sql_file:
                db.executescript(sql_file.read())

            print(f"Created new database from '{sys.argv[1]}'")

            sandbox(db)
        except FileNotFoundError as e:
            print(f"{sys.argv[0]}: cannot access '{sys.argv[1]}': No such file")
            exit(1)
    else:
        print(f"Usage: python {sys.argv[0]} <*.sql>")
        exit(1)

