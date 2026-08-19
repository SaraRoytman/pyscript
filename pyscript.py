import os

folder = input("Enter folder path: ")

for i, filename in enumerate(os.listdir(folder), start=1):
    old_path = os.path.join(folder, filename)
    new_name = f"{i}_{filename}"
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)
    print(f"{filename} -> {new_name}")