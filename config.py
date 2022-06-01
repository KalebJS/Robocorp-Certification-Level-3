from pathlib import Path

cwd = Path.cwd()

class Config:

    class Paths:
        ROOT = cwd

        class Output:
            ROOT = cwd / "output"

        class Temp:
            ROOT = cwd / "temp"
            TRAFFIC_JSON = ROOT / "traffic.json"