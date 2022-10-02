"""
By using this code, written in Python, you agree that you will use it for educational purpose only and in case you use it for some illegal activity, 
the author will not be responsible for it.
"""

import smtplib, pyautogui, time, os
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
    def spam_email(keyword, times, host, your_email, password, subject):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(your_email, password)
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


    def main(self):
        print("!!!!!This is the ultimate spammer!!!!!")
        app = int(input("\nWhere to spam?\n1.File\n2.Email\n3.Youtube Live Comments\n4.Other\n"))


        # TEXT FILE
        if app==1:
            print("\nWhat to spam?\n1. Kungfu Panda script\n2. Custom keyword or phrase")
            meme = int(input())

            if meme==1:
                file = input("Enter filename: ")
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

        # OTHER SPAM
        elif app == 4:
            print("\nWhat to spam?\n1. Kungfu Panda script\n2. Custom keyword or phrase")
            meme = int(input())
            
            if meme == 1:
                input("Open the application where you want to spam. Press enter once you've done it and then switch to that application and place the cursor to the 'type message' box.")
                with open(r'kungfu_panda.txt') as f:
                    script = f.read()
                self.spam_other(script, 1)

            elif meme == 2:
                keyword = input("Enter your custom keyword: ")
                times = int(input("How many times: "))
                input("Open the application where you want to spam. Press enter once you've done it and then switch to that application and place the cursor to the 'type message' box.")
                self.spam_other(keyword+"\n", times)

            else:
                raise Exception("Access denied!")
            
        else:
            raise Exception("Access denied!")

        print("!!!!Spamming task successfully executed!!!!")


if __name__=='__main__':
    sp = Spammer()
    sp.main()