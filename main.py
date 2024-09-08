import requests
import time

def send_message_to_webhook(webhook_url, message):
    payload = {
        "content": message
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

def main():
    webhook_url = input("Enter the webhook URL: ")
    message = input("Enter your message: ")
    count = int(input("How many times do you want to send the message? "))
    delay = float(input("Enter the delay (in seconds) between messages: "))

    for i in range(count):
        send_message_to_webhook(webhook_url, message)
        print(f"Message {i + 1} sent.")
        time.sleep(delay)

if __name__ == "__main__":
    main()
