import tkinter as tk

root = tk.Tk()
root.title("The Ultimate Spammer")
root.geometry("600x650")

# def repeat_options():

#     foptions = ["Kungfu Panda script", "Custom keyword or phrase"]

#     flabel = tk.Label(root, text="What do you wish to spam?")
#     flabel.config(font=("Arial", 16))
#     flabel.pack()

#     fwish= tk.StringVar()
#     fwish.set("Kungfu Panda script")
#     fdrop = tk.OptionMenu( root , fwish , *foptions )
#     fdrop.config(font=("Arial", 12))
#     fdrop.pack()

#     return fwish.get()


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

        def eshow():
            fdrop.config(state="disabled")
            var = fwish.get()
            if var == "Custom keyword or phrase":
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

        ytlabel0 = tk.Label(root, text="It will wait for 10 seconds before sending the spam because of youtube live comment rules.")
        ytlabel0.config(font=("Arial", 14), wraplength=600)
        ytlabel0.pack()

        

    elif clicked.get() == "Instagram":

        foptions = ["Kungfu Panda script", "Custom keyword or phrase"]

        flabel = tk.Label(root, text="What do you wish to spam?")
        flabel.config(font=("Arial", 16))
        flabel.pack()

        fwish= tk.StringVar()
        fwish.set("Kungfu Panda script")
        fdrop = tk.OptionMenu( root , fwish , *foptions )
        fdrop.config(font=("Arial", 12))
        fdrop.pack()

        def instashow():

            fdrop.config(state="disabled")
            var = fwish.get()

            if var == "Custom keyword or phrase":
                instalabel1 = tk.Label(root, text="Enter your custom keyword:")
                instalabel1.config(font=("Arial", 16))
                instalabel1.pack()
                    
                instatext1 = tk.Text(root, height=1, width=100)
                instatext1.config(font=("Arial", 16))
                instatext1.pack(padx=10, pady=10)

                instalabel2 = tk.Label(root, text="How many times do you want to spam?")
                instalabel2.config(font=("Arial", 16))
                instalabel2.pack()
                    
                instatext2 = tk.Text(root, height=1, width=100)
                instatext2.config(font=("Arial", 16))
                instatext2.pack(padx=10, pady=10)

                instalabel3 = tk.Label(root, text="Enter your Instagram username:")
                instalabel3.config(font=("Arial", 16))
                instalabel3.pack()
                    
                instatext3 = tk.Text(root, height=1, width=100)
                instatext3.config(font=("Arial", 16))
                instatext3.pack(padx=10, pady=10)

                instalabel4 = tk.Label(root, text="Enter your Instagram password:")
                instalabel4.config(font=("Arial", 16))
                instalabel4.pack()
                    
                instatext4 = tk.Text(root, height=1, width=100)
                instatext4.config(font=("Arial", 16))
                instatext4.pack(padx=10, pady=10)

                instalabel5 = tk.Label(root, text="Enter the Instagram ID of the person you want to spam:")
                instalabel5.config(font=("Arial", 16), wraplength=600)
                instalabel5.pack()
                    
                instatext5 = tk.Text(root, height=1, width=100)
                instatext5.config(font=("Arial", 16))
                instatext5.pack(padx=10, pady=10)

            elif var == "Kungfu Panda script":

                instalabel6 = tk.Label(root, text="Enter your Instagram username:")
                instalabel6.config(font=("Arial", 16))
                instalabel6.pack()
                    
                instatext6 = tk.Text(root, height=1, width=100)
                instatext6.config(font=("Arial", 16))
                instatext6.pack(padx=10, pady=10)

                instalabel7 = tk.Label(root, text="Enter your Instagram password:")
                instalabel7.config(font=("Arial", 16))
                instalabel7.pack()
                    
                instatext7 = tk.Text(root, height=1, width=100)
                instatext7.config(font=("Arial", 16))
                instatext7.pack(padx=10, pady=10)

                instalabel8 = tk.Label(root, text="Enter the Instagram ID of the person you want to spam:")
                instalabel8.config(font=("Arial", 16), wraplength=600)
                instalabel8.pack()
                    
                instatext8 = tk.Text(root, height=1, width=100)
                instatext8.config(font=("Arial", 16))
                instatext8.pack(padx=10, pady=10)

        instabutton = tk.Button( root , text = "SUBMIT" , command = instashow)
        instabutton.config(font=("Arial", 12))
        instabutton.pack()

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

                olabel = tk.Label(root, text="Open the application where you want to spam. Press enter once you've done it and then switch to that application and place the cursor to the 'type message' box.")
                olabel.config(font=("Arial", 14), wraplength=600)
                olabel.pack()
            
            elif var == "Kungfu Panda script":
                olabelk = tk.Label(root, text="Open the application where you want to spam. Press enter once you've done it and then switch to that application and place the cursor to the 'type message' box.")
                olabelk.config(font=("Arial", 14), wraplength=600)
                olabelk.pack()

        obutton = tk.Button( root , text = "SUBMIT" , command = oshow)
        obutton.config(font=("Arial", 12))
        obutton.pack()


# Dropdown menu options
options = [
    "File",
    "Email",
    "Youtube Live comments",
    "Instagram",
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
