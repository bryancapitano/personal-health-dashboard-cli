class StepsData:
    def __init__(self, all_steps):
        self._all_steps = all_steps

    def __str__(self):
        return f"{self.all_steps}"

    @property
    def all_steps(self) -> list:
        return self._all_steps

    @all_steps.setter
    def steps_data(self, all_steps) -> None:
        self._all_steps = all_steps

    def get_steps_by_day(self) -> dict:
        """Returns a Dict of steps by day: { datetime.date: steps }"""
        steps_by_day = {}  # {date: steps}
        for row in self.all_steps:
            date = row["timestamp"].date()
            # print(f"Date: {date}, Steps: {entry['steps']}")
            # Increment our steps for each day in steps_by_day{}
            steps_by_day[date] = steps_by_day.get(date, 0) + row["steps"]
        return steps_by_day
