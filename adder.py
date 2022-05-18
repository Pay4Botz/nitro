import ctypes
import string
import os
import time

USE_WEBHOOK = True


os.system('cls' if os.name == 'nt' else 'clear')


try:  # Check if the requrements have been installed
    from discord_webhook import DiscordWebhook  # Try to import discord_webhook
except ImportError:  # If it chould not be installed
    # Tell the user it has not been installed and how to install it
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:  # Setup try statement to catch the error
    import requests  # Try to import requests
except ImportError:  # If it has not been installed
    # Tell the user it has not been installed and how to install it
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()  # Exit the program
try:  # Setup try statement to catch the error
    import numpy  # Try to import requests
except ImportError:  # If it has not been installed
    # Tell the user it has not been installed and how to install it
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()  # Exit the program

# check if user is connected to internet
url = "https://github.com"
try:
    response = requests.get(url)  # Get the responce from the url
    print("Internet check")
    
except requests.exceptions.ConnectionError:
    # Tell the user
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()  # Exit program


class NitroGen:  # Initialise the class
    def __init__(self):  # The initaliseaiton function
        self.fileName = "Nitro Codes.txt"  # Set the file name the codes are stored in

    def main(self):  # The main function contains the most important code
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        if os.name == "nt":  # If the system is windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator and Checker ")  # Change the
        else:  # Or if it is unix
            print('Nitro Generator '),
             

        try:
            num = 9999999  # Ask the user for the amount of codes
        except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()  # Exit program

        if USE_WEBHOOK:
            # Get the webhook url, if the user does not wish to use a webhook the message will be an empty string
            #print("If you want to use a Discord webhook, type it here or press enter to ignore: ")
            url = 'https://discord.com/api/webhooks/976486505105223700/9Zzu_F8agmW1XcUcUWFsO8UVOUkJ40uYlIdaej9iOer2hHY-lnqB2httH993YT4o4p_U'
            # If the url is empty make it be None insted
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(  # Let the user know it has started logging the ids
                        url=url,
                        content=f"Started checking urls\nI will send any valid codes here,\n Made by Adarsh :heart: "
                    ).execute()

        

        valid = []  # Keep track of valid codes
        invalid = 0  # Keep track of how many invalid codes was detected
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        # generate codes faster than using random.choice
        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:  # Loop over the amount of codes to check
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"  # Generate the url

                result = self.quickChecker(url, webhook)  # Check the codes

                if result:  # If the code was valid
                    # Add that code to the list of found codes
                    valid.append(url)
                else:  # If the code was not valid
                    invalid += 1  # Increase the invalid counter by one
            except KeyboardInterrupt:
                # If the user interrupted the program
                print("\nInterrupted by user")
                break  # Break the loop

            except Exception as e:  # If the request fails
                print(f" Error | {url} ")  # Tell the user an error occurred

            if os.name == "nt":  # If the system is windows
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid ")  # Change the title
                print("")
            else:  # If it is a unix system
                # Change the title
                print(
                    f'Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid ', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")  # Give a report of the results of the check

        # Tell the user the program finished
        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]  # Wait for 4 enter presses

    

    def quickChecker(self, nitro:str, notify=None):  # Used to check a single code at a time
        # Generate the request url
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  # Get the response from discord

        if response.status_code == 200:  # If the responce went through
            # Notify the user the code was valid
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:  # Open file to write
                # Write the nitro code to the file it will automatically add a newline
                file.write(nitro)

            if notify is not None:  # If a webhook has been added
                DiscordWebhook(  # Send the message to discord letting the user know there has been a valid nitro code
                    url=url,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True  # Tell the main function the code was found

        # If the responce got ignored or is invalid ( such as a 404 or 405 )
        else:
            # Tell the user it tested a code and it was invalid
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  # Tell the main function there was not a code found


if __name__ == '__main__':
    Gen = NitroGen()  # Create the nitro generator object
    Gen.main()  # Run the main code
