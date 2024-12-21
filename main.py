import subprocess

for i in range(1, 11):
    filename = f'P{i}.py'
    try:
        subprocess.run(['python', filename], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {filename}: {e}")