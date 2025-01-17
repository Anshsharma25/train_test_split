import os

# Define paths
images_folder = r"E:\collge assignment\garbage\roboarm.v1i.yolov8\train\images"  # Path to the images folder
labels_folder = r"E:\collge assignment\garbage\roboarm.v1i.yolov8\train\labels"  # Path to the labels folder

# List all image and label files
image_files = sorted([f for f in os.listdir(images_folder) if f.endswith(('.jpg', '.png', '.jpeg'))])
label_files = sorted([f for f in os.listdir(labels_folder) if f.endswith('.txt')])

# Ensure the number of image and label files match
if len(image_files) != len(label_files):
    print(f"Warning: The number of image files ({len(image_files)}) does not match the number of label files ({len(label_files)}).")

# Renaming images and labels to a consistent format like image_1.jpg, image_1.txt, image_2.jpg, image_2.txt, etc.
for i, (image_file, label_file) in enumerate(zip(image_files, label_files), 1):
    # Create the new base filename (e.g., image_1)
    new_base_filename = f"image_pill{i}"

    # Rename image files
    old_image_filepath = os.path.join(images_folder, image_file)
    new_image_filename = f"{new_base_filename}{os.path.splitext(image_file)[1]}"  # Retain the original image extension
    new_image_filepath = os.path.join(images_folder, new_image_filename)

    # Rename the image file
    print(f"Renaming image file {image_file} to {new_image_filename}")
    os.rename(old_image_filepath, new_image_filepath)

    # Rename label files
    old_label_filepath = os.path.join(labels_folder, label_file)
    new_label_filename = f"{new_base_filename}.txt"  # Rename label to match image (e.g., image_1.txt)
    new_label_filepath = os.path.join(labels_folder, new_label_filename)

    # Rename the label file
    print(f"Renaming label file {label_file} to {new_label_filename}")
    os.rename(old_label_filepath, new_label_filepath)

print("Renaming completed.")
