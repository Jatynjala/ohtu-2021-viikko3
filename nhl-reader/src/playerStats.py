from player import Player
from playerReader import PlayerReader

def by_goals_and_assists(item:Player):
    return item.goals+item.assists

class PlayerStats:
    def __init__(self, reader:PlayerReader):
        self.reader = reader
    def top_scores_by_nationality(self, nationality:str):
        filtered_list = [item for item in self.reader.jsonlist if item.nationality==nationality]
        filtered_list.sort(key=by_goals_and_assists, reverse=True)
        return filtered_list