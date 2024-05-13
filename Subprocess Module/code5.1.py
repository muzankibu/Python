# subprocess in python

import subprocess

p = subprocess.Popen("python test5.1.py",
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True, text=True)
out, err = p.communicate(input="Meta\n")
if p.returncode != 0:
    print(out)
    print(err)