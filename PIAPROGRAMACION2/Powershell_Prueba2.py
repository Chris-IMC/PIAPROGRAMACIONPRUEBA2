import subprocess

output = subprocess.run(("powershell", "-Command", "Get-Date"), capture_output=True)
result = output.stdout.decode("utf-8")

print(result)