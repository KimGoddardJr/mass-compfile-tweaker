import os
import difflib
from collections import defaultdict
import glob
import shutil
import json
import fileinput
import subprocess




cur_dir = os.getcwd()

image_folder = os.path.join(cur_dir,'PICTURES_RAW')
out_folder = os.path.join(cur_dir,'OUT')
template_file = 'TEMPLATES/STITCHING_template_JPG.nk'
nuke_files_location = cur_dir

image_groups = os.listdir(image_folder)

with open('JSON/relations.json') as template_file:
            template_paths = json.load(template_file)

type(template_paths)

##create OUT folders

def makedir(folder_name):
            try:
                os.makedirs(folder_name, exist_ok=True)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
                pass

"""
for folder in image_groups:
    out_folder_path = os.path.join(out_folder,folder)
    makedir(out_folder_path)
    out_folders.append(out_folder_path)
"""
## look for all STAR folders in the imagegroups and then look for all PIC folders

for group in image_groups:
    group_path = os.path.join(image_folder,group)
    print(group_path)
    out_folder_path = os.path.join(out_folder,group)
    makedir(out_folder_path)
    #out_folders.append(out_folder_path)
    for stared_folder in os.listdir(group_path):
        if 'STAR-imgs' in stared_folder:
            stared_folder_path = os.path.join(group_path,stared_folder)
            for i,pic in enumerate(os.listdir(stared_folder_path)):
                
                pic_path = os.path.join(stared_folder_path,pic)
                #file_name_base = os.path.basename(str(template_file))
                #file_placing = os.path.join(nuke_files_location,file_name_base)
                shutil.copyfile('TEMPLATES/STITCHING_template_JPG.nk','STITCHING_template_JPG.nk')
                
                name_extension = "{}_{}".format(group,pic)
                new_filename =  "STITCHING_{}.nk".format(name_extension)
                new_filename_path = os.path.join(nuke_files_location, new_filename)
                print(new_filename_path)

                os.rename('STITCHING_template_JPG.nk',new_filename_path)

                ## new paths for pics
                nuke_read_path = 'PICTURES_RAW/{}/STAR-imgs/{}/'.format(group,pic)
                print(nuke_read_path)
                nuke_write_path = 'OUT/{}/STAR-imgs/{}/{}'.format(group,pic,group)
                print(nuke_write_path)
                nuke_file_PATH = '/home/kg/Dropbox/projects/HSLU/360pics/{}'.format(new_filename)
                print(nuke_file_PATH)

                with fileinput.FileInput(new_filename_path, inplace=True, backup='.bak') as file:
                    for line in file:
                        print(line.replace('TEMPLATE_FOLDER/template_subfolder', nuke_read_path), end='')
                        #print(line.replace('OUT/TEMPLATE/example', nuke_write_path), end='')
                        #print(line.replace('/home/kg/Dropbox/projects/HSLU/360pics/TEMPLATES/STITCHING_template_.nk', nuke_file_PATH), end='')
                
                with fileinput.FileInput(new_filename_path, inplace=True, backup='.bak') as file:
                    for line in file:
                        print(line.replace('OUT/TEMPLATE/example', nuke_write_path), end='')

                with fileinput.FileInput(new_filename_path, inplace=True, backup='.bak') as file:
                    for line in file:
                        print(line.replace('/home/kg/Dropbox/projects/HSLU/360pics/TEMPLATES/STITCHING_template_JPG.nk', nuke_file_PATH), end='')
                #open the nuke file 
                #nuke_file = open(new_filename_path,'r')

                
for render_file in os.listdir(cur_dir):
    if render_file.split('.')[-1] == 'nk':
        render_command = "Nuke12.0 --nukex -i --cont --gpu 0 -F 1-1 -xi {}".format(render_file)

        process = subprocess.Popen(render_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()


                        





