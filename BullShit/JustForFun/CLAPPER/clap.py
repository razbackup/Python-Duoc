import shutil, os
import trashCodeBase as trash
#from clappers import clapper1 #Main clap
#CLAPPERS
#from clappers import clapper10, clapper11, clapper12, clapper13, clapper14, clapper15, clapper16, clapper17, clapper18, clapper19, clapper2, clapper20, clapper21, clapper22, clapper23, clapper24, clapper25, clapper26, clapper27, clapper28, clapper29, clapper3, clapper30, clapper31, clapper32, clapper33, clapper34, clapper35, clapper36, clapper37, clapper38, clapper39, clapper4, clapper40, clapper41, clapper42, clapper43, clapper44, clapper45, clapper46, clapper47, clapper48, clapper49, clapper5, clapper6, clapper7, clapper8, clapper9
path,toGB,cont,folder=str(input("Folder: ")),9.31*10**-10,1,"CLAP"
RUTE = os.path.join(path,folder)
try:
    os.mkdir(RUTE)
except FileExistsError:
    RUTE = False
key = path + f"/{folder}"
while True:
    os.system("cls")
    disk = shutil.disk_usage(path)
    print(f"""
    Total: {round(disk.total*toGB,1)} GB
    Free: {round(disk.free*toGB,1)} GB
    Used: {round(disk.used*toGB,3)} GB
    
    SEED: {cont}
        """)
    cont+=1
    trash.trash(key)
    if disk.used >= disk.total:
        break
    else:
        continue
