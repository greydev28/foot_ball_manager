class StandingsManager:
    def __init__(self):
        self.table = {}
    def initialize_table(self,teams):
        for team in teams:
            self.table[team] = {
                "played": 0,
                "won": 0,
                "drawn": 0,
                "lost": 0,
                "goals_for": 0,
                "goals_against": 0,
                "goal_difference": 0,
                "points": 0
            }
        return self.table
    def update_standings(self, fixture):
        if fixture["status"] != "played":
            return "Fixture has not been played"

        home_team = fixture["home_team"]
        away_team = fixture["away_team"]

        home_score = fixture["home_score"]
        away_score = fixture["away_score"]
        self.table[home_team]["played"] +=1
        self.table[away_team]["played"] +=1
        self.table[home_team]["goals_for"] +=home_score
        self.table[away_team]["goals_for"] += away_score
        self.table[home_team]["goals_against"] += away_score
        self.table[away_team]["goals_against"] += home_score
        return self.table


fixture = {
    "id": "F001",
    "home_team": "Arsenal",
    "away_team": "Chelsea",
    "status": "played",
    "home_score": 2,
    "away_score": 1
}
teams = ["Arsenal", "Chelsea"]
standing_manager = StandingsManager()
standing_manager.initialize_table(teams)
standing_manager.update_standings(fixture)
print(standing_manager.table)