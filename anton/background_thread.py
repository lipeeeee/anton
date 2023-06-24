"""Asyncronhous background thread

Made to run a certain function continuously between a 
set period of time

TODO: stop flag
"""

from time import sleep
from threading import Thread
from typing import Callable, Any, Iterable, Mapping


class BackgroundThread(Thread):
    """Background Assynchronous thread

    Runs a function in the background on a set timer. Can be edited
    to support float timers

    Attributes:
        fn_to_run (Callable): Function to run

        time_between_runs (int): Time in seconds of how often the
        `fn_to_run` should be ran
    """

    fn_to_run: Callable
    time_between_runs: int

    def run(self) -> None:
        while True:
            self.fn_to_run()
            sleep(self.time_between_runs)

    def __init__(
        self,
        fn_to_run: Callable,
        time_between_runs: int,
        group: None = None,
        target: Callable[..., object] | None = None,
        name: str | None = None,
        args: Iterable[Any] = ...,
        kwargs: Mapping[str, Any] | None = None,
        *,
        daemon: bool | None = None
    ) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.fn_to_run = fn_to_run
        self.time_between_runs = time_between_runs
