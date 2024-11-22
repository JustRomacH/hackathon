import sqlite3

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect(f"./games.db")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    # Возвращает выбранное значение
    def get_value(self, value: str, table: str, cond: str, cond_value: int) -> int:
        req = self.cur.execute(
            f"SELECT {value} FROM {table} WHERE {cond} = {cond_value}"
        )
        return req.fetchone()[0]

    # Возвращает выбранные значения
    def get_values(
            self, value: str, table: str, cond: str = None, cond_value: int = None, order: str = None, reverse: bool = False
    ) -> list[list[int]]:
        req = f"SELECT {value} FROM {table} "
        if cond:
            req += f"WHERE {cond} = {cond_value} "
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
-- Таблица команд
CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT NOT NULL,
    city TEXT NOT NULL,
    year_formed INTEGER
);

-- Таблица участников
CREATE TABLE participants (
    participant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица игр
CREATE TABLE games (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_date DATE NOT NULL,
    location TEXT NOT NULL
);

-- Таблица результатов
CREATE TABLE results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER,
    team_id INTEGER,
    score INTEGER,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица судей
CREATE TABLE judges (
    judge_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    experience_years INTEGER
);

-- Таблица оценок
CREATE TABLE scores (
    score_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER,
    judge_id INTEGER,
    team_id INTEGER,
    score INTEGER,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (judge_id) REFERENCES judges(judge_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица сезонов
CREATE TABLE seasons (
    season_id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    champion_team_id INTEGER,
    FOREIGN KEY (champion_team_id) REFERENCES teams(team_id)
);

-- Таблица наград
CREATE TABLE awards (
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    award_name TEXT NOT NULL,
    season_id INTEGER,
    FOREIGN KEY (season_id) REFERENCES seasons(season_id)
);

-- Таблица матчей
CREATE TABLE matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER,
    team1_id INTEGER,
    team2_id INTEGER,
    winner_team_id INTEGER,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (team1_id) REFERENCES teams(team_id),
    FOREIGN KEY (team2_id) REFERENCES teams(team_id),
    FOREIGN KEY (winner_team_id) REFERENCES teams(team_id)
);

-- Таблица статистики команд
CREATE TABLE team_statistics (
    stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER,
    total_games INTEGER DEFAULT 0,
    total_wins INTEGER DEFAULT 0,
    total_losses INTEGER DEFAULT 0,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Таблица истории команд
CREATE TABLE team_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER,
    event_date DATE NOT NULL,
    event_description TEXT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- Включаем поддержку внешних ключей
PRAGMA foreign_keys = ON;

-- Заполнение таблицы команд
INSERT INTO teams (team_name, city, year_formed) VALUES
('Буревестники', 'Москва', 2005),
('Северный Ветер', 'Санкт-Петербург', 2010),
('Заря', 'Новосибирск', 2007),
('Стрела', 'Казань', 2012),
('Метеор', 'Екатеринбург', 2008),
('Соколы', 'Владивосток', 2009),
('Торнадо', 'Красноярск', 2011),
('Волна', 'Сочи', 2014);

-- Заполнение таблицы участников
INSERT INTO participants (name, age, team_id) VALUES
('Антон Смирнов', 25, 1),
('Дмитрий Полевой', 27, 1),
('Сергей Гордеев', 24, 1),
('Виталий Котов', 26, 1),
('Алексей Брагин', 23, 1),
('Евгений Пушкин', 25, 1),

('Максим Логинов', 28, 2),
('Олег Тихонов', 30, 2),
('Павел Иванченко', 26, 2),
('Игорь Буров', 29, 2),
('Станислав Жуков', 27, 2),
('Никита Крылов', 28, 2),

('Артем Васильев', 23, 3),
('Владислав Климов', 24, 3),
('Роман Орлов', 22, 3),
('Константин Седов', 25, 3),
('Илья Цветков', 23, 3),
('Григорий Ларионов', 22, 3),

('Виктор Белов', 27, 4),
('Николай Кузнецов', 28, 4),
('Андрей Титов', 25, 4),
('Евгений Фомин', 29, 4),
('Леонид Юрьев', 26, 4),
('Александр Шаров', 28, 4),

('Георгий Серов', 24, 5),
('Анатолий Платонов', 23, 5),
('Данила Савельев', 25, 5),
('Семен Ермаков', 26, 5),
('Игорь Овчинников', 24, 5),
('Петр Сафонов', 27, 5),

('Степан Лебедев', 28, 6),
('Кирилл Носов', 29, 6),
('Егор Громов', 27, 6),
('Матвей Воронов', 30, 6),
('Денис Калинин', 29, 6),
('Руслан Тарасов', 28, 6),

('Артур Ковалев', 26, 7),
('Даниил Черкасов', 25, 7),
('Борис Соколов', 27, 7),
('Федор Никитин', 24, 7),
('Геннадий Мальцев', 28, 7),
('Илья Ефимов', 25, 7),

('Александр Лихачев', 24, 8),
('Владимир Зверев', 25, 8),
('Юрий Сизов', 27, 8),
('Кирилл Гаврилов', 26, 8),
('Михаил Зайцев', 24, 8),
('Денис Буров', 25, 8);

-- Заполнение таблицы игр
INSERT INTO games (game_date, location) VALUES
('2024-01-15', 'Москва'),
('2024-02-20', 'Санкт-Петербург'),
('2024-03-10', 'Новосибирск'),
('2024-03-25', 'Казань'),
('2024-04-15', 'Екатеринбург'),
('2024-05-10', 'Владивосток'),
('2024-06-01', 'Красноярск'),
('2024-06-20', 'Сочи'),
('2024-07-15', 'Москва'),
('2024-08-10', 'Санкт-Петербург'),
('2024-09-05', 'Новосибирск'),
('2024-10-01', 'Казань'),
('2024-10-25', 'Екатеринбург'),
('2024-11-15', 'Владивосток'),
('2024-12-01', 'Красноярск'),
('2024-12-20', 'Сочи');

-- Заполнение таблицы результатов
INSERT INTO results (game_id, team_id, score) VALUES
(1, 1, 12), (1, 2, 10),
(2, 3, 14), (2, 4, 8),
(3, 5, 16), (3, 6, 15),
(4, 7, 20), (4, 8, 12),
(5, 1, 14), (5, 5, 18),
(6, 2, 12), (6, 6, 13),
(7, 3, 17), (7, 7, 19),
(8, 4, 11), (8, 8, 16),
(9, 1, 12), (9, 3, 15),
(10, 2, 14), (10, 4, 9),
(11, 5, 20), (11, 7, 21),
(12, 6, 14), (12, 8, 15),
(13, 1, 18), (13, 8, 16),
(14, 2, 19), (14, 7, 20),
(15, 3, 21), (15, 6, 22),
(16, 4, 11), (16, 5, 17);

-- Заполнение таблицы судей
INSERT INTO judges (name, experience_years) VALUES
('Игорь Васильев', 15),
('Марина Зуева', 12),
('Петр Савельев', 10),
('Наталья Соколова', 8),
('Василий Романов', 6);

INSERT INTO scores (game_id, judge_id, team_id, score) VALUES
(1, 1, 1, 8), (1, 1, 2, 7),
(2, 2, 3, 9), (2, 2, 4, 6),
(3, 3, 5, 10), (3, 3, 6, 9),
(4, 4, 7, 9), (4, 4, 8, 6),
(5, 5, 1, 7), (5, 5, 5, 8),
(6, 1, 2, 8), (6, 1, 6, 9),
(7, 2, 3, 10), (7, 2, 7, 11),
(8, 3, 4, 6), (8, 3, 8, 8),
(9, 4, 1, 9), (9, 4, 3, 10),
(10, 5, 2, 8), (10, 5, 4, 5),
(11, 1, 5, 11), (11, 1, 7, 12),
(12, 2, 6, 8), (12, 2, 8, 9),
(13, 3, 1, 9), (13, 3, 8, 8),
(14, 4, 2, 10), (14, 4, 7, 11),
(15, 5, 3, 11), (15, 5, 6, 12),
(16, 1, 4, 7), (16, 1, 5, 9);

INSERT INTO seasons (year, champion_team_id) VALUES
(2015, 1),
(2016, 2),
(2017, 3),
(2018, 5),
(2019, 7),
(2020, 6),
(2021, 8),
(2022, 7),
(2023, 5),
(2024, 1);

INSERT INTO awards (award_name, season_id) VALUES
('Лучший игрок сезона', 1),
('Самая результативная команда', 2),
('Приз зрительских симпатий', 3),
('Чемпионы турнира', 4),
('Прорыв года', 5),
('Лучший тренер', 6),
('Лучший игрок сезона', 7),
('Самая результативная команда', 8),
('Приз зрительских симпатий', 9),
('Чемпионы турнира', 10);

INSERT INTO matches (game_id, team1_id, team2_id, winner_team_id) VALUES
(1, 1, 2, 1),
(2, 3, 4, 3),
(3, 5, 6, 5),
(4, 7, 8, 7),
(5, 1, 5, 5),
(6, 2, 6, 6),
(7, 3, 7, 7),
(8, 4, 8, 8),
(9, 1, 3, 3),
(10, 2, 4, 2),
(11, 5, 7, 7),
(12, 6, 8, 8),
(13, 1, 8, 1),
(14, 2, 7, 7),
(15, 3, 6, 6),
(16, 4, 5, 5);

INSERT INTO team_statistics (team_id, total_games, total_wins, total_losses) VALUES
(1, 10, 6, 4),
(2, 10, 5, 5),
(3, 10, 7, 3),
(4, 10, 3, 7),
(5, 10, 8, 2),
(6, 10, 6, 4),
(7, 10, 7, 3),
(8, 10, 5, 5);

INSERT INTO team_history (team_id, event_date, event_description) VALUES
(1, '2015-06-01', 'Команда "Буревестники" стала чемпионом турнира.'),
(2, '2016-06-01', 'Команда "Северный Ветер" выиграла региональный кубок.'),
(3, '2017-06-01', 'Команда "Заря" обновила состав игроков.'),
(4, '2018-06-01', 'Команда "Стрела" участвовала в международных соревнованиях.'),
(5, '2019-06-01', 'Команда "Метеор" выиграла национальный чемпионат.'),
(6, '2020-06-01', 'Команда "Соколы" получила приз зрительских симпатий.'),
(7, '2021-06-01', 'Команда "Торнадо" выиграла международный кубок.'),
(8, '2022-06-01', 'Команда "Волна" завершила сезон на первом месте.');

""")

if __name__ == "__main__":
    main()