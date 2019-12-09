WIDTH = 80
def center(s, width):
    if width < len(s):
        return s
    spaces = (width - len(s)) // 2
    result = " " * spaces + s

    return result
def main ():
    print(center ("A Famous Story", WIDTH))
    print(center ("by:", WIDTH))
    print(center ("Someone Famous", WIDTH))
    print ()
    print("Once upon a time...")

main()