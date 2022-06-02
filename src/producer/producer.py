from src.data import TrafficDataHandler
from src.http import HTTPProxy
from src.work_items import WorkItemsHandler


class ProducerProcess:
    def __init__(self) -> None:
        self.http = HTTPProxy()
        self.traffic_data = TrafficDataHandler()
        self.workitems = WorkItemsHandler()

    def run(self):
        raw_data = self.http.download_traffic_data()

        self.traffic_data.load_traffic_data_as_table(raw_data)
        self.traffic_data.filter_and_sort_traffic_data()
        self.traffic_data.filter_latest_data_by_country()

        payloads = self.traffic_data.create_work_item_payloads()
        self.workitems.save_work_item_payloads(payloads)
