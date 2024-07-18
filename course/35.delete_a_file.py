# delete a file

import os
import shutil

path = "35.test.txt"

try:
    # os.remove("D:\\git hub\\Practice-Python\\course\\35.test.txt")
    # os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + "was deleted")
