"""Module for league api HACK'ing

"""

class LeagueConnection:
    """A HACK'ed version of `LCA`(League client api)

    Provides riot-access to every `LCA` http/https request

    Attributes:
        base_url (str): the base url for the `LCA` interface
        protocol (str): specification of http or https protocols
        port (str): the port where `LCA` is being hosted on(riot version, normal version is 2999)
        username (str): As of patch 13.12 the username used in auth is a constant value("riot")
        remoting_auth_token (str): Auth key
    
    Example request:
        GET https://127.0.0.1:2999/liveclientdata/allgamedata
    """

    base_url: str
    protocol: str
    port: str
    username: str
    remoting_auth_token: str

    def __init__(self) -> None:
        self.protocol = "https"
        
    def build_url(self, o: object) -> str:
        """.""" 
        return ""

    def get(self, url) -> object:
        """."""

    def post(self, url, key) -> object:
        """."""
