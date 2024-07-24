import csv
from typing import Optional, Dict, List
import random


class Rumor:
    """Class that represent object rumor, and its content str(id / subject / title / text)
        and tags boolean(boi, hou, bre, bry, din, kon, hav, tar, ter, dou)"""
    def __init__(self):
        self.rumor_id: Optional[str] = None
        self.rumor_subject: Optional[str] = None
        self.rumor_title: Optional[str] = None
        self.rumor_text: Optional[str] = None
        self.tags: Dict[str, bool] = {
            "tag_boi": True,
            "tag_hou": True,
            "tag_bre": True,
            "tag_bry": True,
            "tag_din": True,
            "tag_kon": True,
            "tag_hav": True,
            "tag_tar": True,
            "tag_ter": True,
            "tag_dou": True,
        }

    def __repr__(self) -> str:
        return f"{self.rumor_title}\n"


class RumorMemory:
    """Class that handle, the archived rumor so that a rumor doesn't come up more than once to the players"""
    def __init__(self, init_file: Optional[str] = None):
        self.memory: List[str] = []
        self.save_file = init_file
        self.load_memory()

    def load_memory(self):
        """Method to extracts rumors ID found in the file memory.csv and add them to the active memory of the program"""
        with open(self.save_file, "r", encoding="utf-8") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            for row in csv_data:
                self.memory.append(row[0])

    def add_to_memory(self, rumor_key):
        """Method to add a rumor to the active memory of the program"""
        self.memory.append(rumor_key)

    def save_memory(self):
        """Method to save rumors ID found in the active memory to the memory.csv file ;
            it deletes the content of the file memory.csv and replace it with the active memory"""
        with open(self.save_file, "w", encoding="utf-8", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            for elem in self.memory:
                csv_writer.writerow([elem])

    def __repr__(self) -> str:
        return f"{self.memory}\n"


class RumorGenerator:
    """Class is a composition of Class Rumor, RumorMemory and its own methods.
        Mainly it contains a dictionary where Key = rumor_ID and Value = Rumor
        It also serves the purpose of initializing the rumors from a csv file
        and presenting a random rumor from the dictionary"""
    def __init__(self, init_file_path: Optional[str] = None, memory_file_path=None):
        """ Attribute of the class, the order of initialization is important
            since self.rumors call self.rumor_memory"""
        self.init_file_path = init_file_path
        self.memory_file_path = memory_file_path
        self.rumor_memory: RumorMemory = RumorMemory(self.memory_file_path)
        self.rumors: Dict[str, Rumor] = self.init_rumors()
        self.current_rumor = None
        self.filtered_rumors: Dict[str, Rumor] = self.rumors.copy()

    def init_rumors(self) -> Dict[str, Rumor]:
        """ This method initialize the rumors from a csv file
            It also remove rumors from the rumors dictionary if the rumor_Id is found in the memory.csv"""
        rumors: Dict[str, Rumor] = {}
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
                rumor.tags["tag_boi"] = row[4]
                rumor.tags["tag_hou"] = row[5]
                rumor.tags["tag_bre"] = row[6]
                rumor.tags["tag_bry"] = row[7]
                rumor.tags["tag_din"] = row[8]
                rumor.tags["tag_kon"] = row[9]
                rumor.tags["tag_hav"] = row[10]
                rumor.tags["tag_tar"] = row[11]
                rumor.tags["tag_ter"] = row[12]
                rumor.tags["tag_dou"] = row[13]
                rumors[rumor.rumor_id] = rumor
        self.remove_saved_rumors(rumors)
        return rumors

    def remove_saved_rumors(self, rumors):
        """ This method remove a rumor from the rumors dictionary if its key is in the list rumor_memory"""
        for rumor_key in self.rumor_memory.memory:
            if rumor_key in rumors:
                rumors.pop(rumor_key)
        self.filtered_rumors = rumors.copy

    def update_memory(self):
        """ This method add the current_rumor ID to the list of rumor_memory"""
        self.rumor_memory.add_to_memory(self.current_rumor.rumor_id)
        self.rumors.pop(self.current_rumor.rumor_id)
        self.filtered_rumors = self.rumors.copy()

    def get_rumor_by_id(self, rumor_id: str) -> Optional[Rumor]:
        """ This method return the Value : object Rumor with the specified Key : rumor_ID"""
        return self.rumors[rumor_id]

    def get_random_rumor(self) -> Rumor:
        """ This method change the attribute of the current_rumor to a random rumor from the rumors dictionary"""
        self.current_rumor = self.get_rumor_by_id(random.choice(list(self.filtered_rumors.keys())))

    def remove_by_tag(self, list_of_tags: List[str]):
        self.filtered_rumors = {}
        for rumor_id, rumor in self.rumors.items():
            for tag in list_of_tags:
                if rumor.tags.get(tag, False):
                    self.filtered_rumors[rumor_id] = rumor
                    break
