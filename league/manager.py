from teams import TeamManager
from fixtures import FixtureManager
from standings import StandingsManager
from storage import LeagueStorage
from pathlib import Path

class LeagueManager():
    def __init__(self,file_path):
        self.team_manager = TeamManager()
        self.fixture_manager = FixtureManager()
        self.standings = StandingsManager()
        self.storage = LeagueStorage(file_path)
    def register_team(self,name):
        result = self.team_manager.register_team(name)
        return result
    def generate_fixtures(self):
        teams = self.team_manager.teams

        result = self.team_manager.validate_team_count()

        if result != "number of teams is valid":
            raise ValueError(result)

        return self.fixture_manager.generate_fixtures(teams)
    

file_path = Path("data/league.json")
leaguemanger = LeagueManager(file_path)

leaguemanger.register_team("Arsenal")
leaguemanger.register_team("Chelsea")
leaguemanger.register_team("Man united")
leaguemanger.register_team("Manchester city")
leaguemanger.register_team("Lechester")
leaguemanger.register_team("Wolves")

fixtures = leaguemanger.generate_fixtures()
for fixture in fixtures:
    print(fixture)
