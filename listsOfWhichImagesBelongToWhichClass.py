import os

meningioma_folder = 'BrainTumorDataset/BrainTumorImages/1'
glioma_folder = 'BrainTumorDataset/BrainTumorImages/2'
pituitary_tumor_folder = 'BrainTumorDataset/BrainTumorImages/3'

# Get all files in the folder
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Print the list of file names
print(file_names)