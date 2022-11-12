
import glob
import os
import shutil
from zipfile import ZipFile

source_path = '..\source\*'
destination_path = '..\destination'


postfix = [1, 2, 3]

while True :

    source_object = glob.glob(source_path)

    if len(source_object) > 0 :
        for object_path in source_object:
            
            object_name = object_path.split('\\')[-1].split('.')
            file_name = object_path.split('\\')[-1]

            prefix = object_name[0]
            postfix2 = object_name[1]
            if postfix2 == "txt" :
                for item in range(1, len(postfix)+1):
                    filename = prefix + '_' + str(item) + '.' + postfix2
                    fsrc = open(object_path, 'r')
                    lines = fsrc.readlines()
                    selected_lines = lines[0 : (item*10)]

                    if item == 1 :
                        current_dir = os.getcwd()
                        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
                        list_of_dirs = [name for name in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, name))]
                        primary_path_dest = os.path.join(parent_dir, list_of_dirs[0]) 
                        primary_path_server = os.path.join(parent_dir, list_of_dirs[1])
                        primary_path_source = os.path.join(parent_dir, list_of_dirs[2])
                        zip_folder = 'zip_folder'
                        final_path_dest = os.path.join(primary_path_dest, zip_folder)
                        final_path_server = os.path.join(primary_path_server, zip_folder)
                        try:
                            os.mkdir(final_path_server) 
                        except OSError as error:
                            print(error)

                    fdst = open(f"{final_path_server}\{filename}", 'w')
                    fdst.writelines(selected_lines)
                    fsrc.close()
                    fdst.close()
                    
                    shutil.make_archive(final_path_server, 'zip', primary_path_server)
                    shutil.copy(f"{final_path_server}.zip", destination_path)

                    with ZipFile(f"{final_path_dest}.zip", 'r') as zip :
                        zip.extractall(path=primary_path_dest)
                        print("done!")

                os.remove(f"{final_path_server}.zip")
                shutil.rmtree(final_path_server)

            elif postfix2 == "py" :
                try :
                    exec(open(f"{primary_path_source}\{file_name}").read())
                except Exception as exc:
                    print(f"Error message : {exc}")

            os.remove(object_path.split('/')[-1])

