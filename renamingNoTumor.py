import os
import glob

folder_path = "BrainTumorDataset/notumor"  

image_files = sorted(glob.glob(os.path.join(folder_path, "*.jpg")))

# Rename the files starting from 3065
start_number = 3065

for index, file_path in enumerate(image_files):
    new_name = f"{start_number + index}.jpg"  # Generate new name
    new_path = os.path.join(folder_path, new_name)

    os.rename(file_path, new_path)  # Rename the file
    print(f"Renamed: {file_path} → {new_path}")

print("Renaming completed successfully!")