import os
import sys

def generate_tree(folder_path, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(folder_path):
            relative_path = os.path.relpath(root, folder_path)

            depth = relative_path.count(os.path.sep)

            tree_representation = f"{'|   ' * (depth - 1)}|-- {os.path.basename(relative_path)}/"

            file.write(f"{tree_representation}\n")

            for file_name in files:
                file.write(f"{'|   ' * depth}|-- {file_name}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python generate_tree.py folder_path")
        sys.exit(1)

    main_folder_path = sys.argv[1]

    output_file_name = 'sounds_tree.txt'

    generate_tree(main_folder_path, output_file_name)

    print(f"Written to {output_file_name}")
