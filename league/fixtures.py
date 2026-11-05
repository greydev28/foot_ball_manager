
class FixtureManager:
    def __init__(self):
        self.fixtures = []
        self.counter = 1

    def generate_fixtures(self, teams):
        if self.fixtures:
            raise ValueError("Fixtures have already been generated")
        for i in range(len(teams)):
            for j in range(i + 1, len(teams)):
               match_id = f"F{self.counter:03d}"
               fixture = {
                           "id": match_id,
                           "home_team" : teams[i],
                           "away_team" : teams[j],
                           "status": "pending"}
               self.fixtures.append(fixture)
               self.counter += 1
        
        return self.fixtures
    
    def display_fixtures(self):
        if not self.fixtures:
            print("No fixtures have been generated")
            return
        print("\nLEAGUE FIXTURES")
        print("**" * 70)
        for fixture in self.fixtures:
            print(
                f"{fixture["id"]} | "
                f"{fixture["home_team"]} vs {fixture['away_team']} | "
                f"{fixture["status"].upper()}"
               )
    def find_fixture(self, fixture_id):
        for fixture in self.fixtures:
            if fixture_id == fixture["id"]:
                return fixture
        return None  
    
    def record_result(self,fixture_id,home_score,away_score):
        fixture = self.find_fixture(fixture_id)
        if fixture is None:
            return "Fixture not found!"
        if fixture["status"] == "played":
            return "This fixture has already been played"
        if type(home_score) is not int  or home_score < 0:
            return "Invalid home score"
        
        if type(away_score) is not int or  away_score < 0:
            return "Invalid away score"
        fixture["home_score"] = home_score
        fixture["away_score"] = away_score
        fixture["status"] = "played"
        return fixture


teams = ["Arsenal","Barcelona","Chelsea"]
fixture_manager = FixtureManager()
fixture_manager.generate_fixtures(teams)
result = fixture_manager.record_result("F001",23,1)
print(result)



