import json
from pathlib import Path
from teams import TeamManager
import re
class LeagueStorage:
    def __init__(self,file_path):
        self.file_path = file_path 
    def save_data(self,teams,fixtures):
        data = {
            "team": teams,
            "fixtures": fixtures
        }
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.file_path,"w",encoding="utf-8") as file:
            json.dump(data,file, indent = 4)
        return "league data save successfully"
    
    def validate_fixtures(self, fixtures, teams):
        for fixture in fixtures:
            required_keys = ["id", "home_team", "away_team", "status"]
            if not isinstance(fixture, dict):
                raise ValueError("Each fixture must be a dictionary")
                
            for key in required_keys:
                if key not in fixture:
                    raise ValueError(f"Fixture is missing {key}")
            if fixture["home_team"] not in teams:
                raise ValueError("Home team is not registered")
            if fixture["away_team"] not in teams:
                raise ValueError("Away team is not registered")
            if fixture["status"] not in ["pending", "played"]:
                 raise ValueError("Invalid fixture status")
               
            if fixture["status"] == "pending":
                print("reached")
                if "home_score" in fixture or "away_score" in fixture:
                    raise ValueError("Pending fixtures cannot have scores")
            if fixture["status"] == "played":
                if "home_score" not in fixture or "away_score" not in fixture:
                    raise ValueError("Played fixtures must have scores")
                home_score = fixture["home_score"]
                away_score = fixture["away_score"]

            if type(home_score) is not int or home_score < 0:
                raise ValueError("Invalid home score")

            if type(away_score) is not int or away_score < 0:
                raise ValueError("Invalid away score")
        return True
    def validate_fixtures_id(self,fixtures):
        fixture_ids = set()
        for fixture in fixtures:
            if fixture["id"] in fixture_ids:
                raise ValueError("Duplicate fixure ID")
            fixture_ids.add(fixture["id"])
            if fixture["home_team"] == fixture["away_team"]:
                raise ValueError("A team cannot play against itself")
            if not re.fullmatch(r"F\d{3}", fixture["id"]):
                raise ValueError("Invalid fixture ID format")
    def validate_fixture_count(self, fixtures, teams):
        expected_count = len(teams) * (len(teams) - 1) // 2
        if expected_count != len(fixtures):
            raise ValueError("Incorrect number of fixtures")
        return True
    def validate_data(self, data):
        if not isinstance(data, dict):
            raise ValueError("League data must be a dictionary")

        if "teams" not in data:
            raise ValueError("Teams data is missing")

        if "fixtures" not in data:
            raise ValueError("Fixtures data is missing")

        if not isinstance(data["teams"], list):
            raise ValueError("Teams must be stored as a list")

        if not isinstance(data["fixtures"], list):
            raise ValueError("Fixtures must be stored as a list")

        # Create a fresh TeamManager
        teammanager = TeamManager()

        # Validate each team
        for team in data["teams"]:
            result = teammanager.register_team(team)

            if isinstance(result, str):
                raise ValueError(result)

        # Validate the number of teams
        result = teammanager.validate_team_count()

        if result != "number of teams is valid":
            raise ValueError(result)
          # Validate fixtures
        self.validate_fixtures(data["fixtures"],data["teams"])

        # Validate total fixture count
        self.validate_fixture_count(data["fixtures"], data["teams"])

        return True
            
    def load_data(self):
        try:
            with open(self.file_path,"r", encoding = "utf-8") as file:
                data = json.load(file)
                self.validate_data(data)
                return data
           
        except FileNotFoundError as error:
                raise RuntimeError("file not found!") from error
        except json.JSONDecodeError as error:
                raise RuntimeError("json corrupt") from error

file_path = Path("data/league.json")
leaguestorage = LeagueStorage(file_path)
teams = ["Arsenal", "Chelsea", "Madrid", "Barcelona"]

fixtures = [
    {"id": "F001", "home_team": "Arsenal", "away_team": "Chelsea", "status": "pending", "home_score": 0, "away_score": 0},
    {"id": "F002", "home_team": "Arsenal", "away_team": "Madrid", "status": "pending", "home_score": 0, "away_score": 0},
    {"id": "F003", "home_team": "Arsenal", "away_team": "Barcelona", "status": "pending", "home_score": 0, "away_score": 0},
    {"id": "F004", "home_team": "Chelsea", "away_team": "Madrid", "status": "pending", "home_score": 0, "away_score": 0},
    {"id": "F005", "home_team": "Chelsea", "away_team": "Barcelona", "status": "pending", "home_score": 0, "away_score": 0},
    {"id": "F006", "home_team": "Madrid", "away_team": "Barcelona", "status": "pending", "home_score": 0, "away_score": 0}
]

fixtures[0]["home_score"] = 2

data = {
    "teams": teams,
    "fixtures": fixtures
}



try: 
    result = leaguestorage.validate_data(data)
except ValueError as err:
    print(err)
else:
    print(result)