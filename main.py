from exif import Image 

def import_img(file_name):
    with open(file_name, 'rb') as img:
        unmodified = Image(img)
    return unmodified

def save_img(file, fname):
    with open(("modified_"+fname), 'wb') as modified:
        modified.write(file.get_file())
    
def delete_all(image):
    if image.has_exif:
        for i in image.list_all():
            try:
                image.delete(str(i))
            except():
                pass
    else:
        print("No EXIF data associated with provided image")
    
def delete_specific(image, tag):
    if image.has_exif:
        try:
            image.delete(str(tag))
        except():
            pass
    else:
        print("No EXIF data associated with provided image")

def delete_multiple(image, tag_list):
    if image.has_exif:
        for i in tag_list:
            try:
                image.delete(str(i))
            except():
                pass
    else:
        print("No EXIF data associated with provided image")

def print_all_data(image):
    if image.has_exif:
        for i in image.list_all():
            print(f"{i} : {image.get(str(i))}")
    else:
        print("No EXIF data associated with provided image")

def print_data(image, tag):
    try:
        print(f"{tag} : {image.get(str(tag))}")
    except(KeyError):
        print(f"Tag: {tag} not associated with provided image")

flag = True
while flag:
    try:
        input1 = input("Enter path: ")
        img = import_img(input1)
        modified = False
        while flag:
            print(
"""
Options:
- wipe: deletes all EXIF data
- list: lists all EXIF data attached to the image
- save: Exit and save changes made to new image
""")
            input2 = input("Enter command:").lower()
            print()
            if (input2 == "wipe"):
                delete_all(img)
                modified = True
            elif (input2 == "list"):
                print_all_data(img)
            elif (input2 == "save"):
                if modified:
                    save_img(img, input1)
                flag = False
            else:
                print("invalid input")
    except(FileNotFoundError):
        print("Please enter a valid file path")