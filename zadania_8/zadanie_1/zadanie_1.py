import subprocess

out = subprocess.check_output(["g++ -o plik plik.cpp"], shell=True)
out2 = subprocess.check_output(["./plik"], shell=True)
print(out)
print(out2)
