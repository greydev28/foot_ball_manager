import json
from pathlib import Path
class LeagueStorage:
    def __init__(self,file_path):
        self.file_path = file_path 
    def save_data(self,teams,fixtures):
        data = {
            "team": teams,
            "fixtures": fixtures
        }
        with open(self.file_path,"w",encoding="utf-8") as file:
            json.dump(data,file, indent = 4)
        return "league data save successfully"
    def load_data(self):
        try:
           with open(self.file_path,"r", encoding = "utf-8") as file:
              data = json.load(file)
              return data
        except FileNotFoundError as error:
            raise RuntimeError("file not found!") from error
        except json.JSONDecodeError as error:
            raise RuntimeError("json corrupt") from error



file_path = Path("data/league.json")
 