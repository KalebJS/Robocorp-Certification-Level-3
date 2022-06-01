from src.http import Http


class ProducerProcess:
    def __init__(self) -> None:
        self.http = Http()

    def run(self):
        raw_data = self.http.download_traffic_data()
        