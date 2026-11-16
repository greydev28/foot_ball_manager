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
        if home_team not in self.table or away_team not in self.table:
            return "One or both teams are not registered in the standings"
        
        home_score = fixture["home_score"]
        away_score = fixture["away_score"]
        if home_score > away_score:
            print(f'{home_team} wins.')
            self.table[home_team]["won"] += 1
            self.table[home_team]["points"] += 3
            self.table[away_team]["lost"] += 1
        elif away_score > home_score:
            print(f'{away_score} wins.')
            self.table[away_team]["won"] += 1
            self.table[away_team]["points"] += 3
            self.table[home_team]["lost"] += 1

        else:
            print("Draws")
            self.table[home_team]["drawn"] += 1
            self.table[away_team]["drawn"] += 1

            self.table[home_team]["points"] += 1
            self.table[away_team]["points"] += 1
        self.table[home_team]["played"] +=1
        self.table[away_team]["played"] +=1
        self.table[home_team]["goals_for"] +=home_score
        self.table[away_team]["goals_for"] += away_score
        self.table[home_team]["goals_against"] += away_score
        self.table[away_team]["goals_against"] += home_score
        for team in self.table:
            self.table[team]["goal_difference"] = (self.table[team]["goals_for"] - self.table[team]["goals_against"]) 
        return self.table
    def get_sorted_standings(self):
        sorted_table = sorted(
            self.table.items(),
            key=lambda item: (
                -item[1]["points"],
                -item[1]["goal_difference"],
                -item[1]["goals_for"],
                item[0].lower()
            )
        )
        return sorted_table
    def display_standings(self):
        sorted_table = self.get_sorted_standings()

        print("\nLEAGUE TABLE")
        print("-" * 85)

        print(
            f"{'Team':<15}"
            f"{'P':<5}"
            f"{'W':<5}"
            f"{'D':<5}"
            f"{'L':<5}"
            f"{'GF':<5}"
            f"{'GA':<5}"
            f"{'GD':<5}"
            f"{'Pts':<5}"
        )

        print("-" * 85)

        for team, stats in sorted_table:
            print(
                f"{team:<15}"
                f"{stats['played']:<5}"
                f"{stats['won']:<5}"
                f"{stats['drawn']:<5}"
                f"{stats['lost']:<5}"
                f"{stats['goals_for']:<5}"
                f"{stats['goals_against']:<5}"
                f"{stats['goal_difference']:<5}"
                f"{stats['points']:<5}"
            )

        print("-" * 85)
    def get_champion(self, fixtures):
        for fixture in fixtures:
            if fixture["status"] != "played":
                return "League is still in progress"

        sorted_table = self.get_sorted_standings()

        if not sorted_table:
            return "No teams registered"

        champion = sorted_table[0][0]

        return f"The champion is {champion}!"
    def reset_standings(self, teams):
        self.table.clear()
        self.initialize_table(teams)

        return self.table

