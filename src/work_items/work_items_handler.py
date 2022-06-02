from typing import Generator, List
from RPA.Robocorp.WorkItems import WorkItems, EmptyQueue, WorkItem


class WorkItemsHandler:
    def __init__(self) -> None:
        self.workitems = WorkItems(autoload=False)

    def save_work_item_payloads(self, payloads: List[dict]) -> None:
        self.workitems.get_input_work_item()  # no actual input work item, just a formality

        print("Saving work item payloads...")
        for payload in payloads:
            self.workitems.create_output_work_item(variables=payload, save=True)

    def input_work_item_generator(self) -> Generator[WorkItem, None, None]:
        while True:
            try:
                yield self.workitems.get_input_work_item()
            except EmptyQueue:
                break

    def get_work_item_payload(self, work_item: WorkItem) -> dict:
        return work_item.payload
