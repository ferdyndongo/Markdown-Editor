formatter = ["plain", "bold", "italic", "header", "link", "inline-code", "line-break", "ordered-list", "unordered-list", "new-line"]
commands = ["!help", "!done"]


def h():
    return f"""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\nSpecial commands: !help !done"""


def header():
    level = int(input("-Level:"))
    if level not in range(1, 7):
        print("The level should be within the range of 1 to 6")
        level = int(input())
    text = input("-Text:")
    return f"{'#' * level} {text}\n"


def plain():
    text = input("-Text:")
    return text


def link():
    label = input("- Label:")
    address = input("URL:")
    return f"[{label}]({address})"


def bold():
    text = input("-Text:")
    return f"**{text}**"


def italic():
    text = input("-Text:")
    return f"*{text}*"


def inline_code():
    text = input("-Text:")
    return f"`{text}`"


def line_break():
    return f"\n"


def new_line():
    return f"\n"


def error():
    return "Unknown formatting type or command. Please try again"


def item_list(text):
    num = int(input("- Number of rows:"))
    while num < 1:
        print("The number of rows should be greater than zero")
        num = int(input("- Number of rows:"))
    rows = ""
    for n in range(1, num + 1):
        item = input(f"- Row #{n}:")
        if text == "ordered-list":
            rows += "".join(f"{n}. {item}\n")
        elif text == "unordered-list":
            rows += "".join(f"* {item}\n")
    return rows


def done(rows):
    file = open('output.md', 'w')
    for r in rows:
        file.write(r)
    file.close()


output = []
f = ""
while f != "!done":
    for out in output:
        print(out, end='')
    print()
    f = input("Choose a formatter:")
    if f in formatter:
        if f == "plain":
            output.append(plain())
        elif f == "bold":
            output.append(bold())
        elif f == "italic":
            output.append(italic())
        elif f == "inline-code":
            output.append(inline_code())
        elif f == "link":
            output.append(link())
        elif f == "header":
            output.append(header())
        elif f == "new-line":
            output.append(new_line())
        elif f == "line-break":
            output.append(line_break())
        elif f in ["ordered-list", "unordered-list"]:
            output.append(item_list(f))
    elif f in commands:
        if f == '!help':
            output.append(h())
        else:
            done(output)
            break
    elif f not in formatter or f not in commands:
        output.append(error())
