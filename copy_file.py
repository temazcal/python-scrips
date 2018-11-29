import os
import sys

# Read an Copy to new file Loop
originalFile = input('# What file would you like to copy? :')

if os.path.isfile(originalFile) == True:
    print('# Great!,  We will use this file! ')

else:
    print('# Sorry! File {} does not exist!!'.format(originalFile))
    sys.exit()

newFileName = input('# Type name for new copy! ')

f = open(originalFile, 'r')
f.seek(0)
fileData = f.read()
f.close()

f = open(newFileName, 'w')
f.write(fileData)
f.close()
print(newFileName)