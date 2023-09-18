import os

def get_files_to_delete(folder_path):
    files_to_delete = []

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            # Split the file name and extension
            file_base, file_extension = os.path.splitext(file_name)

            # Check if the file name ends with " (1)"
            if file_base.endswith(" (1)"):
                original_file_base = file_base[:-4]  # Remove " (1)" from the name
                original_file = f"{original_file_base}{file_extension}"

                # Check if the original file exists in the directory
                if original_file in files:
                    # Create full path to the duplicate file
                    duplicate_file_path = os.path.join(root, file_name)
                    files_to_delete.append(duplicate_file_path)

    return files_to_delete

if __name__ == "__main__":
    folder_path = input("Enter the path to the directory: ")

    if os.path.exists(folder_path):
        files_to_delete = get_files_to_delete(folder_path)
        
        if files_to_delete:
            print("\nThe following files will be deleted:\n")
            for file_path in files_to_delete:
                print(file_path)
            
            confirmation = input("\nDo you wish to continue? (yes/no): ").strip().lower()
            if confirmation == 'yes':
                for file_path in files_to_delete:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            else:
                print("Operation aborted by the user.")
        else:
            print("No duplicate files found.")

    else:
        print("Invalid directory. Please check the path and try again.")

