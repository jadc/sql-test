import sqlite3, sys

def sandbox(db):
    pass  # Feel free to modify the code in this function.

# e.g. ex(db, "INSERT INTO music VALUES ('my song', 2020, 60)")
def ex(db, query):
    query = ' '.join(query.split())
    try: return db.execute( query )
    except Exception as e: print(f"!!! Error in: '{query}'\n--> {e.__class__.__name__}: {e}"); exit(1);

# e.g. preview(db, 'music')
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

