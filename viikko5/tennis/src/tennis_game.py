class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.win_condition_lower_limit = 4

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def __get_m_score_by_player_number(self, player_number):
        if player_number == 1:
            return self.m_score1

        return self.m_score2

    def __get_score_word(self, player_number):
        score_words = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

        if player_number == 2 and self.m_score1 == self.m_score2:
            return "All"

        return score_words[self.__get_m_score_by_player_number(player_number)]

    def __get_advantage_win_or_deuce(self):
        score_difference = self.m_score1 - self.m_score2

        if score_difference == 0:
            return "Deuce"

        advantaged_or_winning_player_name = self.player1_name if score_difference > 0 else self.player2_name

        if abs(score_difference) == 1:
            return f"Advantage {advantaged_or_winning_player_name}"

        return f"Win for {advantaged_or_winning_player_name}"

    def get_score(self):
        if self.m_score1 >= self.win_condition_lower_limit or self.m_score2 >= self.win_condition_lower_limit:
            return self.__get_advantage_win_or_deuce()

        return f"{self.__get_score_word(1)}-{self.__get_score_word(2)}"
