from src.data import TrafficData
from src.http import Http


class ProducerProcess:
    def __init__(self) -> None:
        self.http = Http()
        self.traffic_data = TrafficData()

    def run(self):
        raw_data = self.http.download_traffic_data()
        self.traffic_data.load_traffic_data_as_table(raw_data)
        self.traffic_data.filter_and_sort_traffic_data()
