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
    DataBase().cur.executescript("""
    INSERT INTO teams (team_name, city, year_formed)
VALUES
    ('Молния', 'Москва', 2001),
    ('Соколы', 'Санкт-Петербург', 2003),
    ('Шторм', 'Казань', 2007),
    ('Вихрь', 'Новосибирск', 1999),
    ('Торнадо', 'Екатеринбург', 2010),
    ('Барс', 'Краснодар', 2005),
    ('Метеор', 'Воронеж', 2008),
    ('Гром', 'Ростов-на-Дону', 2012);

INSERT INTO participants (name, age, team_id)
VALUES
    ('Иван Петров', 24, 1),
    ('Анна Смирнова', 22, 1),
    ('Олег Иванов', 28, 2),
    ('Мария Сидорова', 29, 2),
    ('Виктор Волков', 26, 3),
    ('Екатерина Орлова', 23, 3),
    ('Алексей Фёдоров', 30, 4),
    ('Дарья Михайлова', 25, 4),
    ('Павел Ковалев', 27, 5),
    ('Светлана Григорьева', 24, 5),
    ('Николай Самойлов', 31, 6),
    ('Ольга Ефимова', 28, 6),
    ('Роман Соколов', 29, 7),
    ('Ирина Беляева', 26, 7),
    ('Сергей Пономарев', 32, 8),
    ('Алена Жукова', 27, 8);

INSERT INTO games (game_date, location)
VALUES
    ('2023-07-10', 'Стадион "Лужники"'),
    ('2023-08-15', 'Стадион "Газпром Арена"'),
    ('2023-09-12', 'Центральный стадион Казани'),
    ('2023-10-05', 'Стадион "Спартак" в Новосибирске'),
    ('2023-06-25', 'Стадион "Динамо" в Екатеринбурге'),
    ('2023-07-30', 'Стадион "Краснодар Арена"'),
    ('2023-08-18', 'Стадион "Центральный" в Воронеже'),
    ('2023-09-15', 'Стадион "Олимп-2" в Ростове-на-Дону');

INSERT INTO results (game_id, team_id, score)
VALUES
    (1, 1, 15),
    (1, 2, 12),
    (2, 1, 17),
    (2, 3, 14),
    (3, 2, 18),
    (3, 4, 16),
    (4, 3, 13),
    (4, 4, 15),
    (5, 5, 19),
    (5, 6, 15),
    (6, 6, 18),
    (6, 7, 14),
    (7, 7, 20),
    (7, 8, 18),
    (8, 5, 16),
    (8, 8, 15);

INSERT INTO judges (name, experience_years)
VALUES
    ('Александр Кузнецов', 7),
    ('Сергей Васильев', 5),
    ('Людмила Орлова', 6),
    ('Михаил Попов', 10),
    ('Наталья Алексеева', 8),
    ('Игорь Смирнов', 4);

INSERT INTO scores (game_id, judge_id, team_id, score)
VALUES
    (1, 1, 1, 14),
    (1, 2, 2, 11),
    (2, 3, 1, 16),
    (2, 4, 3, 13),
    (3, 1, 2, 17),
    (3, 2, 4, 15),
    (4, 3, 3, 12),
    (4, 4, 4, 14),
    (5, 5, 5, 18),
    (5, 6, 6, 14),
    (6, 1, 6, 17),
    (6, 2, 7, 13),
    (7, 3, 7, 19),
    (7, 4, 8, 17),
    (8, 5, 5, 15),
    (8, 6, 8, 14);

INSERT INTO seasons (year, champion_team_id)
VALUES
    (2023, 2),
    (2022, 4),
    (2021, 1),
    (2020, 6),
    (2019, 5);

INSERT INTO awards (award_name, season_id)
VALUES
    ('Лучший игрок', 1),
    ('Лучший защитник', 2),
    ('Лучший нападающий', 3),
    ('Команда года', 1),
    ('Самая честная игра', 2),
    ('Тренер года', 3);

INSERT INTO matches (game_id, team1_id, team2_id, winner_team_id)
VALUES
    (1, 1, 2, 1),
    (2, 1, 3, 1),
    (3, 2, 4, 2),
    (4, 3, 4, 4),
    (5, 5, 6, 5),
    (6, 6, 7, 6),
    (7, 7, 8, 7),
    (8, 5, 8, 5);

INSERT INTO team_statistics (team_id, total_games, total_wins, total_losses)
VALUES
    (1, 4, 3, 1),
    (2, 4, 2, 2),
    (3, 3, 1, 2),
    (4, 4, 2, 2),
    (5, 4, 3, 1),
    (6, 4, 2, 2),
    (7, 3, 2, 1),
    (8, 3, 1, 2);

INSERT INTO team_history (team_id, event_date, event_description)
VALUES
    (1, '2022-05-15', 'Выиграли региональный чемпионат'),
    (2, '2023-06-18', 'Пришли новые тренеры'),
    (3, '2023-04-10', 'Провели сборы в летнем лагере'),
    (4, '2023-08-05', 'Команда вышла в финал городского турнира'),
    (5, '2022-07-22', 'Приобретен новый инвентарь'),
    (6, '2023-03-14', 'Участие в тренировочных сборах'),
    (7, '2021-11-12', 'Открытие нового тренировочного сезона'),
    (8, '2023-05-27', 'Участие в благотворительном матче');

    """)

if __name__ == "__main__":
    main()