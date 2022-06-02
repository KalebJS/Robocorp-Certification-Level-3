import json
from pathlib import Path

import pandas as pd

from .models import TrafficDataItem


class TrafficData:
    def __init__(self) -> None:
        self.data: pd.DataFrame = None

    def load_traffic_data_as_table(self, traffic_data_file: Path) -> None:
        print("Loading traffic data...")
        with open(traffic_data_file) as f:
            data = json.load(f)

        values = data["value"]
        items = [TrafficDataItem(**item) for item in values]
        self.data = pd.DataFrame(items)
