from PIL import Image
import os

def resize_images(folder_path, aspect_ratio):
    """
    Resize all image files in a folder to a specific aspect ratio.
    :param folder_path: str, the path to the folder containing the image files
    :param aspect_ratio: float, the desired aspect ratio
    """
    # Create a new folder named "PICNEW" within the original folder
    new_folder_path = os.path.join(folder_path, 'PICNEW')
    os.makedirs(new_folder_path, exist_ok=True)

    # Scan for all .jpg files in the folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if file.endswith('.jpg') and os.path.isfile(file_path):
            try:
                # Open the image
                image = Image.open(file_path)

                # Calculate the new width and height based on the aspect ratio
                width, height = image.size
                new_width = int(height * aspect_ratio)
                new_height = height

                # Resize the image while maintaining the original aspect ratio
                image = image.resize((new_width, new_height), Image.ANTIALIAS)

                # Construct the new filename by appending "_change.jpg" to the original filename
                new_filename = os.path.splitext(file)[0] + '_change.jpg'

                # Save the resized image in the new folder
                new_file_path = os.path.join(new_folder_path, new_filename)
                image.save(new_file_path)

                print(f'Resized image saved as {new_file_path}')

                # Delete the original image file
                os.remove(file_path)
                print(f'Original image file {file_path} deleted')
            except Exception as e:
                print(f'Error processing file {file}: {e}')

    print(f'All images resized and saved in {new_folder_path}, original images deleted from {folder_path}')

# Example usage:
folder_path = 'Ig_model/Sherni/Pic'  # Replace with the path to your folder containing the image files
aspect_ratio = 0.8  # Replace with the desired aspect ratio
resize_images(folder_path, aspect_ratio)
