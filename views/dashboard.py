# views/dashboard.py 

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
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


def run() -> None:
    
    with Live(make_layout(), refresh_per_second=4, screen=True):   
        for _ in range(5):
            sleep(1)
    

