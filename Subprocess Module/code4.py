import subprocess

result = subprocess.run(["python", "file_donot_exist.py"], capture_output=True, text=True, check=False) #switch between  check=True & check=False for better understanding

print(result.stdout)

print(result.stderr)
