from pathlib import Path
import os,shutil
a=input("Enter path to folder")
p=Path(a)
for folder,subfolder,files in os.walk(p):
    for filename in files:
        if os.path.getsize(os.path.join(folder,filename))>1000000:
            size=os.path.getsize(os.path.join(folder,filename))
            print(os.path.abspath(os.path.join(folder,filename)),'size=',size)
