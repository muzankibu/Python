#problamatic
import subprocess

result = subprocess.run([r"C:\Users\Soleman Hossain\AppData\Local\Programs\Python\Python310\python.exe", "-c", "print('This is directly from a subprocess.run() function')"], capture_output = True, text = True)

print(result.stdout)

