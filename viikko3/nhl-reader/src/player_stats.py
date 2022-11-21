class PlayerStats:
    def __init__(self, player_reader):
        self._player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = self._player_reader.get_players()
        return list(sorted(filter(lambda player: player.nationality == nationality, players), reverse=True, key=lambda player: player.get_score()))

