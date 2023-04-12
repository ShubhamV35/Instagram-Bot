import mymodule


### MAKES SURE YOU KEEP ALL OF THIS FOLDER TO ONE FOLDER NAME Ig_model, its mandatory ###

# All user input detail
actress = "" #enter name of your instagram id not username 


actress_foldername = actress
actress_filename = actress + ".txt"

store_detail_of_folder_location = mymodule.find_folder(actress_foldername)
print("Found folder loction = ",store_detail_of_folder_location)


#MAKE TXT FILE OF EXISTING PIC FOLDER 

photo_id_detail = mymodule.make_txt_file_of_pic(actress_foldername , actress_filename)
print("Done txt file making ")


extra_path_to_be_added_list = 'Ig_model/'+str(actress_foldername)+'/Pic/'

# Loop through the list and concatenate the prefix to each file name
new_photo_id_detail = [extra_path_to_be_added_list + file_name for file_name in photo_id_detail]
print("done adding extra path ")

#Function to upload pics on instagram

mymodule.do_my_work(actress_foldername,new_photo_id_detail)

#mymodule.delete_folder()






