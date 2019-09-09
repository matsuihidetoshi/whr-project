import os
import sys
import platform
import subprocess

def main():
    typ = "invalid"
    opr = "invalid"
    
    while (typ != "f") and (typ != "d"):
        print("file or dir(f/d):")
        typ = input().strip()

    if typ == "f":
        while (opr != "n") and (opr != "c"):
            print("name or content(n/c):")
            opr = input().strip()
    
    print("path:")
    path = input().strip()

    print("keyword:")
    kwd = input().strip()

    print(
        "\npath:" + path
        + "\ntype:" + typ
        + "\noperation:" + opr
        + "\nkeyword:" + kwd
        + "\nos:" + platform.system())

    if typ == "f":
        if opr == "n":
            res = subprocess.run(
                ["find", os.path.expanduser(path), "-type", typ, "-name", "*" + kwd + "*"], stdout=subprocess.PIPE
                )
            sys.stdout.buffer.write(res.stdout)
        else:
            res = subprocess.run(
                ["grep", kwd, "-rl", os.path.expanduser(path)], stdout=subprocess.PIPE
                )
            sys.stdout.buffer.write(res.stdout)
    else:
        res = subprocess.run(
            ["find", os.path.expanduser(path), "-type", typ, "-name", "*" + kwd + "*"], stdout=subprocess.PIPE
            )
        sys.stdout.buffer.write(res.stdout)