import subprocess
def terminal():
    while True:
        command = input(">>> ")
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if output:
            print(output.decode("utf-8"))
        if error:
            print(error.decode("utf-8"))

if __name__ == "__main__":
    terminal()