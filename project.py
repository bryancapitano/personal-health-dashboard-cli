import csv
from datetime import datetime 
from rich.console import Console
from rich.table import Table
from rich import print as pprint
import plotext as plt


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


def get_steps_by_day(steps_data: list) -> dict:
    '''
    Returns a Dict of steps by date 
    
    Dict Format: { datetime.date: steps }
    '''
    steps_by_day = {} # {date: steps}
    for row in steps_data:
        date = row['timestamp'].date()
        #print(f"Date: {date}, Steps: {entry['steps']}")
        # Increment our steps for each day in steps_by_day{}
        steps_by_day[date] = steps_by_day.get(date, 0) + row['steps']
    return steps_by_day


def build_table_of_steps(steps_by_day: dict):
    table = Table(title="Steps by Day: October")
    table.add_column("Day of Month", justify="left", style="cyan", no_wrap=True)
    table.add_column("Step Count", style="magenta")

    for date in sorted(steps_by_day):
        table.add_row(f"{date.strftime('%b')} {date.day}", f"{steps_by_day[date]}")
    
    return table
    

def main():
    # Transform FibBit CSV data -> Python List[]
    month = "./steps_2025-10-01.csv"
    all_steps_data = extract_fitbit_steps(month)
    
    # Aggregate steps by day
    steps_by_day = get_steps_by_day(all_steps_data)
    
    # Print a table of the steps by day
    # table = build_table_of_steps(steps_by_day)
    # console = Console()
    # print("\n")
    # console.print(table)
    
    # Print bar chart of steps by day
    # Got unpacking idea here: 
    # https://www.geeksforgeeks.org/python/python-split-dictionary-keys-and-values-into-separate-lists/   
    dates = []
    steps = [] 
    for d, s in sorted(steps_by_day.items()):
        dates.append(d.day), steps.append(s)
    
    # Styling
    plt.canvas_color("black")
    plt.axes_color("black")
    plt.ticks_color("white")
    plt.frame(False)             # optional: remove border

    # Chart
    plt.bar(dates, steps)
    plt.title("Steps by Day: October")
    plt.show()
    
    
if __name__ == "__main__":
    main()

