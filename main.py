import os
from src.gui import start_gui


def main():
    """Data directory and memory directory are csv file containing respectively every rumors and id of rumors saved in
        memory. These files should be replaced by a Database in the future"""
    data_directory = os.path.join(os.path.dirname(__file__), "data", "general_rumor.csv")
    memory_directory = os.path.join(os.path.dirname(__file__), "memory", "memory.csv")
    start_gui(data_directory, memory_directory)


if __name__ == '__main__':
    main()
