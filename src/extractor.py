import csv
from typing import Optional, Dict
import random
import os


class Rumor:
    def __init__(self):
        self.rumor_id: Optional[str] = None
        self.rumor_subject: Optional[str] = None
        self.rumor_title: Optional[str] = None
        self.rumor_text: Optional[str] = None
        self.tag_boi: Optional[str] = None
        self.tag_hou: Optional[str] = None
        self.tag_bre: Optional[str] = None
        self.tag_bry: Optional[str] = None
        self.tag_din: Optional[str] = None
        self.tag_kon: Optional[str] = None
        self.tag_hav: Optional[str] = None
        self.tag_tar: Optional[str] = None
        self.tag_ter: Optional[str] = None
        self.tag_dou: Optional[str] = None

    def __repr__(self) -> str:
        return f"{self.rumor_title}\n"


class RumorMemory:
    def __init__(self, init_file: Optional[str] = None):
        self.memory: Dict[str, Rumor] = {}

    def load_memory(self):
        pass

    def add_to_memory(self):
        pass

    def save_memory(self):
        pass

    def __repr__(self) -> str:
        pass


class RumorGenerator:
    def __init__(self, init_file_path: Optional[str] = None, current_memory=None):
        self.init_file_path = init_file_path
        self.rumors: Dict[str, Rumor] = self.init_rumors()
        self.rumor_memory: RumorMemory = RumorMemory()
        self.current_memory = current_memory

    def init_rumors(self) -> Dict[str, Rumor]:
        rumors: Dict[str, Rumor] = {}
        try:
            with open(self.init_file_path, "r", encoding="utf-8") as csvfile:
                csv_data = csv.reader(csvfile, delimiter=",")
                for row in csv_data:
                    if row[0] == "rumor_id":
                        continue
                    rumor = Rumor()
                    rumor.rumor_id = row[0]
                    rumor.rumor_subject = row[1]
                    rumor.rumor_title = row[2]
                    rumor.rumor_text = row[3]
                    rumor.tag_boi = row[4]
                    rumor.tag_hou = row[5]
                    rumor.tag_bre = row[6]
                    rumor.tag_bry = row[7]
                    rumor.tag_din = row[8]
                    rumor.tag_kon = row[9]
                    rumor.tag_hav = row[10]
                    rumor.tag_tar = row[11]
                    rumor.tag_ter = row[12]
                    rumor.tag_dou = row[13]
                    rumors[rumor.rumor_id] = rumor
            return rumors
        except FileNotFoundError:
            print(f"File not found at {self.init_file_path}")
            return rumors

    def get_rumor_by_id(self, rumor_id: str) -> Optional[Rumor]:
        return self.rumors[rumor_id]

    def get_random_rumor(self) -> Rumor:
        return self.get_rumor_by_id(random.choice(list(self.rumors.keys())))


def main():
    data_directory = os.path.join(os.path.dirname(__file__), "..", "data", "general_rumor.csv")
    extractor = RumorGenerator(init_file_path=data_directory)
    # for rumor_id, rumor in extractor.rumors.items():
    # print(f"ID_key: {rumor_id},\n "
    #       f"ID_Obj: {rumor.rumor_id},\n"
    #       f"Title: {rumor.rumor_title},\n")

    # print(extractor.rumors)
    rumor_a001 = extractor.get_rumor_by_id(rumor_id="A003")
    print(rumor_a001)
    rumor_a002 = extractor.get_rumor_by_id(rumor_id="A002")
    print(rumor_a002.rumor_id)
    print("------")
    random_rumorx = extractor.get_random_rumor()
    print(random_rumorx.rumor_id)
    print(random_rumorx.rumor_title)
    print(random_rumorx.rumor_text)


if __name__ == "__main__":
    main()
