import os

directory_list = ["Aluminium", "Carton", "Glass", "OrganicWaste",
                  "OtherPlastics", "PaperandCardboard", "Plastic", "Textiles", "Wood"]

for directory in directory_list:
    dirname = f"/Users/christianbennett/Desktop/TrashData/{directory}"

    os.chdir(dirname)
    print(os.getcwd())

    for count, f in enumerate(os.listdir()):
        f_name, f_ext = os.path.splitext(f)
        f_name = f"{directory}" + str(count)

        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)
