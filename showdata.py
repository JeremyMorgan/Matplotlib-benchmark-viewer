import sqlite3
import matplotlib.pyplot as plt

# Connect to the database and create a cursor
conn = sqlite3.connect('stats.db')
cursor = conn.cursor()

try:
    # Retrieve data from the m1vsm2cpu table
    cursor.execute('SELECT machine, singlecore, multicore FROM m1vsm2cpu')
    results = cursor.fetchall()

    # Separate the data into three lists: machines, singlecore scores, and multicore scores
    machines = [result[0] for result in results]
    singlecores = [result[1] for result in results]
    multicores = [result[2] for result in results]

    # Plot the singlecore and multicore scores on a bar graph
    fig, ax = plt.subplots()
    x = range(len(machines))
    width = 0.35
    ax.bar([i - width/2 for i in x], singlecores, width, label='Singlecore')
    ax.bar([i + width/2 for i in x], multicores, width, label='Multicore')
    ax.set_xticks(x)
    ax.set_xticklabels(machines)
    ax.set_title('M1 vs M2 CPU Performance')
    ax.set_xlabel('Machine')
    ax.set_ylabel('Score')
    ax.legend()
    plt.show()

    # Retrieve data from the m1vsm2compute table
    cursor.execute('SELECT machine, computescore FROM m1vsm2compute')
    results = cursor.fetchall()

    # Separate the data into two lists: machines and computescores
    machines = [result[0] for result in results]
    computescores = [result[1] for result in results]

    # Create a bar graph of the computescores data
    fig, ax = plt.subplots()
    x = range(len(machines))
    width = 0.35
    ax.bar([i + width/3 for i in x], computescores,
           width, label='Computescore')
    ax.set_xticks(x)
    ax.set_xticklabels(machines)
    ax.set_title('M1 vs M2 Compute Performance')
    ax.set_xlabel('Machine')
    ax.set_ylabel('Score')
    ax.legend()
    plt.show()

# Retrieve data from the allgeekbenchcpu table
    cursor.execute(
        'SELECT machine, singlecore, multicore FROM allgeekbenchcpu')
    results = cursor.fetchall()

    # Separate the data into three lists: machines, singlecores, and multicores
    machines = [result[0] for result in results]
    singlecores = [result[1] for result in results]
    multicores = [result[2] for result in results]

    # Create a bar graph of the singlecores and multicores data
    fig, ax = plt.subplots()
    x = range(len(machines))
    width = 0.35
    ax.bar([i - width/2 for i in x], singlecores, width, label='Singlecore')
    ax.bar([i + width/2 for i in x], multicores, width, label='Multicore')
    ax.set_xticks(x)
    ax.set_xticklabels(machines)
    ax.set_title('Geekbench Performance')
    ax.set_xlabel('Machine')
    ax.set_ylabel('Score')
    ax.legend()
    plt.show()

    # Retrieve data from the allgeekbenchcompute table
    cursor.execute('SELECT machine, computescore FROM allgeekbenchcompute')
    results = cursor.fetchall()

    # Separate the data into two lists: machines and computescores
    machines = [result[0] for result in results]
    computescores = [result[1] for result in results]

    # Create a bar graph of the computescores data
    fig, ax = plt.subplots()
    x = range(len(machines))
    width = 0.35
    ax.bar([i - width/2 for i in x], computescores,
           width, label='Computescore')
    ax.set_xticks(x)
    ax.set_xticklabels(machines)
    ax.set_title('Geekbench Compute Performance')
    ax.set_xlabel('Machine')
    ax.set_ylabel('Score')
    ax.legend()
    plt.show()

except sqlite3.Error as e:
    print("Error retrieving data from the database:", e)


# Close the database connection
conn.close()
