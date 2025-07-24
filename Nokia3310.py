def main():
    running = True
    while running:
        prompt = """
1 -> Phone book
2 -> Messages
3 -> Chat
4 -> Call register
5 -> Tones
6 -> Settings
7 -> Call divert
8 -> Games
9 -> Calculator
10 -> Reminders
11 -> Clock
12 -> Profiles
13 -> SIM services
100 -> Exit
"""
        print(prompt)
        user_input = int(input("Enter selection: "))

        if user_input == 1:
            print("""
1: Search
2: Service Nos.
3: Add name
4: Erase
5: Edit
6: Assign tone
7: Send b'card
8: Options
9: Speed dials
10: Voice tags
100: Exit
""")
            phone_book_input = int(input("Enter Selection: "))
            if phone_book_input == 8:
                print("""
8 -> Options
    1: Type of view
    2: Memory status
""")
            elif phone_book_input == 100:
                print("Exiting Phone book.")
            else:
                print("Invalid input.")

        elif user_input == 2:
            print("""
2 -> Messages
    1: Write messages
    2: Inbox
    3: Outbox
    4: Picture messages
    5: Templates
    6: Smileys
    7: Message settings
    8: Info service
    9: Voice mailbox number
    10: Service command editor
""")
            message_input = int(input("Enter 7 to see Message settings 00 to return : "))
            if message_input == 7:
                print("""
7

 -> Message settings
    1: Set 1
    2: Common
""")
                settings_input = int(input("Enter 1 or 2 to see submenu 00 to return : "))
                if settings_input == 1:
                    print("""
1 -> Set 1
    1: Message center number
    2: Message sent as
    3: Message validity
""")
                elif settings_input == 2:
                    print("""
2 -> Common
    1: Delivery reports
    2: Reply via same center
    3: Character support
""")
                else:
                    print("Invalid input.")

        elif user_input == 3:
            print("Chat")

        elif user_input == 4:
            print("""
4 -> Call register
    1: Missed calls
    2: Received calls
    3: Dialled numbers
    4: Erase recent call lists
    5: Show call duration
    6: Show call costs
    7: Call cost settings
    8: Prepaid credit
""")
            call_register_input = int(input("Press 5, 6, or 7 for options 00 to return: "))
            if call_register_input == 5:
                print("""
5 -> Show call duration
    1: Last call duration
    2: All calls duration
    3: Received calls duration
    4: Dialled calls duration
    5: Clear timers
""")
            elif call_register_input == 6:
                print("""
6 -> Show call costs
    1: Last call cost
    2: All calls cost
    3: Clear counters
""")
            elif call_register_input == 7:
                print("""
7 -> Call cost settings
    1: Call cost limit
    2: Show costs in
""")
            else:
                print("Invalid input.")

        elif user_input == 5:
            print("""
5 -> Tones
    1: Ringing tone
    2: Ringing volume
    3: Incoming call alert
    4: Composer
    5: Message alert tone
    6: Keypad tones
    7: Warning and game tones
    8: Vibrating alert
    9: Screen saver
""")

        elif user_input == 6:
            print("""
6 -> Settings
    1: Call settings
        1: Automatic redial
        2: Speed dialling
        3: Call waiting options
        4: Own number sending
        5: Phone line in use
        6: Automatic answer
    2: Phone settings
    3: Security settings
    4: Restore factory settings
""")

        elif user_input == 7:
            print("Call divert")

        elif user_input == 8:
            print("Games")

        elif user_input == 9:
            print("Calculator")

        elif user_input == 10:
            print("Reminders")

        elif user_input == 11:
            print("Clock")

        elif user_input == 12:
            print("Profiles")

        elif user_input == 13:
            print("SIM services")

        elif user_input == 0:
            print("Exiting Nokia menu.")
            running = False

        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()

