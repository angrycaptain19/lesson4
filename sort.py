###This script sorts files in the folder which user give in an argument when open script in console. And print result in console###

import sys
import os
from pathlib import Path

# Lists for works:
list_formatted = {
    "image": [],
    "video": [],
    "doc": [],
    "music": [],
    "archive": [],
    "unidentified": [],
    "exists_formats": [],
    "unexists_formats": []
}  # vocabluary for result function

# Start to work with functions


def print_vocabluary(vocabluary={}):
    print("Congragulation!\nYour files had been sorted:")
    for key, values in list_formatted.items():
        if list_formatted[key] != []:
            print(f"{key.title()} :", end="")
            for value in set(values):
                print(f" {value}", end='')
            print()
    print()
    list_formatted.clear()
    print("Thank you for take our service!")


def sort(folder_path=Path()):
    # function sort files in formats in folder.
    # Folder_path is folder path in string, formats is vocabluary
    # where keys are the name of kind format and values are files extension
    # Give result in vocaluary like formats variant with addition keys know_extension and unknow_extension###
    formats = {
        "image": ["JPEG", "PNG", "JPG", "SVG"],
        "video": ["AVI", "MP4", "MOV", "MKV"],
        "doc": ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"],
        "music": ["MP3", "OGG", "WAV", "AMR", "M4A"],
        "archive": ["ZIP", "GZ", "TAR", "RAR"]
    }
    name_list = []
    suffix_list = []
    tmp = []
    p = Path(folder_path)
    for i in p.iterdir():
        if i.is_file() and i.suffix:
            for key, values in formats.items():
                if i.suffix[1:].upper() in values:
                    # if key in list_formatted.keys():
                    list_formatted[key].append(i.name)
                    list_formatted["exists_formats"].append(
                        f"{i.suffix[1:].upper()}")
            name_list.append(i.name)
            suffix_list.append(i.suffix[1:].upper())
        # I need add list to find name of files in dir wich unidentified.
        # Because anoter method didn't work.
        for value in list_formatted.values():
            if value != []:
                tmp = tmp[:] + value[:]
        while name_list:
            name = name_list.pop()
            if name not in tmp:
                list_formatted["unidentified"].append(name)
        for value in suffix_list:
            if value not in list_formatted["exists_formats"]:
                list_formatted["unexists_formats"].append(value)
    for i in p.iterdir():
        if i.is_dir():
            # if [f for f in os.listdir(i.name) if not f.startswith('.')] == []:
            #     break
            # else:
            if not i.name.startswith('.'):
                print(f"files from enclosure folder {i.name}: ")
                vocabluary_enclosure = sort(f"{i.name}")
                print_vocabluary(vocabluary_enclosure)
                vocabluary_enclosure.clear()
        elif i.is_file():
            continue
        else:
            print("If you see this message, that something went wrong")
    return list_formatted

# Take first argument from conslone after name of script, and check variant if user didn't give way.


try:
    folder_path = sys.argv[1]
except IndexError:
    folder_path = "Error path"

# Check condition if script take wrong way.

if folder_path == "Error path":
    print("You didn't enter in console folder path.\nIf you want to sort filest in folder where this script enter Y\n to finish program enter N or anything: ")
    tmp = input("Y/N: ")
    folder_path = Path() if tmp.lower() == "y" else exit()

#
# sort(p, formats) if p.exist1 else print("You give wrong way, try again with Right way!")
tmp = sort(folder_path)
print_vocabluary(tmp)

# Result print area:
