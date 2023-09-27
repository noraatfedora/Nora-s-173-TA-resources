import os
directory = input('enter path') 
dir_list = os.listdir(directory)
dir_list.sort()
print('Files in path: ')
print(dir_list)

start_str = 'CSC173 Project 1_'
username = ''
new_folder_path = ''
for file_name in dir_list:
    current_username = file_name[len(start_str):file_name.index('_attempt')]
    if not username == current_username:
       username = current_username 
       new_folder_path = directory + "/" + username
       if not os.path.exists(new_folder_path):
           os.makedirs(new_folder_path)
    os.replace(directory + '/' + file_name, new_folder_path + '/' + file_name)
