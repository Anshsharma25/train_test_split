import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
images_folder = r"E:\augumentedimages\augumentedimages"  # Path to the images folder
labels_folder = r"E:\augumentedlabels\augumentedlabels"  # Path to the labels folder
output_dir = r"E:\dataset_split"  # Path to save the split datasets

# Create train, validation, and test folders
train_images_dir = os.path.join(output_dir, "train/images")
train_labels_dir = os.path.join(output_dir, "train/labels")
val_images_dir = os.path.join(output_dir, "valid/images")
val_labels_dir = os.path.join(output_dir, "valid/labels")
test_images_dir = os.path.join(output_dir, "test/images")
test_labels_dir = os.path.join(output_dir, "test/labels")
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)
os.makedirs(test_images_dir, exist_ok=True)
os.makedirs(test_labels_dir, exist_ok=True)

# List all images and corresponding labels
image_files = sorted([f for f in os.listdir(images_folder) if f.endswith(('.jpg', '.png', '.jpeg'))])
label_files = sorted([f for f in os.listdir(labels_folder) if f.endswith('.txt')])

# Ensure images and labels match
assert len(image_files) == len(label_files), "Mismatch between images and labels."
assert all(os.path.splitext(img)[0] == os.path.splitext(lbl)[0] for img, lbl in zip(image_files, label_files)), \
    "Image and label filenames do not match."

# Split the dataset: 70% train, 20% validation, 10% test
train_images, temp_images, train_labels, temp_labels = train_test_split(
    image_files, label_files, test_size=0.3, random_state=42  # 30% for validation and test
)

val_images, test_images, val_labels, test_labels = train_test_split(
    temp_images, temp_labels, test_size=0.33, random_state=42  # 33% of 30% for test, 67% for validation
)

# Copy files to respective folders
def copy_files(file_list, source_folder, dest_folder):
    for file in file_list:
        shutil.copy(os.path.join(source_folder, file), os.path.join(dest_folder, file))

copy_files(train_images, images_folder, train_images_dir)
copy_files(val_images, images_folder, val_images_dir)
copy_files(test_images, images_folder, test_images_dir)
copy_files(train_labels, labels_folder, train_labels_dir)
copy_files(val_labels, labels_folder, val_labels_dir)
copy_files(test_labels, labels_folder, test_labels_dir)

print(f"Train-Validation-Test split completed.")
print(f"Training images: {len(train_images)} | Validation images: {len(val_images)} | Test images: {len(test_images)}")
print(f"Dataset saved in {output_dir}")
