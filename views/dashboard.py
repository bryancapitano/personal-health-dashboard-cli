# views/dashboard.py

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from readchar import readkey, key
from time import sleep


class Dashboard:

    def __init__(self):
        self.current_view = "day"
        # console = Console()
        self.layout = self.make_layout()
        self.layout["footer"].update(self.make_footer_menu())

    def make_layout(self) -> Layout:
        """Setup the basic layout"""

        layout = Layout()

        layout.split_column(
            Layout(name="upper", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=3),
        )
        layout["main"].split_row(
            Layout(name="left", ratio=1),
            Layout(name="right", ratio=4),
        )
        return layout

    def make_footer_menu(self) -> Panel:
        menu = Panel(
            "Menu: (d) Day, (w) Week, (m) Month, (q) Quit",
            border_style="cyan",
            style="white on blue",
        )
        return menu

    def run(self) -> None:
        """ Start Event Loop -> Listen for user input """

        with Live(self.layout, refresh_per_second=4, screen=True):

            # https://pypi.org/project/readchar/
            while True:
                k = readkey()
                if k == "q":
                    return
