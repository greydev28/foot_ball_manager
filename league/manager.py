from .teams import TeamManager
from .fixtures import FixtureManager
from .standings import StandingsManager
from .storage import LeagueStorage

class LeagueManager():
    def __init__(self,file_path):
        self.team_manager = TeamManager()
        self.fixture_manager = FixtureManager()
        self.standings_manager = StandingsManager()
        self.storage_manager = LeagueStorage(file_path)
    def register_team(self,name):
        result = self.team_manager.register_team(name)
        return result
    def generate_fixtures(self):
        teams = self.team_manager.teams

        result = self.team_manager.validate_team_count()

        if result != "number of teams is valid":
            raise ValueError(result)

        return self.fixture_manager.generate_fixtures(teams)

    def initialize_standings(self):
        teams = self.team_manager.teams
        return self.standings_manager.initialize_table(teams)
    def display_standing(self):
        result = self.standings_manager.display_standings()
        return result
    
    def record_result(self, fixture_id, home_score, away_score):
        fixture = self.fixture_manager.record_result(
            fixture_id,
            home_score,
            away_score
        )

        self.standings_manager.reset_standings(
            self.team_manager.teams
        )

        for match in self.fixture_manager.fixtures:
            if match["status"] == "played":
                self.standings_manager.update_standings(match)

        return fixture
    def display_fixtures(self):
        return self.fixture_manager.display_fixtures()  

    def save_league(self):
        teams = self.team_manager.teams
        fixtures = self.fixture_manager.fixtures

        return self.storage_manager.save_data(teams, fixtures)  

    def load_league(self):
        data = self.storage_manager.load_data()

        self.team_manager.teams = data["teams"]
        self.fixture_manager.fixtures = data["fixtures"]
        
        self.fixture_manager.counter = len(self.fixture_manager.fixtures) + 1

        self.standings_manager.reset_standings(
            self.team_manager.teams
        )

        for fixture in self.fixture_manager.fixtures:
            if fixture["status"] == "played":
                self.standings_manager.update_standings(fixture)

        return data
    def display_teams(self):
        return self.team_manager.display_teams()
        


