class TeamManager:
    def __init__(self):
        self.teams = []
    def register_team(self, name):
        cleaned_name = name.strip()
        normalized_name = cleaned_name.lower()
        if not cleaned_name:
            return "Team name cannot be empty"
        elif any(team.lower() == normalized_name for team in self.teams):
            return f"{cleaned_name} already exists"
        elif len(self.teams) >= 8:
            return "Maximum number of teams reached"
        else:
            self.teams.append(cleaned_name)
            return self.teams
    def validate_team_count(self):
        if len(self.teams) < 4:
            return "team not complete"
        elif len(self.teams) > 8:
            return "teams cannot be more than eight!"
        else:
            return "number of teams is valid"

    def display_teams(self):
        print("\nREGISTERED TEAMS")

        if not self.teams:
            print("No teams registeresd yet.")
            return

        for i, team in enumerate(self.teams, start=1):
            print(f"{i}. {team}")