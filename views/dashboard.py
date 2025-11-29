# views/dashboard.py

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from readchar import readkey, key


class Dashboard:
    MENU = {
        "d": "Menu: [bold underline](d) Day[/], (w) Week, (m) Month, (q) Quit",
        "w": "Menu: (d) Day, [bold underline](w) Week[/], (m) Month, (q) Quit",
        "m": "Menu: (d) Day, (w) Week, [bold underline](m) Month[/], (q) Quit",
    }
    
    def __init__(self):
        self.current_view = "day"
        # console = Console()
        self.layout = self.make_layout()
        self.make_footer_menu()

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

    def make_footer_menu(self, view="d") -> None:
        menu = Panel(
            Dashboard.MENU[view],
            border_style="cyan",
            style="white on blue",
        )
        self.layout["footer"].update(menu)
    
    def handle_keypress(self, key) -> str | None:
        if key == "q":
            return key
        elif key in ["d", "w", "m"]:
            self.make_footer_menu(key)
        return None

    def run(self) -> None:
        """ Start Event Loop -> Listen for user input """

        with Live(self.layout, refresh_per_second=4, screen=True):

            # https://pypi.org/project/readchar/
            while True:
                if self.handle_keypress(readkey()) == "q": return
                
