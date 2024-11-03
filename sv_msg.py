"""
COMP.CS.100 Programming 1
Code Template
"""
def read_message():
    '''This function takes the input as strings and capatilize'''
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    #print(lines)
    #text = '\n'.join(lines)
    #text=text.upper()
    #text=list(text)
    #print(type(text))
    return lines
def main():
    print("Enter text rows to the message. Quit by entering an empty row.")

    msg=read_message()
    msg= '\n'.join(msg)
    msg = msg.upper()



    print(f"The same, shouting:\n{msg}")


if __name__ == "__main__":
    main()
