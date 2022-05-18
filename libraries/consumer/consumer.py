from typing import List, Tuple

from requests import Session, Response

from .exceptions import ServerError, BadRequest
from .utilities import retry_on_server_error


class Consumer:
    """
    Inhuman Insurance, Inc. Artificial Intelligence System robot. Consumes traffic data work items.
    """

    def __init__(self):
        """
        Constructor.
        """
        self.session = Session()

    @staticmethod
    def filter_traffic_data(traffic_data: List[dict]) -> Tuple[List[dict], List[dict]]:
        """
        Separates the incorrect traffic data.

        Args:
            traffic_data (List[dict]): The traffic data.

        Returns:
            Tuple[List[dict], List[dict]]: The separated traffic data.
        """
        print("Separating incorrect traffic data...")

        correct_data = list()
        incorrect_data = list()
        for item in traffic_data:
            if (len(item["country"]) != 3 or
                    item["rate"] < 0.0):
                incorrect_data.append(item)
            else:
                correct_data.append(item)

        print("Separated incorrect traffic data")
        return correct_data, incorrect_data

    @staticmethod
    def _check_response(response: Response) -> None:
        """
        Checks the response.

        Args:
            response (Response): The response.

        Raises:
            ServerError: If the response is a 500+ error.

        """
        if 500 <= response.status_code < 600:
            raise ServerError(response.status_code)
        elif response.status_code != 200:
            raise BadRequest(response.status_code)

    @retry_on_server_error
    def post_traffic_data_to_sales_system(self, traffic_item: dict):
        """
        Posts the traffic data to the sales system.

        Args:
            traffic_item (dict): The traffic item.
        """
        response = self.session.post(
            url="https://robocorp.com/inhuman-insurance-inc/sales-system-api", json=traffic_item
        )
        self._check_response(response)

    def send_traffic_data(self, traffic_data: List[dict]) -> List[dict]:
        """
        Posts the traffic data to the sales system.

        Args:
            traffic_data (List[dict]): The traffic data.

        Returns:
            List[dict]: The unsuccessful traffic data.
        """
        print("Posting traffic data to sales system...")

        failed_items = list()
        consecutive_failed_items = 0
        for item in traffic_data:
            try:
                self.post_traffic_data_to_sales_system(item)
                consecutive_failed_items = 0
            except ServerError or BadRequest as e:
                print(f"Failed to post traffic data item: {e}")
                failed_items.append(item)
                consecutive_failed_items += 1
                if consecutive_failed_items > 4:
                    print("Too many consecutive failed items, aborting")
                    break
        else:
            print("Posted traffic data to sales system")

        return failed_items
