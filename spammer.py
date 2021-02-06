"""
By using this code, written in Python, you agree that you will use it for educational purpose only and in case you use it for some illegal activity, 
the author will not be responsible for it.
"""

import smtplib, pyautogui, time, os, helium
pyautogui.FAILSAFE = True
cwd = os.getcwd()

class Spammer:
    """
    Spammer class which has functions to spam in file, email and other ways.
    """
    @staticmethod
    def spam_script_file(filepath, filename):
        try:
            os.chdir(filepath)
            f = open(f"{filename}", 'a')
            script_file = open('kungfu_panda.txt', 'r')
            script = script_file.read()
            f.write(script)
            f.close()
            script_file.close()

        except Exception as e:
            print(e)

        finally:
            os.chdir(cwd)

    @staticmethod
    def spam_file(filepath, filename, keyword, times):
        try:
            os.chdir(filepath)
            with open(f"{filename}", 'a') as f:
                for i in range(times):
                    f.write(f"{keyword}\n")

        except Exception as e:
            print(e)

        finally:
            os.chdir(cwd)

    @staticmethod
    def spam_email(keyword, times):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            host = input("Enter email address to spam: ")
            your_email = input("Enter your email: ")
            password = input("Enter your password: ")
            server.login(your_email, password)
            subject = input("Enter spam mail subject: ")
            body = keyword * times
            server.sendmail(your_email, host, f"Subject: {subject}\n{body}")
            server.quit()
            print("Spam email has been sent successfully!")

        except Exception as e:
            print(f"Following error occured:\n{e}")
            
    @staticmethod
    def spam_other(keyword, times):
        print("Starting spamming in 10 seconds...")
        time.sleep(10)
        for _ in range(times):
            pyautogui.typewrite(keyword)

    @staticmethod
    def spam_insta(username, password, to, keyword, times):
        helium.start_chrome("instagram.com/direct/inbox")
        helium.write(username, into="Phone number, username, or email")
        helium.write(password, into="Password")
        helium.click("Log In")
        time.sleep(5)

        if helium.Button("Save Info").exists():
            helium.click("Not Now")

        if helium.Button("Turn On").exists():
            helium.click("Not Now")

        try:
            helium.click("Send Message")
            helium.write(to)
            time.sleep(5)
            helium.click(to)
            helium.click("Next")
        except LookupError:
            print("Invalid username {}!".format(to))
            quit()

        time.sleep(2)
        for _ in range(times):
            helium.write(keyword)
            helium.press(helium.ENTER)
        time.sleep(5)
        helium.kill_browser()


    def main(self):
        print("!!!!!This is the ultimate spammer!!!!!")
        app = int(input("\nWhere to spam?\n1.File\n2.Email\n3.Youtube Live Comments\n4.Instagram\n5.Other\n"))


        # TEXT FILE
        if app==1:
            print("\nWhat to spam?\n1. Kungfu Panda script\n2. Custom keyword or phrase")
            meme = int(input())

            if meme==1:
                file = input("Enter file name: ")
                path = input("Enter the directory path where this file is located: ")
                self.spam_script_file(path, file)

            elif meme==2:
                file = input("Enter file name: ")
                path = input("Enter the directory path where this file is located: ")
                keyword = input("Enter your custom keyword: ")
                times = int(input("How many times: "))
                self.spam_file(path, file, keyword, times)

            else:
                raise Exception("Access denied!")

        
        # EMAIL SPAM
        elif app==2:
            print("\nWhat to spam?\n1. Kungfu Panda script\n2. Custom keyword or phrase")
            meme = int(input())

            if meme == 1:
                script_file = open(r'kungfu_panda.txt', 'r')
                script = script_file.read()
                self.spam_email(script, 1)

            elif meme==2:
                keyword = input("Enter your custom keyword: ")
                times = int(input("How many times: "))
                self.spam_email(f"{keyword}\n", times)

            else:
                raise Exception("Access denied!")


        # YOUTUBE COMMENT SPAM
        elif app==3:
            print("Open the youtube video with comment section on.")
            keyword = input("Enter your keyword: ")
            times = int(input("How many times: "))
            print("It will wait for 10 seconds before sending the spam because of youtube live comment rules.")
            time.sleep(10)
            for _ in range(times):
                self.spam_other(keyword, times)
                time.sleep(5)

        # INSTAGRAM SPAM
        elif app == 4:
            print("\nWhat to spam?\n1. Kungfu Panda script\n2. Custom keyword or phrase")
            meme = int(input())

            if meme == 1:
                username = input("Enter your Instagram username: ")
                password = input("Enter your Instagram password: ")
                host = input("Enter the Instagram ID of the one you want to spam: ")
                with open(r'kungfu_panda.txt') as f:
                    script = f.read()
                self.spam_insta(username, password, host, script, 1)

            elif meme == 2:
                keyword = input("Enter your custom keyword: ")
                times = int(input("How many times: "))
                username = input("Enter your Instagram username: ")
                password = input("Enter your Instagram password: ")
                host = input("Enter the Instagram ID of the one you want to spam: ")
                try:
                    self.spam_insta(username, password, host, keyword, times)
                except Exception as e:
                    print(e)

            else:
                raise Exception("Access denied!")


        # OTHER SPAM
        elif app==5:
            print("\nWhat to spam?\n1. Kungfu Panda script\n2. Custom keyword or phrase")
            meme = int(input())
            
            if meme == 1:
                check = input("Open the application where you want to spam. Press enter once you've done it and then switch to that application and place the cursor to the 'type message' box.")
                with open(r'kungfu_panda.txt') as f:
                    script = f.read()
                self.spam_other(script, 1)

            elif meme == 2:
                keyword = input("Enter your custom keyword: ")
                times = int(input("How many times: "))
                check = input("Open the application where you want to spam. Press enter once you've done it and then switch to that application and place the cursor to the 'type message' box.")
                self.spam_other(keyword+"\n", times)

            else:
                raise Exception("Access denied!")
            

        else:
            raise Exception("Access denied!")

        print("!!!!Spamming task successfuly executed!!!!")



if __name__=='__main__':
    sp = Spammer()
    sp.main()