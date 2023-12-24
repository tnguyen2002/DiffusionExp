from PIL import Image
import os

def resize_and_rename_images(input_folder, output_folder, prefix):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input directory
    files = os.listdir(input_folder)

    # Loop through all files in the input directory
    for index, file in enumerate(files):
        try:
            # Construct the full file path
            input_file_path = os.path.join(input_folder, file)

            # Open the image
            with Image.open(input_file_path) as img:
                # Resize the image
                img = img.resize((512, 512))

                # Define new filename
                new_filename = f"{prefix}_{index}.png"

                # Save the resized image in the output folder
                img.save(os.path.join(output_folder, new_filename))

        except IOError:
            print(f"Error processing file: {file}")

# Example usage
resize_and_rename_images('/Users/tnguyen/Documents/lolify/Demon_Slayer_Images', '/Users/tnguyen/Documents/lolify/demon_images512', 'DemonSlayer')
