#!/usr/bin/env python3

import os
import sys
import shutil

# Constants
TEMPLATE_FILE = "./utils/template.py"
PREP_DIR = "../prep"


def heading_to_camel_case(heading: str) -> str:
    words = heading.split()
    camel_case_heading = words[0].lower() + "".join(word.title() for word in words[1:])
    return camel_case_heading


def create_question_folder(question_name):
    # Convert question name to lowercase and replace spaces with underscores
    folder_name = heading_to_camel_case(question_name)
    folder_path = os.path.join(PREP_DIR, folder_name)

    # Create the directory if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created directory: {folder_path}")
    else:
        print(f"Directory '{folder_path}' already exists.")
        return

    # Copy template.py file as solution.py
    template_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), TEMPLATE_FILE
    )
    solution_file_path = os.path.join(folder_path, "solution.py")
    shutil.copyfile(template_path, solution_file_path)

    print(f"Created solution file: {solution_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: createfile "Question Name"')
        sys.exit(1)

    question_name = sys.argv[1]

    if not os.path.exists(PREP_DIR):
        print("Error: Prep directory not found.")
        sys.exit(1)

    create_question_folder(question_name)
