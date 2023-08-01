# a context manager for file handling that automatically opens and closes a file.


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# Example usage:
with FileManager("myFile.txt", "w") as file:
    file.write("My name is Julius Kazibwe!")


# multithreading and multiprocessing  that allows us to run the function for different amounts of time.

import time
import threading
import multiprocessing


def long_running_function(duration):
    print(f"Starting function for {duration} seconds")
    time.sleep(duration)
    print(f"Function completed for {duration} seconds")


# Multithreading example
threads = []
for duration in range(1, 6):
    thread = threading.Thread(target=long_running_function, args=(duration,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Multiprocessing example
processes = []
for duration in range(1, 6):
    process = multiprocessing.Process(target=long_running_function, args=(duration,))
    process.start()
    processes.append(process)

for process in processes:
    process.join()


# context manager for managing a database connection.

import sqlite3


class DatabaseManager:
    def __init__(self, database):
        self.database = database
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


# Example usage:
with DatabaseManager("mydb.db") as conn:
    cursor = conn.cursor()

    # Create a table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"""
    )

    # Insert data into the table
    users = [
        (1, "Julius Kazibwe", 24),
        (2, "Mable Faqiha", 23),
        (3, "Ernest Kitiibwa", 28),
    ]
    cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", users)

    # Commit the changes
    conn.commit()

    # Fetch and print the data from the table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
