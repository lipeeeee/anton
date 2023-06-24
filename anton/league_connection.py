"""Module for league api HACK'ing

"""

import asyncio
from background_thread import BackgroundThread
from windows_utils import execute_cmd_command


class LeagueConnection:
    """A HACK'ed version of `LCA`(League client api)

    Provides riot-access to every `LCA` http/https request

    Attributes:
        base_url (str): the base url for the `LCA` interface

        protocol (str): specification of http or https protocols

        port (str): the port where `LCA` is
        being hosted on(riot version, normal version is 2999)

        username (str): As of patch 13.12 the username used
        in auth is a constant value("riot")

        remoting_auth_token (str): Auth key

        connected (bool): connected to `LCA` status

    Class Constants:
        LCA_NOT_CONNECTED_OUTPUT (str): Output when trying to hack but
        `LCA` is down

        LCA_NOT_CONNECTED_OUTPUT (str): Output after sucesseful hacked connection

        CMD_HACK (str): The cmd command to get LCA's info

    Data:
    Example request:
        GET https://127.0.0.1:2999/liveclientdata/allgamedata
    Example of no connection to `LCA`:
        "No Instance(s) Available."
    """

    base_url: str
    protocol: str
    port: str
    username: str
    remoting_auth_token: str
    connected: bool

    # Class Constants
    LCA_NOT_CONNECTED_OUTPUT = "No Instance(s) Available"  # starts with
    LCA_CONNECTED_OUTPUT = "CommandLine"  # starts with
    CMD_HACK = "WMIC PROCESS WHERE name='LeagueClientUx.exe' GET commandline"

    def __init__(self) -> None:
        self.protocol = "https"
        self.bt = BackgroundThread(fn_to_run=self.listen, time_between_runs=2)
        self.bt.start()
        print("continuing")
        # asyncio.run(self.listen())
        # task = asyncio.create_task(self.listen())

    def listen(self) -> None:
        """Pseudo-Hook to listen to the status of `LCA`

        Function that runs every X seconds to get the status of `LCA`'s LeagueConnection
        """
        print("Listening to `LCA`...")
        cmd_output = execute_cmd_command(self.CMD_HACK)
        print(f"got {cmd_output}")

    def build_url(self, o: object) -> str:
        """."""
        return ""

    def get(self, url) -> object:
        """."""

    def post(self, url, key) -> object:
        """."""


if __name__ == "__main__":
    lc = LeagueConnection()
    print("AFTER")
