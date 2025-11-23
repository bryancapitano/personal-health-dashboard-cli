import csv
from datetime import datetime 


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
