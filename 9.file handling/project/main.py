from pathlib import Path
def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}:{items}")
def createfile():
    readfileandfolder()

print("press 1 to create file")
print("press 2 to reading file")
print("press 3 to updating file")
print("press 4 to deleting file ")
check=int(input("please enter your response--"))