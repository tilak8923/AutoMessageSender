import pyautogui
import pyperclip
import time

def send_messages_from_file(file_path, link, count):
    delay=1
    try:
        # File se messages read karo
        with open(file_path, "r") as file:
            messages = [line.strip() for line in file if line.strip()]  # Blank lines ignore karo
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

            pyautogui.hotkey("command", "v")  
            pyautogui.press("enter")  
            time.sleep(delay)  

        pyautogui.typewrite(f"{count}")
        pyautogui.press("enter") 

        print(f"All messages from {file_path} sent successfully!")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

file = "file.txt"
# You Can Add more files here


text = ""
# text that you want to send with each message , let it be empty if you don't want to send any text 


send_messages_from_file(file, text , 1)