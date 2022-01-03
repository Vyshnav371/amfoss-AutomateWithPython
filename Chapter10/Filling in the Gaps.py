from pathlib import Path
import os,shutil
a=input("enter path to folder")
p=Path(a)
b=input('enter Prefix: ')
for folder,subfolder,files in os.walk(p):
    for filename in files:
        if filename.startswith(b):
            print('maybe')
    
