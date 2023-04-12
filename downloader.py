import os
import shutil
from instaloader import Instaloader, Profile

def function_to_download_post(Instagram_Id_name,Actress_Folder_name):

    # Create an Instaloader instance
    L = Instaloader()

    # Load the profile of the Instagram account (replace PROFILE_NAME with the username of the Instagram account you want to download posts from)
    profile = Profile.from_username(L.context, Instagram_Id_name)

    # Download all the posts of the profile
    L.context.log("Downloading posts from profile: {}".format(profile.username))
    for post in profile.get_posts():
        # Download the post and save it to a local file
        L.download_post(post, target=Actress_Folder_name)

    L.context.log("Finished downloading posts.")




def find_folder(foldername):
       # Get the current directory
       current_directory = os.getcwd()
#return os.path.abspath(os.path.join(dirpath, dirname))

       # Walk through the current directory and its subdirectories
       for directorypath,directoryname , filename  in os.walk(current_directory):
             for dir in directoryname:
                    #check if the directory name matches the given foldername
                    if dir == foldername:
                          return os.path.abspath(os.path.join(directorypath,dir))
        # Return None if the folder is not found
       return 0



def make(location_of_actress_post_folder):
    make = os.path.join(location_of_actress_post_folder,"Pic")
    os.makedirs(make)


def send(location_of_actress_post_folder):

    # Create "pic" folder in the same location
    pic_folder_path = os.path.join(location_of_actress_post_folder, 'pic')
    if not os.path.exists(pic_folder_path):
         os.mkdir(pic_folder_path)

    # List all files in the folder
    files = os.listdir(location_of_actress_post_folder)

    # Loop through each file and move image files to "pic" folder
    for file in files:
        # Check if file has a common image file extension
        if file.lower().endswith(('.jpg')):
            # Create source and destination paths
            src = os.path.join(location_of_actress_post_folder, file)
            dst = os.path.join(pic_folder_path, file)
            # Move file to "pic" folder
            shutil.move(src, dst)
            print(f"Moved '{file}' to '{pic_folder_path}'")




def move_to_ig_model_actress_folder(source_folder, destination_folder):
    try:
    # Move the folder to the destination
       shutil.move(source_folder, destination_folder)
       print(f"Folder moved successfully from '{source_folder}' to '{destination_folder}'.")
    except Exception as e:
       print(f"Error occurred while moving folder: {e}")


#User input detail
Instagram_Id_name = input("Enter the username of instagram account.")
Actress_Folder_name = input("Name the folder which you want to create and store all post..")
jpg_files = []


#This is my function call to download the all post from instagram actress
function_to_download_post(Instagram_Id_name , Actress_Folder_name)


#This is my function call to find the location of downloaded instagram actress
location_of_actress_post_folder = find_folder(Actress_Folder_name)

print(location_of_actress_post_folder)

#This is my function to make Pic folder in Actress_Folder_name
make(location_of_actress_post_folder)

#send the all pic from location :- actress_folder_name to Pic folder
send(location_of_actress_post_folder)

#Moving the all pic folder in Mera to Ig model actress folder

source_folder = r'C:\Users\vishw\Downloads\Post\Automation'
destination_folder = r'C:\Users\vishw\Downloads\Post\Automation\Ig_model'
addition = Actress_Folder_name+"\Pic"

source_folder = os.path.join(source_folder,addition)
destination_folder = os.path.join(destination_folder,Actress_Folder_name)

#Moving pic folder to actress folder name
move_to_ig_model_actress_folder(source_folder, destination_folder)

