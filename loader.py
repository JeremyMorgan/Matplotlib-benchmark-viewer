import sqlite3

# Open the database
try:
    conn = sqlite3.connect('stats.db')
    cursor = conn.cursor()
except sqlite3.Error as e:
    # If things go wrong
    print("Error connecting to the database:", e)

# start m1-vs-m2-cpu.csv
# create the table
try:
    # Create the table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS m1vsm2cpu (
            machine TEXT UNIQUE,
            singlecore INT,
            multicore INT
        )
    ''')
    conn.commit()
except sqlite3.Error as e:
    print("Error creating table:", e)
# insert the data
try:
    # Insert data from the CSV file into the table
    with open('csv/m1-vs-m2-cpu.csv', 'r') as file:
        # Skip the first line (header)
        next(file)

        # Insert each row of data into the database if it does not already exist
        for line in file:
            machine, singlecore, multicore = line.strip().split(',')
            cursor.execute('''
                INSERT OR IGNORE INTO m1vsm2cpu (machine, singlecore, multicore)
                VALUES (?, ?, ?)
            ''', (machine, int(singlecore), int(multicore)))

    conn.commit()
except sqlite3.Error as e:
    print("Error inserting data into the database:", e)
# end m1-vs-m2-cpu.csv

# start m1-vs-m2-compute.csv
# create the table
try:
    # Create the table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS m1vsm2compute (
            machine TEXT UNIQUE,
            computescore INT
        )
    ''')
    conn.commit()
except sqlite3.Error as e:
    print("Error creating table:", e)
# insert the data
try:
    # Insert data from the CSV file into the table
    with open('csv/m1-vs-m2-compute.csv', 'r') as file:
        # Skip the first line (header)
        next(file)

        # Insert each row of data into the database if it does not already exist
        for line in file:
            machine, computescore = line.strip().split(',')
            cursor.execute('''
                INSERT OR IGNORE INTO m1vsm2compute (machine, computescore)
                VALUES (?, ?)
            ''', (machine, int(computescore)))

    conn.commit()
except sqlite3.Error as e:
    print("Error inserting data into the database:", e)
# end m1-vs-m2-compute.csv

# start all-geekbench-cpu.csv
# create the table
try:
    # Create the table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS allgeekbenchcpu (
            machine TEXT UNIQUE,
            singlecore INT,
            multicore INT
        )
    ''')
    conn.commit()
except sqlite3.Error as e:
    print("Error creating table:", e)
# insert the data
try:
    # Insert data from the CSV file into the table
    with open('csv/all-geekbench-cpu.csv', 'r') as file:
        # Skip the first line (header)
        next(file)

        # Insert each row of data into the database if it does not already exist
        for line in file:
            machine, singlecore, multicore = line.strip().split(',')
            cursor.execute('''
                INSERT OR IGNORE INTO allgeekbenchcpu (machine, singlecore, multicore)
                VALUES (?, ?, ?)
            ''', (machine, int(singlecore), int(multicore)))

    conn.commit()
except sqlite3.Error as e:
    print("Error inserting data into the database:", e)
# end all-geekbench-cpu.csv

# start all-geekbench-compute.csv
# create the table
try:
    # Create the table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS allgeekbenchcompute (
            machine TEXT UNIQUE,
            computescore INT
        )
    ''')
    conn.commit()
except sqlite3.Error as e:
    print("Error creating table:", e)
# insert the data
try:
    # Insert data from the CSV file into the table
    with open('csv/all-geekbench-compute.csv', 'r') as file:
        # Skip the first line (header)
        next(file)

        # Insert each row of data into the database if it does not already exist
        for line in file:
            machine, computescore = line.strip().split(',')
            cursor.execute('''
                INSERT OR IGNORE INTO allgeekbenchcompute (machine, computescore)
                VALUES (?, ?)
            ''', (machine, int(computescore)))

    conn.commit()
except sqlite3.Error as e:
    print("Error inserting data into the database:", e)
# end all-geekbench-compute.csv

conn.close()
