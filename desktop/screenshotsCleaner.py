import os
import sys

#--setup--
desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop') #linux and mac only
imgs_dir = os.path.join(desktop_dir, 'imgs') #your screenshots folder
listdir = os.listdir(desktop_dir) #list all the files in your desktop

nofiles = True
count = 0

for i in listdir:
	if i.endswith('.png') and 'screen shot' in i.lower(): #adjust the condition for your case
		nofiles = False; count += 1
		file_path = os.path.join(desktop_dir, i); new_file_path = os.path.join(imgs_dir, i)
		os.rename(file_path, new_file_path) #move the file to its new place

if nofiles:
	if '-v' in sys.argv:
		os.system("say \"no screenshots on your desktop.\"") #mac only
	else:
		print("no screenshots on your desktop.")

else:
	if '-v' in sys.argv:
		os.system("say {} screenshots are cleared from your desktop, have a nice day.".format(count)) #mac only
	else:
		print('{} screenshots are cleared from your desktop, have a nice day.'.format(count))


'''for i in os.listdir(os.path.join(os.path.expanduser('~'), 'Desktop')):
	if i.endswith('.png') and 'screen shot' in i.lower():
		os.rename(os.path.join(os.path.expanduser('~'), 'Desktop', i), os.path.join(os.path.expanduser('~'), 'Desktop', 'imgs',  i))
'''
#print(sys.argv)
