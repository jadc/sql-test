#!/usr/bin/env python
import sqlite3, sys

args = ['PRAGMA foreign_keys=ON']
if __name__ == '__main__':
    if len(sys.argv) > 1:
        db = sqlite3.connect(":memory:").cursor()
        for arg in args: db.execute(arg)

        # Bulk read first file
        try: 
            with open(sys.argv[1], 'r') as sql_file:
                db.executescript(sql_file.read())
            print(f"Created new database from '{sys.argv[1]}' in memory")
        except FileNotFoundError as e:
            print(f"{sys.argv[0]}: cannot access '{sys.argv[1]}': No such file", file=sys.stderr); 
            exit(1)
        except Exception as e:
            print(f"Failed to interpret '{sys.argv[1]}' as an SQL file\n{e.__class__.__name__}: {e}", file=sys.stderr); 
            exit(1)

        # Read sandboxes
        for file in sys.argv[2:]:
            try:
                with open(file, 'r') as sql_file:
                    queries = [x for x in ' '.join(sql_file.read().split()).split(';') if x]
                    for query in queries:
                        print(f"\n==> '{query}'")
                        cursor = db.execute(query)
                        for row in cursor: print(row)
            except FileNotFoundError as e:
                print(f"{sys.argv[0]}: cannot access '{file}': No such file", file=sys.stderr);
            except Exception as e:
                print(f"Error while reading '{file}'\n{e.__class__.__name__}: {e}", file=sys.stderr);

        exit(0)
    else:
        print(f"Usage: {sys.argv[0]} <*.sql> [*.sql, ...]", file=sys.stderr)
    exit(1)
