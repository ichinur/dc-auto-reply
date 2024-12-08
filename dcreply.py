import requests
import random
import time
from colorama import Fore

print("╦╔═╗╦ ╦╦╔╗ ╔═╗╔╦╗")
print("║║  ╠═╣║╠╩╗║ ║ ║ ")
print("╩╚═╝╩ ╩╩╚═╝╚═╝ ╩ ")
print("\n===========================================")
author = "ichi"
print("Author: " + author)
script = "Auto-Reply Discord"
print("Script: " + script)
telegram = "@litbrother"
print("Telegram: " + telegram)

channel_id = input("Masukkan ID channel: ").strip()

with open("massage.txt", "r") as f:
    words = [line.strip() for line in f.readlines()]

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

headers = {
    'Authorization': authorization,
    'Content-Type': 'application/json'
}

def get_channel_slowmode(channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        channel_data = response.json()
        return channel_data.get("rate_limit_per_user", 0)
    else:
        print(Fore.RED + f"Failed to get channel info: {response.status_code} - {response.text}")
        return 0

def fetch_latest_message(channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=1"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        messages = response.json()
        if messages:
            return messages[0]
    return None

def send_reply(channel_id, content, message_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    payload = {
        "content": content,
        "message_reference": {
            "message_id": message_id
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(Fore.GREEN + f"Sent reply: {content}")
    elif response.status_code == 429:
        retry_after = response.json().get("retry_after", 1)
        print(Fore.RED + f"Rate limit hit. Retrying after {retry_after:.2f} seconds...")
        time.sleep(retry_after)
    elif response.status_code == 400:
        print(Fore.RED + f"Invalid message reference: {response.text}")
    else:
        print(Fore.RED + f"Failed to send reply: {response.status_code} - {response.text}")

last_message_id = None
slowmode_duration = get_channel_slowmode(channel_id)

if slowmode_duration > 0:
    print(Fore.YELLOW + f"Slowmode is active with a duration of {slowmode_duration} seconds.")
else:
    print(Fore.GREEN + "No slowmode is currently applied.")

print("Auto-reply bot is running...\n")
while True:
    try:
        latest_message = fetch_latest_message(channel_id)

        if latest_message:
            message_id = latest_message['id']
            author = latest_message['author']['username']
            content = latest_message['content']
            is_bot = latest_message['author'].get('bot', False)
            keywords = ["what", "lv", "bencat"] #Change Keyword Here
            content_lower = content.lower()

            if message_id != last_message_id and not is_bot and any(keyword in content_lower for keyword in keywords):
                print(Fore.CYAN + f"Keyword found in message from {author}: {content}")
                print(Fore.YELLOW + "Waiting for 5 seconds before replying...")
                time.sleep(5)
                reply = random.choice(words)
                send_reply(channel_id, reply, message_id)
                last_message_id = message_id

                if slowmode_duration > 0:
                    print(Fore.YELLOW + f"Waiting for slowmode duration ({slowmode_duration}s) before checking for next messages...")
                    time.sleep(slowmode_duration)

        time.sleep(2)

    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        time.sleep(5)
