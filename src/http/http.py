from pathlib import Path
from RPA.HTTP import HTTP

from config import Config


class Http:
    http: HTTP = HTTP()

    def download_traffic_data(self) -> Path:
        filepath = Config.Paths.Temp.TRAFFIC_JSON
        self.http.download(
            url="https://github.com/robocorp/inhuman-insurance-inc/raw/main/RS_198.json",
            target_file=filepath,
            overwrite=True
        )
        return filepath