from os import path, listdir, rename, system
from sys import argv

#--setup--
desktop_dir = path.join(path.expanduser('~'), 'Desktop') #linux and mac only
imgs_dir = path.join(desktop_dir, 'imgs') #your screenshots folder
dirlist = listdir(desktop_dir) #list all the files in your desktop

nofiles = True
count = 0

def checker(_str): #adjust the condition for your case
	if _str.endswith('.png') and 'screen shot' in _str.lower(): return True
	else: return False

for i in dirlist:
	if checker(i):
		nofiles = False
		count += 1
		file_path = path.join(desktop_dir, i);
		new_file_path = path.join(imgs_dir, i)
		rename(file_path, new_file_path) #move the file to its new place

if nofiles:
	message = "no screenshots on your desktop."
	system("say \"{}\"".format(message)) if '-v' in argv else print(message)

else:
	message = "{} screenshots are cleared from your desktop, have a nice day.".format(count)
	system("say \"{}\"".format(message)) if '-v' in argv else print(message)