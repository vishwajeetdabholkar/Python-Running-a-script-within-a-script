# Python-Running-a-script-within-a-script
Python code to run a python script with arguments from another script

Following example contains two python prorgams:
1. Fobonacci.py
2. Run_Script_Using_Subprocess.py

First script has a simple code to generate the fionacci series for provided range.
This script accepts input via commadn line argumnet
The arguments that are given after the name of the program in the command line shell 
of the operating system are known as Command Line Arguments. 
In my example I have shown it using sys.argv 

there are otherways to use command line argumets as well 
you can find them here: https://www.tutorialspoint.com/python/python_command_line_arguments.htm

Second script will run the Fibonacci.py script with argumets as user input.
We are using Subprocess module to achieve it.

## About Subprocess

The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
to execute or a code from subprocess, we use subprocess.call() method.
its syntax is:
subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
