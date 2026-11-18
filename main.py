from pathlib import Path
from league.manager import LeagueManager


def display_menu():
    print("\n========== FOOTBALL LEAGUE MANAGEMENT SYSTEM ==========")
    print("1. Register Team")
    print("2. Display Teams")
    print("3. Generate Fixtures")
    print("4. Display Fixtures")
    print("5. Record Match Result")
    print("6. Display League Standings")
    print("7. Display Champion")
    print("8. Save League")
    print("9. Load League")
    print("0. Exit")
    print("=======================================================")


def main():
    file_path = Path("data/league.json")
    league = LeagueManager(file_path)

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Enter team name: ")
                result = league.register_team(name)
                print(result)

            elif choice == "2":
                league.display_teams()

            elif choice == "3":
                fixtures = league.generate_fixtures()
                league.initialize_standings()
                print(f"{len(fixtures)} fixtures generated successfully.")

            elif choice == "4":
                league.display_fixtures()

            elif choice == "5":
                fixture_id = input("Enter fixture ID: ").strip()

                home_score = int(input("Enter home team score: "))
                away_score = int(input("Enter away team score: "))

                result = league.record_result(
                    fixture_id,
                    home_score,
                    away_score
                )

                print("Match result recorded successfully.")
                print(result)

            elif choice == "6":
                league.display_standings()

            elif choice == "7":
                champion = league.standings_manager.get_champion(
                    league.fixture_manager.fixtures
                )
                print(champion)

            elif choice == "8":
                league.save_league()
                print("League saved successfully.")

            elif choice == "9":
                league.load_league()
                print("League loaded successfully.")

            elif choice == "0":
                print("Thank you for using the Football League Management System.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError as error:
            print(f"Error: {error}")

        except RuntimeError as error:
            print(f"Error: {error}")

        except FileNotFoundError:
            print("No saved league file was found.")

        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()