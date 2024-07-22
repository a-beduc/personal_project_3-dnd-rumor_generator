import csv
from typing import Optional, Dict, List
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
        self.memory: List[str] = []
        self.save_file = init_file
        self.load_memory()

    def load_memory(self):
        with open(self.save_file, "r", encoding="utf-8") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=",")
            for row in csv_data:
                self.memory.append(row[0])

    def add_to_memory(self, rumor_key):
        self.memory.append(rumor_key)

    def save_memory(self):
        with open(self.save_file, "w", encoding="utf-8", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            for elem in self.memory:
                csv_writer.writerow([elem])

    def __repr__(self) -> str:
        return f"{self.memory}\n"


class RumorGenerator:
    def __init__(self, init_file_path: Optional[str] = None, memory_file_path=None):
        self.init_file_path = init_file_path
        self.memory_file_path = memory_file_path
        self.rumor_memory: RumorMemory = RumorMemory(self.memory_file_path)
        self.rumors: Dict[str, Rumor] = self.init_rumors()
        self.current_rumor = None

    def init_rumors(self) -> Dict[str, Rumor]:
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
        self.remove_saved_rumors(rumors)
        return rumors

    def remove_saved_rumors(self, rumors):
        for rumor_key in self.rumor_memory.memory:
            if rumor_key in rumors:
                rumors.pop(rumor_key)

    def update_memory(self):
        self.rumor_memory.add_to_memory(self.current_rumor.rumor_id)

    def get_rumor_by_id(self, rumor_id: str) -> Optional[Rumor]:
        return self.rumors[rumor_id]

    def get_random_rumor(self) -> Rumor:
        self.current_rumor = self.get_rumor_by_id(random.choice(list(self.rumors.keys())))
