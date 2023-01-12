import os
class SystemDriveFinder:
    def __init__(self):
        pass
    def find_drives(self):
        print("This is to find out  file")
        drives = []
        for x in range(65,91):
            if os.path.exists(chr(x)+":"):
                drives.append(chr(x))
        return drives
if __name__=='__main__':
    obj=SystemDriveFinder()
    print(obj.find_drives())
