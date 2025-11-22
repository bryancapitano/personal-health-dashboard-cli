import csv
from datetime import datetime 
from rich.console import Console
from rich.table import Table
from rich import print as pprint
import plotext as plt
from domain.steps import StepsData


def extract_fitbit_steps(fname: str) -> list:
    '''
    Transform FibBit Steps into -> List of Dicts
    
    Dict Format: 
    {
        "timestamp": dateobject
        "steps": steps
    }
    '''
    steps_list = []
    with open(fname) as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert FitBit's timestamp into datetime object
            dt = datetime.fromisoformat(row['timestamp'])
            steps = int(row['steps'])
            step_dict = {"timestamp": dt, "steps": steps}
            steps_list.append(step_dict)
    return steps_list


def build_table_of_steps(steps_by_day: dict):
    table = Table(title="Steps by Day: October")
    table.add_column("Day of Month", justify="left", style="cyan", no_wrap=True)
    table.add_column("Step Count", style="magenta")

    for date in sorted(steps_by_day):
        table.add_row(f"{date.strftime('%b')} {date.day}", f"{steps_by_day[date]}")
    
    return table


def plot_bargraph(dates, steps):
    ''' Displays bar chart of steps by day '''
       
    # Styling
    plt.canvas_color("black")
    plt.axes_color("black")
    plt.ticks_color("white")
    plt.frame(False)

    # Chart
    plt.bar(dates, steps)
    plt.title("Steps by Day: October")
    plt.show()
    

def unpack_days_and_steps(steps_by_day):
    ''' Breaks dates and steps into seperate Lists '''
    
    # Got unpacking idea here: 
    # https://www.geeksforgeeks.org/python/python-split-dictionary-keys-and-values-into-separate-lists/   
    dates = []
    steps = [] 
    for d, s in sorted(steps_by_day.items()):
        dates.append(d.day), steps.append(s)
    return dates, steps
    

def main():
    # Transform FibBit CSV data -> Python List[]
    month = "./steps_2025-10-01.csv"
    # all_steps_data = extract_fitbit_steps(month)
    steps = StepsData(extract_fitbit_steps(month))
    
    # Aggregate steps by day
    #steps_by_day = get_steps_by_day(all_steps_data)
    
    # Print a table of the steps by day
    # table = build_table_of_steps(steps.get_steps_by_day())
    # console = Console()
    # print("\n")
    # console.print(table)
    
    # Print bar chart of steps by day
    dates, steps = unpack_days_and_steps(steps.get_steps_by_day())
    plot_bargraph(dates, steps)
    
    
if __name__ == "__main__":
    main()

