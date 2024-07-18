import os
import csv


class Rumor:
    def __init__(self):
        self.rumor_id = None
        self.rumor_subject = None
        self.rumor_title = None
        self.rumor_text = None
        self.tag_boi = None
        self.tag_hou = None
        self.tag_bre = None
        self.tag_bry = None
        self.tag_din = None
        self.tag_kon = None
        self.tag_hav = None
        self.tag_tar = None
        self.tag_ter = None
        self.tag_dou = None

    def __repr__(self):
        return f"{self.rumor_title}\n"


class CsvExtractor:

    def __init__(self, init_file_path=None):
        self.init_file_path = init_file_path
        self.rumors = self.init_rumors()

    def init_rumors(self):
        rumors = {}
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

    def get_rumor_by_id(self, rumor_id):
        return self.rumors[rumor_id]


def main():
    data_directory = os.path.join("data", "general_rumor.csv")
    extractor = CsvExtractor(init_file_path=data_directory)
    # for rumor_id, rumor in extractor.rumors.items():
    # print(f"ID_key: {rumor_id},\n "
    #       f"ID_Obj: {rumor.rumor_id},\n"
    #       f"Title: {rumor.rumor_title},\n")

    print(extractor.rumors)
    rumor_a001 = extractor.get_rumor_by_id(rumor_id="A001")
    print(rumor_a001.rumor_title)


if __name__ == '__main__':
    main()
