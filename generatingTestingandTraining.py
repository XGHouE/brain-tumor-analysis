import os
import shutil
import random

# Paths
source_folder = "wholeDataset/Scans"  # Update with the actual path
train_folder = "Training Set"
test_folder = "Testing Set"

# Create directories if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Get all image filenames
all_images = [f"{i}.jpg" for i in range(1, 4660)]  # Generates "1.jpg" to "4659.jpg"

# Shuffle and split
random.seed(42)  # Ensures reproducibility
random.shuffle(all_images)

split_ratio = 0.8  # 80% training, 20% testing
split_index = int(len(all_images) * split_ratio)

train_images = all_images[:split_index]
test_images = all_images[split_index:]

# Move images
for img in train_images:
    shutil.copy(os.path.join(source_folder, img), os.path.join(train_folder, img))

for img in test_images:
    shutil.copy(os.path.join(source_folder, img), os.path.join(test_folder, img))

print("Dataset successfully split into training and testing sets!")