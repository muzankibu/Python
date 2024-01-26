import subprocess

result = subprocess.run(["python", "test2.py"], capture_output=True, text=True)

print(result.stdout)
