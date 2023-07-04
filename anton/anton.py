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
        response = self.league_client.post(
            path="lol-challenges/v1/update-player-preferences/",
            json={"challengeIds": []},
        )

        if response is None or response.status_code != 204:
            print("SOMETHING WENT WRONG")

    def start_league_offline(self) -> None:
        """Starts League of Legends in an offline state

        blabla
        """
