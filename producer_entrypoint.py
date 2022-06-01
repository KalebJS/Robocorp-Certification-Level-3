from src.producer import ProducerProcess


def main():
    process = ProducerProcess()
    process.run()


if __name__ == "__main__":
    main()