from typing import List
from RPA.Robocorp.WorkItems import WorkItems


class WorkItemsHandler:
    def __init__(self) -> None:
        self.workitems = WorkItems()
        self.workitems.get_input_work_item()  # no actual input work item, just a formality

    def save_work_item_payloads(self, payloads: List[dict]) -> None:
        print("Saving work item payloads...")
        for payload in payloads:
            self.workitems.create_output_work_item(variables=payload, save=True)
