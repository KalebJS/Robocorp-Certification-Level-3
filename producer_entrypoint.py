from config import Config
from src.producer import ProducerProcess
from src.utils import prepare_directory


def main():
    prepare_directory(Config.Paths.Temp.ROOT)
    prepare_directory(Config.Paths.Output.ROOT)

    process = ProducerProcess()
    process.run()


if __name__ == "__main__":
    main()
