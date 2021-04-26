import os
import shutil

OUT_FOLDER = "out"
M_VAR = 1.00229526


def do_replace(i, dots=False):
    with open(i) as f:
        if dots:
            content = f.read().replace(".", ",")
        else:
            content = f.read().replace(",", ".")

    if i.endswith(".dat"):
        lines = content.splitlines()
        if lines[0].startswith("X-Axis"):
            lines.pop(0)

        new_lines = list()
        for line in lines:
            x, y = line.split()
            x_new = float(x) * M_VAR
            new_lines.append(f"{x_new}\t{y}")

        content = "\n".join(new_lines)

    with open(f"{OUT_FOLDER}{os.sep}{i}", "w") as f:
        f.write(content)


def main():
    if os.path.isdir(OUT_FOLDER):
        shutil.rmtree(OUT_FOLDER)
    os.mkdir(OUT_FOLDER)

    for i in os.listdir():
        if i.endswith((".TXT", '.txt')):
            dots = True
        else:
            dots = False

        if i.endswith((".TXT", '.txt', '.dat')):
            do_replace(i, dots=dots)
