import os
import shutil
import random

def split_dataset(source_dir, dest_dir, split_ratio=0.8):
    """Splits dataset into training and testing sets while maintaining directory structure."""
    # Define paths
    scans_dir = os.path.join(source_dir, "scans")
    masks_dir = os.path.join(source_dir, "masks")
    
    train_scans_dir = os.path.join(dest_dir, "train", "scans")
    test_scans_dir = os.path.join(dest_dir, "test", "scans")
    train_masks_dir = os.path.join(dest_dir, "train", "masks")
    test_masks_dir = os.path.join(dest_dir, "test", "masks")
    
    # Create directories
    for folder in [train_scans_dir, test_scans_dir, train_masks_dir, test_masks_dir]:
        os.makedirs(folder, exist_ok=True)
    
    # Process each class in scans
    for tumor_type in os.listdir(scans_dir):
        tumor_path = os.path.join(scans_dir, tumor_type)
        if not os.path.isdir(tumor_path):
            continue
        
        # Get all images in the tumor type folder
        images = sorted(os.listdir(tumor_path))
        random.shuffle(images)  # Shuffle for randomness
        split_idx = int(len(images) * split_ratio)
        
        train_images = images[:split_idx]
        test_images = images[split_idx:]
        
        # Create corresponding subdirectories in train/test sets
        os.makedirs(os.path.join(train_scans_dir, tumor_type), exist_ok=True)
        os.makedirs(os.path.join(test_scans_dir, tumor_type), exist_ok=True)
        
        # Move images and corresponding masks
        for img in train_images:
            shutil.copy(os.path.join(scans_dir, tumor_type, img), os.path.join(train_scans_dir, tumor_type, img))
            shutil.copy(os.path.join(masks_dir, img), os.path.join(train_masks_dir, img))
        
        for img in test_images:
            shutil.copy(os.path.join(scans_dir, tumor_type, img), os.path.join(test_scans_dir, tumor_type, img))
            shutil.copy(os.path.join(masks_dir, img), os.path.join(test_masks_dir, img))
    
    print("Dataset split completed successfully!")

# Example usage
source_folder = "full data set"
destination_folder = "split_dataset"
split_dataset(source_folder, destination_folder, split_ratio=0.8)
