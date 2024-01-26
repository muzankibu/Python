import subprocess

try:

    output = subprocess.check_output(["python", "--version"], text=True)

    print(output)

except subprocess.CalledProcessError as e:

    print(f"Command failed with return code {e.returncode}")
