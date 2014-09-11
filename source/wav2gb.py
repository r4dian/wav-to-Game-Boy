#!/usr/bin/env python
import sys, os, subprocess, glob

def conv(files):
	for file in files:
		name, ext = os.path.splitext(file)
		subprocess.call('sox '+file+' "converted/'+name+'.tmp.wav" remix 1,2 rate 1920 gain -n')
		print('sox --i -s "converted/'+name+'.tmp.wav"')
		samples = int(subprocess.check_output('sox --i -s "converted/'+name+'.tmp.wav"'))

		if samples <= 65504:
			extra = samples % 32
			if extra == 0:
				subprocess.call('sox "converted/'+name+'.tmp.wav" -b 8 -e un "converted/'+name+'.raw"')
			else:
				print('sox "converted/'+name+'.tmp.wav" -b 8 -e un "converted/'+name+'.raw" pad '+str(32-extra)+'s@'+str(samples)+'s')
				subprocess.call('sox "converted/'+name+'.tmp.wav" -b 8 -e un "converted/'+name+'.raw" pad '+str(32-extra)+'s@'+str(samples)+'s')
		else:
			print("The downsampled. mono "+name +" is still too long at "+str(samples)+" samples. Converted the 1st 65504 samples only.")
			subprocess.call('sox "converted/'+name+'.tmp.wav" -b 8 -e un "converted/'+name+'.raw" trim 0 65504s')
	for f in glob.glob('converted/*.tmp.wav'):
	 	os.unlink (f)


if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("""Usage: python wav2gb.py file1 file2 ...
or drag & drop files onto the .exe""")
		input("Press Enter to continue...")
		sys.exit()
	subprocess.call('mkdir converted', shell=True)
	conv(sys.argv[1:])
	input("Press Enter to close...")
	sys.exit()

# for playback:
# sox -c 1 -b 8 -e un -r 1920 converted\*.wav.raw -d