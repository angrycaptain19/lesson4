###This script sorts files in the folder which user give in an argument when open script in console. And print result in console###

import sys
from pathlib import Path

# Take first argument from conslone after name of script, and check variant if user didn't give way.

# folder_path = sys.argv[1] if sys.argv[1] else folder_path = "Error path"
folder_path = "Error path"

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


formats = {
    "image": ["JPEG", "PNG", "JPG", "SVG"],
    "video": ["AVI", "MP4", "MOV", "MKV"],
    "doc": ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"],
    "music": ["MP3", "OGG", "WAV", "AMR", "M4A"],
    "archive": ["ZIP", "GZ", "TAR", "RAR"]
}

name_list = []
suffix_list = []

# Check condition if script take wrong way.

if folder_path == "Error path":
    print("You didn't enter in console folder path.\nIf you want to sort filest in folder where this script enter Y\n to finish program enter N or anything: ")
    tmp = input("Y/N: ")
    p = Path() if tmp.lower() == "y" else exit()

for i in p.iterdir():
    if i.suffix:
        for key, values in formats.items():
            if i.suffix[1:].upper() in values:
                # if key in list_formatted.keys():
                list_formatted[key].append(i.name)
                list_formatted["exists_formats"].append(
                    f"{i.suffix[1:].upper()}")
        for values in list_formatted.values():
            for val in values:
                if i.suffix[1:].upper() != val:
                    name_list.append(i.name)
                    suffix_list.append(i.suffix[1:].upper())

print(list_formatted.values())
print(name_list)
print(suffix_list)


# for i in p.iterdir():
#     if i.suffix:
#         for value in list_formatted["exists_formats"]:
#             if i.suffix[1:].upper() != value:
#                 list_formatted["unidentified"].append(i.name)
#                 list_formatted["unexists_formats"].append(
#                     f"{i.suffix[1:].upper()}")

# p = Path(folder_path)

# sort(p, formats) if p.exist1 else print("You give wrong way, try again with Right way!")

# Start to work with function


def sort(folder_path=Path(), formats=formats):
    # function sort files in formats in folder.
    # Folder_path is folder path in string, formats is vocabluary
    # where keys are the name of kind format and values are files extension
    # Give result in vocaluary like formats variant with addition keys know_extension and unknow_extension###
    for i in p.iterdir():
        if i.isFile():
            if i.suffix[1:].upper() in formats.keys['image_list'].values():
                image_list_formatted.append(i.name)
                exist_format_list.append(i.suffix)
            elif i.suffix[1:].upper() in formats.keys['video_list'].values():
                video_list_formatted.append(i.name)
                exist_format_list.append(i.suffix)
            elif i.suffix[1:].upper() in formats.keys['doc_list'].values():
                doc_list_formatted.append(i.name)
                exist_format_list.append(i.suffix)
            elif i.suffix[1:].upper() in formats.keys['music_list'].values():
                music_list_formatted.append(i.name)
                exist_format_list.append(i.suffix)
            elif i.suffix[1:].upper() in formats.keys['archive_list'].values():
                archive_list_formatted.append(i.name)
                exist_format_list.append(i.suffix)
            else:
                un_list_formatted.append(i.name)
                unexist_format_list.append(i.suffix)
        elif i.is_dir():
            sort(i, formats)
        else:
            print("If you see this message, that something went wrong")
    return list_formatted


# Result print area:
print("Congragulation!\nYour files had been sorted:")
for key, values in list_formatted.items():
    if list_formatted[key] != []:
        print(f"{key.title()} :", end="")
        for value in set(values):
            print(f" {value}", end='')
        print()
print()
print(list_formatted['unidentified'])
print("Thank you for take our service!")
print(list_formatted)
