import os
import csv
from typing import Optional, Dict


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


class CsvExtractor:
    def __init__(self, init_file_path: Optional[str] = None):
        self.init_file_path = init_file_path
        self.rumors: Dict[str, Rumor] = self.init_rumors()

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
        try:
            return self.rumors[rumor_id]
        except KeyError:
            print(f"The key {rumor_id} doesn't exist.")
            return None
        except AttributeError:
            print(f"The key {rumor_id} doesn't exist.")
            return None
        except TypeError:
            print(f"The key {rumor_id} doesn't exist.")
            return None


def main():
    data_directory = os.path.join("data", "general_rumor.csv")
    extractor = CsvExtractor(init_file_path=data_directory)
    # for rumor_id, rumor in extractor.rumors.items():
    # print(f"ID_key: {rumor_id},\n "
    #       f"ID_Obj: {rumor.rumor_id},\n"
    #       f"Title: {rumor.rumor_title},\n")

    print(extractor.rumors)
    rumor_a001 = extractor.get_rumor_by_id(rumor_id="A033")

    print(rumor_a001.rumor_title)


if __name__ == '__main__':
    main()
