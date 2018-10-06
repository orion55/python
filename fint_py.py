import os

findDir = "main"
fullDir = os.path.dirname(__file__) + '/' + findDir

resultname = "result.txt"
fullResultName = os.path.dirname(__file__) + '/' + resultname


def walk(fullDir):
    py_dirs = set()
    for root, dirs, files in os.walk(fullDir):
        for file in files:
            if file.endswith('.py'):
                py_dirs.add(os.path.join(root).replace(os.path.dirname(__file__) + '/', '').replace("\\", "/"))
    return sorted(py_dirs)


if not os.path.isdir(fullDir):
    exit(-1)

lines = walk(fullDir)

outF = open(fullResultName, "w")
outF.write("\n".join(lines))
outF.close()

print('Ok!')