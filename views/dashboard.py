# views/dashboard.py 

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.align import Align
from textual_image.renderable.halfcell import Image
import sevseg
from time import sleep

console = Console()

def make_layout() -> Layout:
    ''' Setup the basic layout '''
    
    layout = Layout()

    layout.split_column(
        Layout(name="upper", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=3)
    )
    layout["main"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="right", ratio=4),
    )
    return layout


def make_footer_menu() -> Panel:
    menu = Panel(
            "Menu: (d) Day, (w) Week, (m) Month, (q) Quit",
            border_style="cyan",
            style="white on blue",
    )
    return menu
    

def run() -> None:
    
    layout = make_layout()
    layout["footer"].update(make_footer_menu())
    
    with Live(layout, refresh_per_second=4, screen=True):   
        for _ in range(5):
            sleep(1)
    

