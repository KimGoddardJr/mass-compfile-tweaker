import os

out_folder = 'OUT'


for folder in os.listdir(out_folder):
    if 'BACKUP' not in folder:
        folder_path=os.path.join(out_folder,folder)    
        if os.path.isdir(folder_path):
            for stared_folder in os.listdir(folder_path):
                stared_folder_path = os.path.join(folder_path,stared_folder)
                if os.path.isdir(stared_folder_path):
                    for img_folder in os.listdir(stared_folder_path):
                        img_folder_path = os.path.join(stared_folder_path,img_folder)
                        if os.path.isdir(img_folder_path):
                            for img in os.listdir(img_folder_path):

                                new_img_name = "{}_{}".format(img_folder,img)
                                img_path = os.path.join(img_folder_path,img)
                                print(new_img_name)
                                os.rename(img_path,new_img_name)

def your_amazing_function():
    print('stupid')

def recursive_search(folde_path,target_file,your_amazing_function):
    for recursive_folder in os.listdir(folder_path):
        recursive_path = os.path.join(folder_path,recursive_path)
            if os.path.isdir(recursive_path):
                recursive_search(recursive_path,target_file)
            elif os.path.isdir(recursive_path) == False and recursive_path.split('.')[-1] == target_file:
                your_amazing_function