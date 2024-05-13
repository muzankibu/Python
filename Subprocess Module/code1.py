import subprocess

result = subprocess.run(["python", "test5.1.py"], shell=True, capture_output=True, text=True, input="Mta\n")

print(result.stdout)
