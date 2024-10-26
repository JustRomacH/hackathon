import sqlite3

class DataBase:
    def __init__(self):
        self.con = sqlite3.connect("games.db")

def main():
    DataBase()

if __name__ == "__main__":
    main()