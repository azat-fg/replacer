import os
import shutil

OUT_FOLDER = "out"


def do_replace(i, pop_first=False, dots=False):
    with open(i) as f:
        if dots:
            content = f.read().replace(".", ",")
        else:
            content = f.read().replace(",", ".")

    if pop_first:
        lines = content.splitlines()
        lines.pop(0)
        content = "\n".join(lines)

    with open(f"{OUT_FOLDER}{os.sep}{i}", "w") as f:
        f.write(content)


def main():
    if os.path.isdir(OUT_FOLDER):
        shutil.rmtree(OUT_FOLDER)
    os.mkdir(OUT_FOLDER)

    for i in os.listdir():
        if i.endswith(".dat"):
            do_replace(i, pop_first=True)
        elif i.endswith((".TXT", '.txt')):
            do_replace(i, dots=True)
