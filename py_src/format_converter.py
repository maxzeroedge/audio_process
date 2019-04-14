import os, subprocess, sys

def convert_to_wav(inFile):
    outFile = inFile.replace('.mp3', '.wav')
    if os.path.isfile(outFile):
        os.remove(outFile)
    cmd = 'ffmpeg -i {} {}'.format(inFile, outFile).split(' ')
    with subprocess.Popen( args=cmd, stdout=subprocess.PIPE ) as proc:
        print(proc.stdout.read())


if __name__=="__main__":
    args = sys.argv
    convert_to_wav(args[1])