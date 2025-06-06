import sys
import pyautogui
import pyperclip
import time

# it automatically detects the paste hotkey based on the platform
if sys.platform == "darwin":
    paste_hotkey = ["command", "v"]
elif sys.platform == "win32":
    paste_hotkey = ["ctrl", "v"]
else:
    paste_hotkey = ["ctrl", "v"]

def send_messages_from_file(file_path, text, count):
    delay=1
    try:
        # Read msgs from file
        with open(file_path, "r") as file:
            messages = [line.strip() for line in file if line.strip()]  # for ignoring blank lines
            print("Messages Read from File:", messages)
        if not messages:
            print(f"No messages found in {file_path}.")
            return

        print(f"Place your cursor in the chat box for messages from {file_path}. Starting in 5 seconds...")
        time.sleep(5)

        for msg in messages:
            full_text = f"{msg}\n{text}"                          # Message + text combine
            pyperclip.copy(full_text)  
            time.sleep(0.1)  

            pyautogui.hotkey(*paste_hotkey)
            pyautogui.press("enter")  
            time.sleep(delay)  

        pyautogui.typewrite(f"{count}")
        pyautogui.press("enter") 

        print(f"All messages from {file_path} sent successfully!")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

# provide the name of the files and texts(optional you can leave it blank) in a list of dictionaries
data = [
    {"file": "file1.txt", "text": "hello_world"},
    {"file": "file2.txt", "text": "https://example.com"},
]   
# you can add more files and links as needed

# Iterate through the list of dictionaries and call sendMsg for each item
for i, item in enumerate(data, start=1):
    send_messages_from_file(item["file"], item["text"], i)
    print(f"Finished processing {item['file']}.")
