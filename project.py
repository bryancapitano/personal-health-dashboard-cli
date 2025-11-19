import csv
from datetime import datetime 
from rich.console import Console
from rich.table import Table
from rich import print


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
    Returns a Dict of steps by day
    
    Dict Format: 
    {
        "day": datetime.day
        "steps": steps
    }
    '''
    steps_by_day = {} # {day: steps, day: steps, ...}
    for row in steps_data:
        day = row['timestamp'].day
        #print(f"Day: {day}, Steps: {entry['steps']}")
        # Increment our steps for each day in steps_by_day{}
        steps_by_day[day] = steps_by_day.get(day, 0) + row['steps']
    return steps_by_day


def build_table_of_steps(steps_by_day: dict):
    table = Table(title="Steps by Day: October")
    table.add_column("Day of Month", justify="left", style="cyan", no_wrap=True)
    table.add_column("Step Count", style="magenta")

    for day, steps in steps_by_day.items():
        table.add_row(f"{day}", f"{steps}")
    
    return table
    

def main():
    # Build List of Steps from a single month of FibBit data
    month = "./steps_2025-10-01.csv"
    all_steps_data = extract_fitbit_steps(month)
    
    # Aggregate steps by day
    steps_by_day = get_steps_by_day(all_steps_data)
    
    # Print a table of the steps by day
    table = build_table_of_steps(steps_by_day)
    console = Console()
    print("\n")
    console.print(table)
    
    
if __name__ == "__main__":
    main()

