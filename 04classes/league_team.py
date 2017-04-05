#!/usr/bin/env python3

# league_team.py
#
# League table class example.
#
# AMJ
# 2017-04-01

from functools import total_ordering

@total_ordering
class TeamRecord:

    def __init__ (self, name):

        self.name = name

        self.__games_won = 0
        self.__games_drawn = 0
        self.__games_lost = 0

        self.__points_for = 0
        self.__points_against = 0

    @property
    def games_played (self):
        return self.__games_won + self.__games_drawn + self.__games_lost

    @property
    def games_won (self):
        return self.__games_won

    @property
    def games_drawn (self):
        return self.__games_drawn

    @property
    def games_lost (self):
        return self.__games_lost

    @property
    def points_for (self):
        return self.__points_for

    @property
    def points_against (self):
        return self.__points_against

    @property
    def points_difference (self):
        return self.points_for - self.points_against

    @property
    def league_points (self):
        return 3 * self.__games_won + self.__games_drawn

    def play_game (self, scored, conceded):
        self.__points_for += scored
        self.__points_against += conceded

        if scored > conceded:
            self.__games_won += 1
        elif conceded > scored:
            self.__games_lost += 1
        else:
            self.__games_drawn += 1

    def __lt__ (self, other):
        return self.league_points < other.league_points

    def __eq__ (self, other):
        return self.league_points == other.league_points

    def __str__ (self):
        return "{:20s} {:2d} {:2d} {:2d} {:2d} {:3d} {:3d} {:-3d} {:2d}" \
            .format (self.name,
                     self.games_played, self.games_won, self.games_drawn, self.games_lost,
                     self.points_for, self.points_against, self.points_difference,
                     self.league_points)

if __name__ == '__main__':

    team_one = TeamRecord ('Huddersfield')
    team_two = TeamRecord ('Wigan')

    team_one.play_game (10, 24)
    team_two.play_game (24, 2)

    league = []
    league.append (team_one)
    league.append (team_two)

    for team in league:
        print (team)

    print ()
    league.sort (reverse = True)

    for team in league:
        print (team)
