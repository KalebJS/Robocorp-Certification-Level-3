import json
import os
from typing import List, Tuple

from RPA.HTTP import HTTP

from workflow import TEMP_DIR


class Producer:
    """
    Inhuman Insurance, Inc. Artificial Intelligence System robot. Produces traffic data work items.
    """

    def __init__(self):
        """
        Initializes the producer.
        """
        self.http = HTTP()

    def download_traffic_data(self) -> str:
        """
        Downloads traffic data from the Internet.

        Returns:
            str: The path to the downloaded traffic data.
        """
        print("Downloading traffic data...")

        output_file = os.path.join(TEMP_DIR, "traffic.json")
        self.http.download(
            url="https://github.com/robocorp/inhuman-insurance-inc/raw/main/RS_198.json",
            target_file=output_file,
            overwrite=True
        )

        print("Downloaded traffic data to {}".format(output_file))

        return output_file

    def parse_traffic_data(self, traffic_data_json_filepath: str) -> List[dict]:
        """
        Parses the traffic data.

        Args:
            traffic_data_json_filepath (str): The path to the traffic data.

        Returns:
            List[dict]: The parsed traffic data.
        """
        print("Parsing traffic data...")

        with open(traffic_data_json_filepath, "r") as traffic_data_json_file:
            traffic_data_json = json.load(traffic_data_json_file)["value"]

        edible_data = [item for item in traffic_data_json if
                       (item["NumericValue"] < 5.0 and item["Dim1"].lower() == "btsx")]

        result_data = list()
        for item in edible_data:
            item = {
                "country": item["SpatialDim"],
                "year": item["TimeDim"],
                "rate": item["NumericValue"]
            }
            result_data.append(item)

        print("Parsed traffic data")
        return result_data