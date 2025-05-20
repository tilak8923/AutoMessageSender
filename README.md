## Read Before Use -
# Auto Message Sender 📨

This Python script helps you automatically send multiple messages from a `.txt` file into any chat interface (like WhatsApp Web, Telegram Desktop, etc.) using `pyautogui` and `pyperclip`.

## 🔧 Features

- Read messages from a text file
- Send each message with optional additional text
- Automatically paste and send messages one by one
- Works with any app where you can manually type/paste text

## 🖥️ Requirements

- Python 3.x
- `pyautogui`
- `pyperclip`

Install dependencies:
 - pip install pyautogui pyperclip

## HowToUse

- Add your messages to file.txt (one message per line).
- Edit the text variable in the script if you want to append extra text.

Run the script:
  - python auto_sender.py

- Within 5 seconds, place your cursor in the desired chat box.
- The messages will start sending one by one.

## Customization

- You can add more .txt files and call send_messages_from_file() multiple times.
- You can change the delay between messages by editing the delay variable.

## ⚠️ Disclaimer

- This script simulates keyboard actions. Use it responsibly and only where automated messaging is allowed or with your own accounts.

## 📄 License

- This project is licensed under the MIT License.
