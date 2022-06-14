from pathlib import Path
from RPA.HTTP import HTTP
import requests
from retry import retry

from config import Config
from src.data import WorkItem

from .exception import BadRequestException, BadResponseException


class HTTPProxy:
    session: requests.Session = requests.Session()

    def download_traffic_data(self) -> Path:
        print("Downloading traffic data...")
        filepath = Config.Paths.Temp.TRAFFIC_JSON
        self.session.download(
            url="https://github.com/robocorp/inhuman-insurance-inc/raw/main/RS_198.json",
            target_file=filepath,
            overwrite=True,
        )
        return filepath

    @staticmethod
    def _check_response_status(response: requests.Response):
        if 200 <= response.status_code < 300:
            return

        if 400 <= response.status_code < 500:
            raise BadRequestException(response.status_code)
        else:
            raise BadResponseException(response.status_code)

    @retry(BadResponseException, tries=3, delay=1)
    def post_traffic_data_to_sales_system(self, work_item: WorkItem):
        print("Posting traffic data to sales system...")
        response = self.session.post(
            url="https://robocorp.com/inhuman-insurance-inc/sales-system-api", json=work_item.dict()
        )
        self._check_response_status(response)

        return response.json()
