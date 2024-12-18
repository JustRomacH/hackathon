from django.shortcuts import render
from .database import DataBase

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def teams(request):
    db = DataBase()
    teams_db = []

    for team in db.get_values("*", "teams"):
        team_id = team[0]
        stats_db = db.get_values(
            "total_games, total_wins, total_losses", "team_statistics", "team_id", team_id
        )
        participants_db = db.get_values(
            "name, age", "participants", "team_id", team_id
        )
        teams_db.append(list(team) + list(stats_db[0]) + list(participants_db))

    return render(
        request, 'main/teams.html',
        {'teams': teams_db}
    )

def matches(request):
    db = DataBase()
    matches_db = []

    for match in db.get_values("*", "matches"):
        game_id = match[1]
        match = list(match)
        team_name1 = db.get_value("team_name", "teams", "team_id", match[2])
        team_name2 = db.get_value("team_name", "teams", "team_id", match[3])
        match[2] = team_name1
        match[3] = team_name2
        match[4] = db.get_value("team_name", "teams", "team_id", match[4])
        games_db = db.get_values("game_date, location", "games", "game_id", game_id)[0]
        scores_db = db.get_values("team_id, score, judge_id", "scores", "game_id", game_id)
        first_team = db.get_value("team_name", "teams", "team_id", scores_db[0][0])
        second_team = db.get_value("team_name", "teams", "team_id", scores_db[1][0])
        judges = []

        for team_score in scores_db:
            judges.append(
                db.get_values(
                    "name, experience_years", "judges", "judge_id", team_score[2])[0]
            )

        matches_db.append(
            list(match)
              + list(games_db)
              + [[first_team, scores_db[0][1], scores_db[0][2]]]
              + [[second_team, scores_db[1][1], scores_db[1][2]]]
              + list(judges)
        )

    return render(request, 'main/matches.html', {"matches": matches_db})

def seasons(request):
    db = DataBase()
    seasons_db = []
    for season in db.get_values("*", "seasons"):
        season_id = season[0]
        year = season[1]
        team_id = season[2]
        team_info = db.get_values(
            "team_name, city", "teams", "team_id", team_id
        )[0]
        team_name = team_info[0]
        team_city = team_info[1]
        seasons_db.append((season_id, year, team_name, team_city))
    return render(
        request, 'main/seasons.html', {"seasons": seasons_db}
    )

def about(request):
    return render(request, 'main/about.html')