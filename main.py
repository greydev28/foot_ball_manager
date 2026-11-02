from league.teams import  TeamManager

league = TeamManager()

league.register_team("arsenal")

print(league.register_team("arsenal"))


league.register_team("barcelona")
league.register_team("real madrid")

league.register_team("ac millan")

league.register_team("napoli")

league.register_team("lechester")
league.register_team("manchester united")
print(league.validate_team_count())
league.display_teams()