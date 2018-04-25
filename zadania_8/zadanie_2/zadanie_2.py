import subprocess

out = subprocess.check_output(["mkdir -p K1/K2 K1/K3/K4 K5/K6"], shell=True)
print(out)
