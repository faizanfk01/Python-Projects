import pywhatkit

def get_valid_phone():
    while True:
        phone = input("Enter the phone number (with country code, e.g., +12XXXXXXXXX): ").strip()
        if (phone.startswith("+") and phone[1:].isdigit()) or phone.isdigit():
            return phone
        else:
            print("Enter a valid phone number with country code as (+12)9876543210.")

def get_valid_hour():
    while True:
        try:
            hour = int(input("Enter the Hour (0-23): "))
            if 0 <= hour <= 23:
                return hour
            else:
                print("Hour must be between 0 and 23.")
        except ValueError:
            print("Please enter a valid number for Hour.")

def get_valid_minute():
    while True:
        try:
            minute = int(input("Enter the Minute (0-59): "))
            if 0 <= minute <= 59:
                return minute
            else:
                print("Minute must be between 0 and 59.")
        except ValueError:
            print("Please enter a valid number for Minute.")

def send_whatsapp_message_instantly(wait_time=15, tab_close=True, close_time=2):
    message = input("Enter your message: ").strip()
    phone = get_valid_phone()
    try:
        pywhatkit.sendwhatmsg_instantly(phone, message, wait_time, tab_close, close_time)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Failed to send message: {e}")

def send_whatsapp_message_by_time(wait_time=15, tab_close=True, close_time=2):
    message = input("Enter your message: ").strip()
    hour = get_valid_hour()
    minute = get_valid_minute()
    phone = get_valid_phone()
    try:
        pywhatkit.sendwhatmsg(phone, message, hour, minute, wait_time, tab_close, close_time)
        print(f"Message scheduled successfully for {hour:02d}:{minute:02d}!")
    except Exception as e:
        print(f"Failed to schedule message: {e}")

def run_whatsapp_program():
    print("📱 WhatsApp Automation Program")
    while True:
        print("\nOptions:")
        print("1️. Send Message Instantly")
        print("2️. Send Message by Time")
        print("3️. Quit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            send_whatsapp_message_instantly()
        elif choice == "2":
            send_whatsapp_message_by_time()
        elif choice == "3":
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or q.")

if __name__ == "__main__":
    run_whatsapp_program()
