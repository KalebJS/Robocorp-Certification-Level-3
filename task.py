import os
import shutil

from libraries import Producer, Consumer
from workflow import TEMP_DIR, OUTPUT_DIR


class Process:
    def __init__(self):
        for directory in [TEMP_DIR, OUTPUT_DIR]:
            shutil.rmtree(directory, ignore_errors=True)
            os.mkdir(directory)

        self.producer = Producer()
        self.consumer = Consumer()

    def run(self):
        """
        Run the process

        :return: None
        """

        # Start the producer
        traffic_data_json = self.producer.download_traffic_data()
        parsed_traffic_data = self.producer.parse_traffic_data(traffic_data_json)

        # Start the consumer
        correct_traffic_data, incorrect_traffic_data = self.consumer.filter_traffic_data(parsed_traffic_data)
        self.consumer.send_traffic_data(correct_traffic_data)


if __name__ == "__main__":
    process = Process()
    process.run()
