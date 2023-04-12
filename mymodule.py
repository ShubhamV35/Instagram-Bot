from instabot import Bot
import os
import shutil

###################################################################################

def find_folder(foldername):
        
       # Get the current directory
       current_directory = os.getcwd()

       # Walk through the current directory and its subdirectories
       for directorypath,directoryname , filename  in os.walk(current_directory):
             for dir in directoryname:
                    #check if the directory name matches the given foldername
                    if dir == foldername:
                          return os.path.abspath(os.path.join(directorypath,dir))
        # Return None if the folder is not found
       return "Not Found directory of folder"

#################################################################################


def make_txt_file_of_pic(actress_foldername , actress_filename):
    
     # Directory path where the 'Ig_model' folder is located
     directory = 'Ig_model'

     # Creating a list to store the names of the JPG files
     jpg_files = []

    # Traversing through the 'shubham' folder and its subdirectories
     for root, dirs, files in os.walk(os.path.join(directory, actress_foldername, 'pic')):
          for file in files:
                # Checking if the file has a .jpg extension
               if file.endswith('.jpg'):
                     # Appending the file name to the list
                    jpg_files.append(file)


    # Creating a text file to store the file names
     with open(os.path.join(directory, actress_foldername, actress_filename), 'w') as f:
    # Writing the file names to the text file, one file name per line
       f.write('\n'.join(jpg_files))
     return jpg_files
   
#####################################################################################




def do_my_work(actress_foldername , new_photo_id_detail):

    print("enter")
    bot = Bot()
    bot.login(username="",password="")  #Give username and password of your instagram
    PATH = os.path.join("Ig_model", actress_foldername,"Pic")

    # Loop through the list of photos and upload each one
    for photo in new_photo_id_detail:
        bot.upload_photo(photo, caption='#viral #engagement #explorepage #instagram #trending #followers #instagood #followforfollowback')

   #Logout from instagram
    bot.logout()



#############################################################################################


