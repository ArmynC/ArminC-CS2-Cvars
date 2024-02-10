import os
import sys

def generate_play_cvar(root_dir, output_file):
    with open(output_file, 'a') as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                relative_path = os.path.relpath(os.path.join(dirpath, filename), root_dir)
                play_statement = f"play {os.path.splitext(relative_path)[0].replace(os.path.sep, '/')}"
                f.write(f"{play_statement}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python generate_tree.py <path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    output_file = os.path.join(os.path.dirname(__file__), 'sounds_cvar.txt')

    if not os.path.isdir(folder_path):
        print(f"'{folder_path}' invalid directory")
        sys.exit(1)

    open(output_file, 'w').close()

    generate_play_cvar(folder_path, output_file)
