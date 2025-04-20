import os
import shutil
import argparse

# Basic file types and their extensions
FILE_TYPES = {
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'documents': ['.pdf', '.doc', '.docx', '.txt'],
    'videos': ['.mp4', '.avi', '.mov'],
    'audio': ['.mp3', '.wav'],
    'archives': ['.zip', '.rar'],
    'code': ['.py', '.js', '.html', '.css','.c']
}

def setup_arguments():
    # Set up command line options
    parser = argparse.ArgumentParser(description='Sort files into folders by type')
    parser.add_argument('folder', nargs='?', default=os.getcwd(),
                      help='Folder to organize (default: current folder)')
    parser.add_argument('--preview', action='store_true',
                      help='Show changes without moving files')
    return parser.parse_args()

def get_file_type(filename):
    # Check what type of file it is based on extension
    extension = os.path.splitext(filename)[1].lower()
    for file_type, extensions in FILE_TYPES.items():
        if extension in extensions:
            return file_type
    return 'other'

def make_unique_name(filepath):
    # Add number to filename if it already exists
    if not os.path.exists(filepath):
        return filepath
    
    folder = os.path.dirname(filepath)
    name, ext = os.path.splitext(os.path.basename(filepath))
    
    counter = 1
    while True:
        new_name = os.path.join(folder, f"{name}_{counter}{ext}")
        if not os.path.exists(new_name):
            return new_name
        counter += 1

def organize_files(folder, preview=False):
    # Create folders for each file type
    for file_type in FILE_TYPES:
        type_folder = os.path.join(folder, file_type)
        if not os.path.exists(type_folder) and not preview:
            os.makedirs(type_folder)
    
    # Count how many files are moved
    moved_files = {}
    
    # Go through each file in the folder
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        
        # Skip folders and this script itself
        if os.path.isdir(filepath) or filename == os.path.basename(__file__):
            continue
        
        # Figure out where to move the file
        file_type = get_file_type(filename)
        if file_type == 'other':
            continue
            
        new_path = os.path.join(folder, file_type, filename)
        if not preview and os.path.exists(new_path):
            new_path = make_unique_name(new_path)
        
        # Move the file or show what would happen
        if preview:
            print(f"Would move {filename} to {file_type} folder")
        else:
            try:
                shutil.move(filepath, new_path)
                print(f"Moved {filename} to {file_type} folder")
                moved_files[file_type] = moved_files.get(file_type, 0) + 1
            except Exception as e:
                print(f"Error moving {filename}: {e}")
    
    return moved_files

def main():
    # Get command line arguments
    args = setup_arguments()
    
    print(f"Organizing files in: {args.folder}")
    if args.preview:
        print("PREVIEW MODE - No files will be moved")
    
    # Organize the files and show results
    results = organize_files(args.folder, args.preview)
    
    if not args.preview and results:
        print("\nFiles organized:")
        for file_type, count in results.items():
            print(f"  {file_type}: {count} files")
        print(f"Total: {sum(results.values())} files")
    
    print("Done!")

if __name__ == "__main__":
    main()