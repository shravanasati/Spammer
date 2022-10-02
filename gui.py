import tkinter as tk
import spammer, time

root = tk.Tk()
root.title("The Ultimate Spammer")
root.geometry("600x800")

def success():
    ending = tk.Label(root, text="!!!!Spamming task successfully executed!!!!")
    ending.config(font=("Arial", 14), wraplength=600)
    ending.pack()


def show():

    drop.config(state="disabled")

    if clicked.get() == "File":
        
        foptions = ["Kungfu Panda script", "Custom keyword or phrase"]

        flabel = tk.Label(root, text="What do you wish to spam?")
        flabel.config(font=("Arial", 16))
        flabel.pack()

        fwish= tk.StringVar()
        fwish.set("Kungfu Panda script")
        fdrop = tk.OptionMenu( root , fwish , *foptions )
        fdrop.config(font=("Arial", 12))
        fdrop.pack()


        def fshow():

            fdrop.config(state="disabled")

            var = fwish.get()
            if  var == "Kungfu Panda script":
                klabel1 = tk.Label(root, text="Enter file name:")
                klabel1.config(font=("Arial", 16))
                klabel1.pack()

                ktext1 = tk.Text(root, height=1, width=100)
                ktext1.config(font=("Arial", 16))
                ktext1.pack(padx=10, pady=10)

                klabel2 = tk.Label(root, text="Enter the directory path where this file is located:")
                klabel2.config(font=("Arial", 16), wraplength=600)
                klabel2.pack()
                
                ktext2 = tk.Text(root, height=1, width=100)
                ktext2.config(font=("Arial", 16))
                ktext2.pack(padx=10, pady=10)

                fbtn1 = tk.Button(root, text="START SPAMMING", command=spam_file_k)
                fbtn1.config(font=("Arial", 12))
                fbtn1.pack()

                def spam_file_k():
                    try:
                        sp = spammer.Spammer()
                        file = ktext1.get("1.0", "end")
                        path = ktext2.get("1.0", "end")
                        sp.spam_script_file(path, file)
                    except Exception as e:
                        print(e)
                    else:
                        success()

            elif var == "Custom keyword or phrase":
                cuslabel1 = tk.Label(root, text="Enter file name:")
                cuslabel1.config(font=("Arial", 16))
                cuslabel1.pack()

                custext1 = tk.Text(root, height=1, width=100)
                custext1.config(font=("Arial", 16))
                custext1.pack(padx=10, pady=10)

                cuslabel2 = tk.Label(root, text="Enter the directory path where this file is located:")
                cuslabel2.config(font=("Arial", 16))
                cuslabel2.pack()
                
                custext2 = tk.Text(root, height=1, width=100)
                custext2.config(font=("Arial", 16))
                custext2.pack(padx=10, pady=10)

                cuslabel3 = tk.Label(root, text="Enter your custom keyword:")
                cuslabel3.config(font=("Arial", 16))
                cuslabel3.pack()
                
                custext3 = tk.Text(root, height=1, width=100)
                custext3.config(font=("Arial", 16))
                custext3.pack(padx=10, pady=10)

                cuslabel4 = tk.Label(root, text="How many times do you want to spam?")
                cuslabel4.config(font=("Arial", 16))
                cuslabel4.pack()
                
                custext4 = tk.Text(root, height=1, width=100)
                custext4.config(font=("Arial", 16))
                custext4.pack(padx=10, pady=10)

                fbtn2 = tk.Button(root, text="START SPAMMING", command=spam_file_c)
                fbtn2.config(font=("Arial", 12))
                fbtn2.pack()

                def spam_file_c():
                    try:
                        sp = spammer.Spammer()
                        file = custext1.get("1.0", "end")
                        path = custext2.get("1.0", "end")
                        keyword = custext3.get("1.0", "end")
                        times = custext4.get("1.0", "end")
                        sp.spam_file(path, file, keyword, times)
                    except Exception as e:
                        print(e)
                    else:
                        success()


        fbutton = tk.Button( root , text = "SUBMIT" , command = fshow)
        fbutton.config(font=("Arial", 12))
        fbutton.pack()

    elif clicked.get() == "Email":

        foptions = ["Kungfu Panda script", "Custom keyword or phrase"]

        flabel = tk.Label(root, text="What do you wish to spam?")
        flabel.config(font=("Arial", 16))
        flabel.pack()

        fwish= tk.StringVar()
        fwish.set("Kungfu Panda script")
        fdrop = tk.OptionMenu( root , fwish , *foptions )
        fdrop.config(font=("Arial", 12))
        fdrop.pack()

        ql1 = tk.Label(root, text="Enter email address to spam:")
        ql1.config(font=("Arial", 16))
        ql1.pack()
                
        qt1 = tk.Text(root, height=1, width=100)
        qt1.config(font=("Arial", 16))
        qt1.pack(padx=10, pady=10)


        ql2 = tk.Label(root, text="Enter your email address:")
        ql2.config(font=("Arial", 16))
        ql2.pack()
                
        qt2 = tk.Text(root, height=1, width=100)
        qt2.config(font=("Arial", 16))
        qt2.pack(padx=10, pady=10)


        ql3 = tk.Label(root, text="Enter your password:")
        ql3.config(font=("Arial", 16))
        ql3.pack()
                
        qt3 = tk.Text(root, height=1, width=100)
        qt3.config(font=("Arial", 16))
        qt3.pack(padx=10, pady=10)


        ql4 = tk.Label(root, text="Enter the subject:")
        ql4.config(font=("Arial", 16))
        ql4.pack()
                
        qt4 = tk.Text(root, height=1, width=100)
        qt4.config(font=("Arial", 16))
        qt4.pack(padx=10, pady=10)

        def eshow():

            fdrop.config(state="disabled")
            var = fwish.get()
            host = qt1.get("1.0", "end")
            your_email = qt2.get("1.0", "end")
            password = qt3.get("1.0", "end")
            subject = qt4.get("1.0", "end")

            if var == "Custom keyword or phrase":
                def spam_email_c():

                    keyword = etext1.get("1.0", "end")
                    times = int(etext2.get("1.0", "end"))
                    
                    try:
                        sp = spammer.Spammer()
                        sp.spam_email(f"{keyword}\n", times, host, your_email, password, subject)
                    except Exception as e:
                        print(e)
                    else:
                        success()

                elabel1 = tk.Label(root, text="Enter your custom keyword:")
                elabel1.config(font=("Arial", 16))
                elabel1.pack()
                
                etext1 = tk.Text(root, height=1, width=100)
                etext1.config(font=("Arial", 16))
                etext1.pack(padx=10, pady=10)

                elabel2 = tk.Label(root, text="How many times do you want to spam?")
                elabel2.config(font=("Arial", 16))
                elabel2.pack()
                
                etext2 = tk.Text(root, height=1, width=100)
                etext2.config(font=("Arial", 16))
                etext2.pack(padx=10, pady=10)

                ebtn1 = tk.Button(root, text="START SPAMMING", command=spam_email_c)
                ebtn1.config(font=("Arial", 12))
                ebtn1.pack()


            elif var == "Kungfu Panda script":
                try:
                    script_file = open(r'kungfu_panda.txt', 'r')
                    script = script_file.read()
                    sp = spammer.Spammer()
                    sp.spam_email(script, 1, host, your_email, password, subject)
                except Exception as e:
                    print(e)
                else:
                    success()

        ebutton = tk.Button( root , text = "SUBMIT" , command = eshow)
        ebutton.config(font=("Arial", 12))
        ebutton.pack()

    elif clicked.get() == "Youtube Live comments":

        ytlabel = tk.Label(root, text="Open the youtube video with comment section on.")
        ytlabel.config(font=("Arial", 14), wraplength=600)
        ytlabel.pack()

        ytlabel1 = tk.Label(root, text="Enter your custom keyword:")
        ytlabel1.config(font=("Arial", 16))
        ytlabel1.pack()
                
        yttext1 = tk.Text(root, height=1, width=100)
        yttext1.config(font=("Arial", 16))
        yttext1.pack(padx=10, pady=10)

        ytlabel2 = tk.Label(root, text="How many times do you want to spam?")
        ytlabel2.config(font=("Arial", 16))
        ytlabel2.pack()
                
        yttext2 = tk.Text(root, height=1, width=100)
        yttext2.config(font=("Arial", 16))
        yttext2.pack(padx=10, pady=10)

        ybtn1 = tk.Button(root, text="START SPAMMING", command=spam_yt)
        ybtn1.config(font=("Arial", 12))
        ybtn1.pack()


        def spam_yt():

            ytlabel0 = tk.Label(root, text="It will wait for 10 seconds before sending the spam because of youtube live comment rules.")
            ytlabel0.config(font=("Arial", 14), wraplength=600)
            ytlabel0.pack()

            try:
                sp = spammer.Spammer()
                keyword = yttext1.get("1.0", "end")
                times = yttext2.get("1.0", "end")
                time.sleep(10)
                for _ in range(times):
                    sp.spam_other(keyword, times)
                    time.sleep(5)
            except Exception as e:
                print(e)
            else:
                success()

    elif clicked.get() == "Others":

        foptions = ["Kungfu Panda script", "Custom keyword or phrase"]

        flabel = tk.Label(root, text="What do you wish to spam?")
        flabel.config(font=("Arial", 16))
        flabel.pack()

        fwish= tk.StringVar()
        fwish.set("Kungfu Panda script")
        fdrop = tk.OptionMenu( root , fwish , *foptions )
        fdrop.config(font=("Arial", 12))
        fdrop.pack()

        def oshow():

            fdrop.config(state="disabled")
            var = fwish.get()

            if var == "Custom keyword or phrase":

                olabel1 = tk.Label(root, text="Enter your custom keyword:")
                olabel1.config(font=("Arial", 16))
                olabel1.pack()
                    
                otext1 = tk.Text(root, height=1, width=100)
                otext1.config(font=("Arial", 16))
                otext1.pack(padx=10, pady=10)

                olabel2 = tk.Label(root, text="How many times do you want to spam?")
                olabel2.config(font=("Arial", 16))
                olabel2.pack()
                    
                otext2 = tk.Text(root, height=1, width=100)
                otext2.config(font=("Arial", 16))
                otext2.pack(padx=10, pady=10)


                obtn1 = tk.Button(root, text="START SPAMMING", command=spam_others_c)
                obtn1.config(font=("Arial", 12))
                obtn1.pack()

                def spam_others_c():

                    olabel = tk.Label(root, text="Open the application where you want to spam. Press enter once you've done it and then switch to that application and place the cursor to the 'type message' box.")
                    olabel.config(font=("Arial", 14), wraplength=600)
                    olabel.pack()
                    try:
                        sp = spammer.Spammer()
                        keyword = otext1.get("1.0", "end")
                        times = otext2.get("1.0", "end")
                        sp.spam_other(keyword+"\n", times)
                    except Exception as e:
                        print(e)
                    else:
                        success()
                
            elif var == "Kungfu Panda script":

                olabelk = tk.Label(root, text="Open the application where you want to spam. Press enter once you've done it and then switch to that application and place the cursor to the 'type message' box.")
                olabelk.config(font=("Arial", 14), wraplength=600)
                olabelk.pack()
                
                try:
                    sp = spammer.Spammer()
                    with open(r'kungfu_panda.txt') as f:
                        script = f.read()
                    sp.spam_other(script, 1)
                except Exception as e:
                    print(e)
                else:
                    success()

        obutton = tk.Button( root , text = "SUBMIT" , command = oshow)
        obutton.config(font=("Arial", 12))
        obutton.pack()

    
# Dropdown menu options
options = [
    "File",
    "Email",
    "Youtube Live comments",
    "Others"
]

l_where = tk.Label(root, text="Where do you want to spam?")
l_where.config(font=("Arial", 16))
l_where.pack()

# datatype of menu text
clicked = tk.StringVar()

# initial menu text
clicked.set( "File" )

# Create Dropdown menu
drop = tk.OptionMenu( root , clicked , *options )
drop.config(font=("Arial", 12))
drop.pack()

# Create button, it will change label text
button = tk.Button( root , text = "SUBMIT" , command = show)
button.config(font=("Arial", 12))
button.pack()

# Execute tkinter
root.mainloop()
