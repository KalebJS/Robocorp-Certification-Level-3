import json
from pathlib import Path
from typing import List

import pandas as pd

from config import Config

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
        self.data = pd.DataFrame([dict(item) for item in items])

    def filter_and_sort_traffic_data(self) -> None:
        print("Filtering and sorting traffic data...")

        both_gender_value = "BTSX"
        self.data = self.data[self.data["genders"] == both_gender_value]

        max_rate = 5.0
        self.data = self.data[self.data["rate"] < max_rate]

        self.data = self.data.sort_values(by=["year"], ascending=False)

    def filter_latest_data_by_country(self) -> None:
        print("Filter latest data by country...")
        self.data = self.data.groupby("country").head(1)

    def create_work_item_payloads(self) -> List[dict]:
        print("Creating work item payloads...")

        payloads = []
        for row in self.data.itertuples():
            payload = {
                "country": row["country"],
                "year": row["year"],
                "rate": row["rate"],
            }
            payloads.append(payload)

        return payloads
