"""Module for league api HACK'ing

"""

class LeagueConnection:
    """A HACK'ed version of `LCA`(League client api)

    Provides riot-access to every `LCA` http/https request

    Attributes:
        base_url (str): the base url for the `LCA` interface
    """

    base_url: str

    def __init__(self) -> None:
        """."""
        base_url = ""

    def get(self, url) -> object:
        """."""

    def post(self, url, key) -> object:
        """."""
