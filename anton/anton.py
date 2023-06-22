"""Anton Module

"""

from .league_connection import LeagueConnection

class Anton:
    """Main Anton class

    Anton is a league of legends hack focused around QOL(Quality of life)
    improvements
    """

    league_client: LeagueConnection

    def __init__(self) -> None:
        """."""
        self.league_client = LeagueConnection()

    def remove_challenges(self) -> None:
        """Remove League Challenges

        Remove League of Legends challenges from profile
        using RIOT's `League Client API`
        """
        return