with open("checkmate.py", "r", encoding="utf-8") as file:
    exec(file.read())


def main():
    board = """\
R...
.K..
..P.
....\
"""

    checkmate(board)

if __name__ == "__main__":
    main()
