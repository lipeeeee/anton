"""Module for league api HACK'ing

"""

from collections import defaultdict
import re
import requests
from requests.models import Response
from .background_thread import BackgroundThread
from .windows_utils import execute_cmd_command, remove_excessive_spaces
from typing import DefaultDict


class LeagueConnection:
    """A HACK'ed version of `LCA`(League client api)

    Provides riot-access to every `LCA` http/https request

    Attributes:
        cmd_output_dict (Dict): A Dictionary of values of the output of
        `CMD_HACK`

        base_url (str): the base url for the `LCA` interface

        protocol (str): specification of http or https protocols

        username (str): As of patch 13.12 the username used
        in auth is a constant value("riot")

        port (str): the port where `LCA` is
        being hosted on(riot version, normal version is 2999)

        remoting_auth_token (str): Auth key

        connected (bool): connected to `LCA` status

        listener (BackgroundThread): listener for `LCA`'s status

    Class Constants:
        LCA_NOT_CONNECTED_OUTPUT (str): Output when trying to hack but
        `LCA` is down

        LCA_NOT_CONNECTED_OUTPUT (str): Output after sucesseful hacked connection

        CMD_HACK (str): The cmd command to get LCA's info

        LISTEN_TIMEOUT (str): The time in seconds on how long to wait before
        each try of connection

    Data:
    Example request:
        GET https://127.0.0.1:2999/liveclientdata/allgamedata
    Example of no connection to `LCA`:
        "No Instance(s) Available"
    """

    cmd_output_dict: DefaultDict
    base_url: str
    protocol: str
    username: str
    # port: str  # moved to @proprety
    # remoting_auth_token: str @ proprety
    connected: bool
    listener: BackgroundThread

    # Class Constants
    LCA_NOT_CONNECTED_OUTPUT = "No Instance(s) Available"  # starts with
    LCA_CONNECTED_OUTPUT = "CommandLine"  # starts with
    CMD_HACK = "WMIC PROCESS WHERE name='LeagueClientUx.exe' GET commandline"
    LISTEN_TIMEOUT = 2

    def __init__(self) -> None:
        self.cmd_output_dict: DefaultDict = defaultdict(lambda: "default")
        self.base_url = "127.0.0.1"
        self.protocol = "https"
        self.username = "riot"
        self.connected = False

        # Start LCA Listener
        self.listener = BackgroundThread(
            fn_to_run=self.listen, time_between_runs=self.LISTEN_TIMEOUT, daemon=True
        )
        self.listener.start()

    @property
    def port(self):
        """The port where `LCA` is being hosted on"""
        return self.cmd_output_dict["app-port"]

    @property
    def remoting_auth_token(self):
        """Riot auth key"""
        return self.cmd_output_dict["remoting-auth-token"]

    @property
    def auth(self):
        """Auth tuple (username, remoting_auth_token)"""
        return (self.username, self.remoting_auth_token)

    def listen(self) -> None:
        """Listens to the status of `LCA`

        Loads content of `LCA` into:
            self.cmd_output_dict (defaultdict): the contents

            self.connected (bool): the status of connection
        """
        print("Listening to `LCA`...")

        # Process Output
        cmd_output = execute_cmd_command(self.CMD_HACK)
        self.cmd_output_dict = self.parse_cmd_output(self.format_cmd_output(cmd_output))
        self.connected = cmd_output.startswith(self.LCA_CONNECTED_OUTPUT)

        print(f"CMD_OUTPUT_DICT: {self.cmd_output_dict}")
        print(f"RAT: {self.remoting_auth_token}")

    def format_cmd_output(self, output: str) -> str:
        """Formats output from windows's cmd

        Removes '\n' and excessive spaces from the output
        of `CMD_HACK`

        WARNING:
            The execution of this function can most likely be removed
        """
        output = remove_excessive_spaces(output)
        output = re.sub("\n", "", output)
        return output

    def parse_cmd_output(self, output: str) -> DefaultDict:
        """Parses cmd output to a dictionary"""
        variables: DefaultDict = DefaultDict(lambda: "default")
        reg_expr = r'--([\w-]+)=([^"\s]+|"([^"]+))'

        # RegEx find
        matches = re.findall(reg_expr, output)

        # Dictionary parse
        for entry in matches:
            key = entry[0]
            values = entry[1]
            variables[key] = values

        return variables

    def build_url(self, path: str) -> str:
        """Build request url

        Helper function that builds a complete url of a request
        """
        return f"{self.protocol}://{self.base_url}:{self.port}/{path}"

    def get(self, path: str) -> Response | None:
        """Get request"""
        if not self.connected:
            return None

        return requests.get(self.build_url(path), auth=self.auth)

    def post(
        self, path: str, data: dict | None = None, json: dict | None = None
    ) -> Response | None:
        """Post into LCA"""
        if not self.connected:
            return None

        return requests.post(
            self.build_url(path), data=data, json=json, auth=self.auth, verify=False
        )


if __name__ == "__main__":
    lc = LeagueConnection()
