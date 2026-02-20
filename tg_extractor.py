import requests
import sys

def print_banner():
    print("="*60)
    print(" 🕵️‍♂️ TG-Forensic-Extractor | C2 Infrastructure Analysis ")
    print("="*60)

def main():
    print_banner()
    
    # 1. Gather Input
    token = input("\n[?] Enter the compromised Bot Token: ").strip()
    chat_id = input("[?] Enter Target Chat ID (Leave blank to auto-detect from recent logs): ").strip()

    print("\n[*] Initializing forensic extraction...")

    # 2. Extract Bot Identity
    me_resp = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()
    if not me_resp.get("ok"):
        print("[-] Error: Invalid Bot Token or Bot has been terminated by Telegram.")
        sys.exit()

    bot = me_resp['result']
    print(f"\n[+] Bot Username : @{bot.get('username')}")
    print(f"[+] Bot Name     : {bot.get('first_name')}")
    print(f"[+] Bot ID       : {bot.get('id')}")

    # 3. Check Recent Updates (Queue) for auto-detection and last message
    updates_resp = requests.get(f"https://api.telegram.org/bot{token}/getUpdates").json()
    last_message = None
    
    if updates_resp.get("ok") and len(updates_resp['result']) > 0:
        updates = updates_resp['result']
        last_update = updates[-1] # Grab the very last item in the queue
        
        if 'message' in last_update:
            last_message = last_update['message']
            
            # Auto-detect chat ID if the user left it blank
            if not chat_id:
                chat_id = str(last_message['chat']['id'])
                print(f"[+] Auto-detected Chat ID from recent traffic: {chat_id}")

    # 4. Extract Target Profile / Group Information
    if chat_id:
        chat_resp = requests.get(f"https://api.telegram.org/bot{token}/getChat?chat_id={chat_id}").json()
        if chat_resp.get("ok"):
            chat = chat_resp['result']
            chat_type = chat.get('type').capitalize()
            chat_title = chat.get('title', chat.get('first_name', 'Unknown'))
            
            print(f"\n[+] Target {chat_type} Name: {chat_title}")
            
            if chat.get('description'):
                print(f"[+] Description: {chat.get('description')}")
            
            # Attempt to pull Administrators/Members
            admin_resp = requests.get(f"https://api.telegram.org/bot{token}/getChatAdministrators?chat_id={chat_id}").json()
            if admin_resp.get("ok"):
                print("[+] Extracted Group Administrators / Active Members:")
                for admin in admin_resp['result']:
                    user = admin['user']
                    username = f"@{user.get('username')}" if user.get('username') else "No Username"
                    print(f"    - {user.get('first_name', 'Unknown')} ({username}) | ID: {user.get('id')}")
            else:
                print("[-] Note: Bot lacks administrative privileges to view the member list.")
        else:
            print(f"\n[-] Could not retrieve metadata for Chat ID {chat_id}. The bot may have been kicked.")

    # 5. Extract Last Message Content
    if last_message:
        print(f"\n[+] Last Intercepted Message ID: {last_message.get('message_id')}")
        text_content = last_message.get('text', '[Non-text payload / Media / Document]')
        print(f"[+] Message Payload: {text_content}")
    else:
        print("\n[-] No recent messages found in the bot's update queue.")

if __name__ == "__main__":
    main()
