import sqlite3

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("lapta/games.db")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    # Возвращает выбранное значение
    def get_value(self, value: str, table: str, cond: str, cond_value: int) -> int:
        req = self.cur.execute(
            f"SELECT {value} FROM {table} WHERE {cond} = {cond_value}"
        )
        return req.fetchone()[0]

    # Возвращает выбранные значения всех юзеров
    def get_values(self, value: str, table: str,  order: str = None, reverse: bool = False) -> list[list[int]]:
        req = f"SELECT {value} FROM {table} "
        # Порядок сортировки
        if order:
            req += f"ORDER BY {order} "
            if reverse:
                req += "DESC"
        return self.cur.execute(req).fetchall()

    # Изменяет выбранное значение
    def update_value(self, table: str, value: str, new_value: str, cond_value: str) -> None:
        self.cur.execute(
            f"UPDATE {table} SET {value} = {new_value} WHERE {cond_value} = {value}"
        )

def main():
    DataBase()

if __name__ == "__main__":
    main()