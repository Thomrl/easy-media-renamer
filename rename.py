# script that goes through a directory and removes everything after e.g S03E01 or 2020
import os, shutil, re, sys

#Directory
path = sys.argv[1]
            
def rename(type):
    mo = sE.search(file)
    pattern = mo.group()
    cake = re.split((pattern), file)[0]
    dotsremoved = cake.replace(".", " ")
    titlefied = str.title(dotsremoved)
    yearOrEp = str.title(pattern)
    if type == "movie":
        yearOrEp = "("+yearOrEp+")"
    print(file + " is being renamed to: " + titlefied+yearOrEp+".mkv")
    os.rename(file, titlefied+yearOrEp+".mkv")

if os.path.exists(path):
    os.chdir(path)
    for file in os.listdir():
        if re.search(r"\w\d\d\w\d\d", file):
            if file.endswith(".mkv"):
                sE = re.compile(r"(\w\d\d\w\d\d)")
                rename("series")
        if re.search(r"\d\d\d\d", file):
            if file.endswith(".mkv"):
                sE = re.compile(r"(\d\d\d\d)")
                rename("movie")

