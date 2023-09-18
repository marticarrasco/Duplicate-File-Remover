# Duplicate File Remover

## Description

This Python script searches a given directory for duplicate files that have the naming convention of ending with ` (1)`. If it finds any such files and their corresponding original versions (without the ` (1)` suffix), it lists them for the user and asks for confirmation before proceeding with the deletion.

## Usage

1. Make sure you have Python 3.x installed on your machine.
2. Save the script as `remove_duplicates.py` (or any other name you prefer).
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is located.
5. Run the script with the command:

    ```bash
    python remove_duplicates.py
    ```

6. When prompted, input the path to the directory you'd like to scan for duplicate files.
7. The script will display a list of potential duplicates.
8. Confirm the deletion by entering `yes` when prompted. Otherwise, enter `no` to abort the operation.

## Caution

**Always ensure you have backups of important data. This script deletes files, so use it at your own risk.**

## License

This script is provided under the MIT License. Use, modify, and distribute as you see fit, but ensure to give appropriate credit.
