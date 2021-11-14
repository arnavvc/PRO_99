import os
import shutil
import time

def main():
    exists = False
    deleted_folders_count = 0
    deleted_files_count = 0

    print("Files that haven't been used in this amount of days will be DELETED")
    days = input("Enter the amount of the days: ")

    days = int(days) * 86400
    date = time.time() - days

    print("---------------")
    path = input("Enter an existing path: ")

    if os.path.exists(path):
        exists = False
    else:
        exists = True

    while(exists):
        path = input("Re-enter an existing path: ")
        if os.path.exists(path):
            exists = False
        else:
            exists = True

    if (exists == False):
        if os.path.exists(path):
            for root_folder, folders, files in os.walk(path):
                if date >= get_file_date(root_folder):

                    remove_folder(root_folder)
                    deleted_folders_count += 1

                    break

                else:
                    for folder in folders:
                        folder_path = os.path.join(root_folder, folder)

                        if date >= get_file_date(folder_path):
                            remove_folder(folder_path)
                            deleted_folders_count += 1

                    for file in files:
                        file_path = os.path.join(root_folder, file)

                        if date >= get_file_date(file_path):

                            remove_file(file_path)
                            deleted_files_count += 1

            else:

                if date >= get_file_date(path):
                    remove_file(path)
                    deleted_files_count += 1

        else:

            print(f'"{path}" is not found')
            deleted_files_count += 1

        print(f"Total folders deleted: {deleted_folders_count}")
        print(f"Total files deleted: {deleted_files_count}")


def get_file_date(path):
    ctime = os.stat(path).st_ctime

    return ctime

def remove_folder(path):

	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")

	else:
		print("Unable to delete the "+path)

def remove_file(path):

	if not os.remove(path):
		print(f"{path} is removed successfully")

	else:
		print("Unable to delete the "+path)

if __name__ == '__main__':
	main()