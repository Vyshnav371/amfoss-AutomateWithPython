import os,shutil
from pathlib import Path
ext=input("enter extension")
a=input('Enter path of folder to search')
p=Path(a)
if ext[0]!='.':
    ext='.'+ext
newfolder=ext[1:]+'_Files'
os.makedirs(p/newfolder)
print()
for folder,subfolder,files in os.walk(p):
    for filename in files:
        if filename.endswith(ext):
            try:
                shutil.move(os.path.join(folder,filename),p/newfolder)
            except:
                continue
        else:
            continue
'''/home/vyshnav/Desktop/Python'''
        
    
    
