from RPA.Robocorp.WorkItems import Error

from src.data import WorkItem
from src.http import HTTPProxy
from src.http.exception import BadRequestException, BadResponseException
from src.work_items import WorkItemsHandler, BadPayloadError


class ConsumerProcess:
    def __init__(self):
        self.work_items = WorkItemsHandler()
        self.http = HTTPProxy()

    def run(self):
        for work_item in self.work_items.input_work_item_generator():
            try:
                validated_item = WorkItem(**work_item.payload)
            except ValueError as e:
                print(f"Bad payload: {e}")
                self.work_items.release_failed_work_item(
                    exception_type=Error.BUSINESS,
                    code="BAD_PAYLOAD",
                    msg=str(e),
                )
                continue

            try:
                self.http.post_traffic_data_to_sales_system(validated_item)
            except (BadResponseException, BadRequestException) as e:
                print(f"Bad request: {e}")
                self.work_items.release_failed_work_item(code=e.status_code, msg=e.message)
                continue
