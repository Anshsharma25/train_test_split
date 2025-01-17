import os

# Define paths
labels_folder = r"E:\collge assignment\yourlabels"  # Path to the labels folder

# List all label files
label_files = [f for f in os.listdir(labels_folder) if f.endswith('.txt')]

# Iterate over each label file
for label_file in label_files:
    label_filepath = os.path.join(labels_folder, label_file)

    # Read the content of the label file
    with open(label_filepath, 'r') as file:
        lines = file.readlines()

    # Check and modify the class label in each line
    modified_lines = []
    for line in lines:
        # Split the line into components (assuming the format is: class x_center y_center width height)
        components = line.strip().split()

        # Change any class to '0'
        components[0] = '0'  # Change the class label to '0'

        # Rebuild the line with the updated class label
        modified_line = ' '.join(components) + '\n'
        modified_lines.append(modified_line)

    # Save the modified lines back to the file
    with open(label_filepath, 'w') as file:
        file.writelines(modified_lines)

    print(f"Updated {label_file}: Changed all classes to '0'.")

print("Class renaming completed.")
