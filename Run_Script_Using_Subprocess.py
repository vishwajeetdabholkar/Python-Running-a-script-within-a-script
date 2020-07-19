import subprocess
print("Enetr one numebr to pass as arugment")

x = input()

subprocess.call(['python', 'fibonacci.py', x])
