Wav to Game Boy converter
=========================

Batch convert sounds files to 8-bit unsigned raw files for use the [Paragon5 tracker](https://rv6502.ca/post/2014/07/17/game-boy-tracker-replay-routines-released/) (AKA Beyond Tracker, AKA ...)
Converts anything your version of sox can read.

Requirements: A version of [sox.exe](http://sourceforge.net/projects/sox/files/sox/14.4.1/sox-14.4.1a-win32.zip/download) (and its accompanying zlib1.dll) in the same directory.

Use:
```bat
python wav2gb.py file1.ogg file2.wav ....etc
```

Windows .exe file included for people who can't/won't install Python. Just drag & drop a bunch of sound files onto the .exe file.

Sounds are padded up to a multiple of 32 samples for use with the 3rd channels X: play long wave command.

Currently if the sound is over 65504 samples (about 34 seconds) the remainder is lost. We could auto slice into multiple raw files, but due to how tempo works in the tracker, it'd be hard to line the slices up exactly. I think it's better if a wav editor is used to cut the sample into shorter samples on the beat.