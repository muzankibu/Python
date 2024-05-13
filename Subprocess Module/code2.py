import subprocess

result = subprocess.run(["python", "test1.py"], capture_output=True, text=True)

print(result.stdout)
print(result.stderr)
