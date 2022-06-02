from src.work_items import WorkItemsHandler


class ConsumerProcess:
    def __init__(self):
        self.work_items = WorkItemsHandler()

    def run(self):
        for work_item in self.work_items.input_work_item_generator():
            print(work_item)
