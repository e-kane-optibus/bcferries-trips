import sys
import os
import csv
import io

COLOR_RED   = "\033[1;31m"
COLOR_GREEN = "\033[0;32m"
COLOR_RESET = "\033[0;0m"

def convert_file():
    if len(sys.argv) < 2:
        print(COLOR_RED + "No file provided!" + COLOR_RESET)
        exit()
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print(COLOR_RED + "Input is not a file! Please input trips.txt." + COLOR_RESET)
        exit()
    make_new_file(filepath)        
    
def make_new_file(filepath):
    with open(filepath, "rb") as file_raw:
        trips_txt = io.TextIOWrapper(file_raw)
        csv_file = csv.DictReader(trips_txt)
        csv_list = list(csv_file)
        file_name = "trips_new.txt"
        if os.path.exists(file_name):
            print(COLOR_RED + "File with name " + file_name + " already exists in directory; cannot create a new one. Move this file and try again." + COLOR_RESET)
            return
        new_file = open(file_name, "w",newline="")
        new_csv_writer = csv.DictWriter(new_file, fieldnames=csv_file.fieldnames + ["service ID + trip ID"])
        new_csv_writer.writeheader()
        for row in csv_list:
            if row["trip_short_name"]:
                row["service ID + trip ID"] = row["service_id"] + row["trip_id"]
        for row in csv_list:
            row["block_id"] = ""
            new_csv_writer.writerow(row)
        new_file.close()
        print(COLOR_GREEN + "Exported " + file_name + " with all block_id values removed and a combined serive ID for all trips with short names." + COLOR_RESET)

if __name__ == "__main__":
    convert_file()
