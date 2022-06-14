from config import Config
from src.consumer import ConsumerProcess
from src.utils import prepare_directory


def main():
    prepare_directory(Config.Paths.Temp.ROOT)
    prepare_directory(Config.Paths.Output.ROOT)

    process = ConsumerProcess()
    process.run()


if __name__ == "__main__":
    main()
