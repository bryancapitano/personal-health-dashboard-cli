# views/dashboard.py

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from readchar import readkey, key


class Dashboard:
    MENU = {
        "day": "Menu: [bold underline](d) Day[/], (w) Week, (m) Month, (q) Quit",
        "week": "Menu: (d) Day, [bold underline](w) Week[/], (m) Month, (q) Quit",
        "month": "Menu: (d) Day, (w) Week, [bold underline](m) Month[/], (q) Quit",
    }
    
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

    def make_footer_menu(self, view="day") -> Panel:
        menu = Panel(
            Dashboard.MENU[view],
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
                elif k== "d":
                    self.layout["footer"].update(self.make_footer_menu("day"))
                elif k == "w":
                    self.layout["footer"].update(self.make_footer_menu("week"))
                elif k == "m":
                    self.layout["footer"].update(self.make_footer_menu("month"))
