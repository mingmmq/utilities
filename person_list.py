import os

if __name__ == '__main__':
    index = []
    with open("Train/pos.lst") as f:
        for file in f.readlines():
            index.append(os.path.basename(file).split(".")[0])

    with open("Train/person.txt", "w") as f:
        for i in index:
            f.write(i + "\n")
