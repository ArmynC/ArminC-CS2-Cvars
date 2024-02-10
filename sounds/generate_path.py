import os
import sys

def generate_path(folder_path, output_file):
    with open(output_file, 'w') as file:
        for root, _, files in os.walk(folder_path):
            relative_path = os.path.relpath(root, folder_path)
            
            file.write(f"{relative_path.replace(os.path.sep, '/')}/\n")
            
            for file_name in files:
                file.write(f"{relative_path.replace(os.path.sep, '/')}/{file_name}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python generate_path.py folder_path")
        sys.exit(1)
    
    main_folder_path = sys.argv[1]
    
    output_file_name = 'sounds_path.txt'
    
    generate_path(main_folder_path, output_file_name)
    
    print(f"Written to {output_file_name}")
