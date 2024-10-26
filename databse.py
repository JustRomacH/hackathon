import sqlite3

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("games.db")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()



def main():
    DataBase().cur.execute("""
CREATE TABLE team_history (
    history_id INT AUTO_INCREMENT PRIMARY KEY,
    team_id INT,
    event_date DATE NOT NULL,
    event_description TEXT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

 """)

if __name__ == "__main__":
    main()