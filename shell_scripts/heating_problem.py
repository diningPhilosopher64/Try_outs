import fileinput
import os 



for line in fileinput.input('/etc/default/grub',inplace=True):
	print line.replace('GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"','GRUB_CMDLINE_LINUX_DEFAULT="quiet splash intel_pstate=enable"')



os.system('sudo update-grub')	