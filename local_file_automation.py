import os
import shutil

def sort_files(source_path):
    """
    Sorts files in a given directory into subfolders based on their extensions.
    """
    
    # 1. Use a Dictionary to map folders to their extensions
    # This makes it incredibly easy to add new file types later (like PDFs or Zip files)
    file_categories = {
        "csv files": [".csv"],
        "image files": [".jpg", ".jpeg", ".png", ".gif"],
        "text files": [".txt"],
        "excel files": [".xlsx", ".xls"]
    }

    # 2. Safely create the target folders if they don't exist
    for folder_name in file_categories.keys():
        # os.path.join is much safer than using string concatenation (+)
        folder_path = os.path.join(source_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"📁 Created folder: {folder_name}")

    # 3. Get all items in the directory
    all_items = os.listdir(source_path)

    # 4. Loop through and sort the files
    for item in all_items:
        item_path = os.path.join(source_path, item)
        
        # Skip folders (we only want to move files)
        if os.path.isdir(item_path):
            continue
            
        moved = False
        
        # Check which category the file belongs to
        for folder, extensions in file_categories.items():
            # Use .endswith() instead of "in" to prevent bugs
            if any(item.lower().endswith(ext) for ext in extensions):
                destination_path = os.path.join(source_path, folder, item)
                
                # Move the file if it doesn't already exist in the target folder
                if not os.path.exists(destination_path):
                    shutil.move(item_path, destination_path)
                    print(f"✅ Moved: {item} -> {folder}/")
                else:
                    print(f"⚠️ Skipped: {item} (Already exists in {folder}/)")
                
                moved = True
                break # Stop checking other categories once we find a match
        
        # Optional: Log files that didn't match any category
        if not moved:
            print(f"⏭️ Ignored: {item} (No matching category)")

# Run the function
if __name__ == "__main__":
    # Use a raw string (r"") for Windows paths
    path = r"C:\Users\banga\OneDrive\Desktop\Python Folders\Projects\automatice file sorted in file explorer"
    
    print("Starting file sort...")
    sort_files(path)
    print("Sort complete!")