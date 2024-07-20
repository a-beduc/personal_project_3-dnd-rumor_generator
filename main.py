from src.rumor_extractor import CsvExtractor
import os

def main():
    data_directory = os.path.join("data", "general_rumor.csv")
    extractor = CsvExtractor(init_file_path=data_directory)
    # for rumor_id, rumor in extractor.rumors.items():
    # print(f"ID_key: {rumor_id},\n "
    #       f"ID_Obj: {rumor.rumor_id},\n"
    #       f"Title: {rumor.rumor_title},\n")

    print(extractor.rumors)
    rumor_a001 = extractor.get_rumor_by_id(rumor_id="A03")

    print(rumor_a001.rumor_title)


if __name__ == '__main__':
    main()
