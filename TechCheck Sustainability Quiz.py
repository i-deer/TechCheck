# Stemettes CS Project - TechCheck

# Source: https://www.ovoenergy.com/guides/energy-guides/how-much-electricity-does-a-home-use

# Average watt usage is (2,700,000 watts per hour) per year -> (750 watts per second) per year
# 1 year is 31536000 seconds
# 1800 kwh for flats (500 watts per second), 4300 kwh for detached houses and bungalows (approx 1200) -> 3050 as an everage point (approx 850 watts per second)
# figures dont include heating

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

watt_values_list = [0,0]

class Sustainability_Quiz_App (tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 
 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
 
        # initializing frames to an empty array
        self.frames = {}
 
        # iterating through a tuple consisting of the different page layouts
        for F in (start_Screen, devices_Screen, results_Screen):
 
            frame = F(container, self)
 
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
 
            frame.grid(row = 0, column = 0, sticky ="nsew")
 
        self.show_frame(start_Screen)
 
    # to display the current frame passed as parameter
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
class start_Screen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        style = ttk.Style()
        style.configure("Heading.TLabel", background = "blue", font = ("ariel", 20, "bold"))
        
        title = ttk.Label(
            self,
            text = "TechCheck's Power Usage Quiz",
            style = "Heading.TLabel",
            width = 105
            )

        title.place(x = 0, y = 2)

        style.configure("TButton", bg = "black", bd = 3, color = "black", font = ("ariel", 16, "bold"))
        
        next_button = ttk.Button(
            self,
            text = "Next",
            command = lambda:controller.show_frame(devices_Screen),
            width = 5
            )

        next_button.place(x = 20, y = 50)

        style.configure("TLabel", font = ("ariel", 16, "normal"))

        titles_y_pos = 110
        
        welcome_title = ttk.Label(
            self,
            text = "Welcome to TechCheck's Sustainability Power Calculator!",
            )

        welcome_title.place(x = 20, y = titles_y_pos)
        titles_y_pos += 50

        instruction_titles = ["The below calculator will allow you to see how many watts you are using per second if you were to use all the device you have at once",
                              "Please select from the options below which type of house you live in"
                              ]

        for instruction in instruction_titles:

            explanation_title = ttk.Label(
                self,
                text = instruction,
                )

            explanation_title.place(x = 20, y = titles_y_pos)
            titles_y_pos += 50


        home_list = {"Mid-terrace" : "1",
                     "Flat": "2",
                     "End-terrace": "3",
                     "Semi-detached House":"4",
                     "Detached House":"5",
                     "Bungalow":"6"}

        y_pos = titles_y_pos

        for (house_type,value) in home_list.items():
            radio_button = ttk.Radiobutton(
                self,
                text= house_type,
                variable=StringVar(),
                value = value,
                )

            radio_button.place(x = 100, y = y_pos)
            y_pos += 40

        mid_terrace_or_flat_owner = False #500 (ideal)
        end_terrace_owner = False #975 (ideal)
        semi_detached_house_or_bungalow_owner = False # 1120 (ideal)
        detached_house_owner = False #1200 (ideal)

        def on_select_type(event):
            selected_house_type = radio_button.get()
            if selected_house_type == "Mid-terrace":
                mid_terrace_or_flat_owner = True
            elif selected_house_type == "Flat":
                mid_terrace_or_flat_owner = True
            elif selected_house_type == "End-terrace":
                end_terrace_owner = True
            elif selected_house_type == "Semi-detached House":
                semi_detached_house_or_bungalow_owner = True
            elif selected_house_type == "Bungalow":
                semi_detached_house_or_bungalow_owner = True
            elif selected_house_type == "Detached House":
                detached_house_owner = True

        radio_button.bind("<<RadiobuttonSelected>>", on_select_type)

class devices_Screen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        style = ttk.Style()
        style.configure("Heading.TLabel", background = "blue", foreground = "white", font = ("ariel", 20, "bold"))
        
        title = ttk.Label(
            self,
            text = "TechCheck's Power Usage Quiz",
            style = "Heading.TLabel",
            width = 105
            )

        title.place(x = 0, y = 2)

        style.configure("TButton", background = "black", foreground = "white", font = ("ariel", 16, "bold"))

        #contains values of user's watt usage
        #self.watt_values_list = [0,0]
        
        def calc_usage():
            # Variable is initially set to 0 but increases depending on the users electrical usage
            initial_watt_usage = 0

            # Variable is initially set to 0 but increases depending on the users electrical usage
            running_watt_usage = 0

            # Loops so each item watt consumption can be added to the total
            for item in devices_calc_list:

                # fetches the rated watt values from the devices dictionary
                rated_watts = devices[item][0]

                # adds both measures to the user's electrical usage
                running_watt_usage = running_watt_usage + rated_watts

                # fetches the rated watt and surge watt values from the devices dictionary
                surge_watts = devices[item][1]

                # adds both measures to the user's electrical usage
                initial_watt_usage = initial_watt_usage + surge_watts

            #appends values to the list so function can return multiple values
            watt_values_list[0] = initial_watt_usage
            watt_values_list[1] = running_watt_usage

            mb.showinfo("Information", "This is your total initial watt usage if you were to run all your devices at once: " + str(watt_values_list[0]))

            mb.showinfo("Information", "This is your watt usage if you were to run all your devices at once per second: " + str(watt_values_list[1]))
            
            print("This is your total initial watt usage if you were to run all your devices at once:", str(watt_values_list[0]))
            print("This is your watt usage if you were to run all your devices at once per second:", str(watt_values_list[1]))
            print(str(watt_values_list))

        next_button = ttk.Button(
            self,
            text = "Next",
            command = lambda:controller.show_frame(results_Screen),
            width = 5
            )

        next_button.place(x = 20, y = 50)

        back_button = ttk.Button(
            self,
            text = "Back",
            command = lambda:controller.show_frame(start_Screen),
            width = 5
            )

        back_button.place(x = 700, y = 50)

        submit_button = ttk.Button(
            self,
            text = "Submit",
            command = calc_usage,
            width = 7
            )

        submit_button.place(x = 360, y = 50)

        titles_y_pos = 110
        
        main_title = ttk.Label(
            self,
            text = "Please select from the dropdown boxes below the devices you use",
            )

        main_title.place(x = 20, y = titles_y_pos)
        titles_y_pos += 50

        instruction_titles = ["You can select up to 10 devices",
                              "Click next once you are done"
                              ]

        for instruction in instruction_titles:

            explanation_title = ttk.Label(
                self,
                text = instruction,
                )

            explanation_title.place(x = 20, y = titles_y_pos)
            titles_y_pos += 50

        y_pos = titles_y_pos

        # Source: https://generatorist.com/list-of-electric-appliances-their-wattage-usage

        # rated_watts: the amount of power that is needed to run the device
        # surge_watts: the amount of power needed to start up the device

        # this dictionary stores an electrical item as the key, then for the value section it stores the item's rated and surge watt usage
        devices = {"item":["rated_watts","surge_watts"],
                    "Ceiling Fan":[60,70],
                    "Central AC (10,000 BTU)":[1500,4500],
                    "Central AC (24,000 BTU)":[3800,11400],
                    "Central AC (40,000 BTU)":[6000,6700],
                    "Dehumidifier":[240, 0],
                    "Electric Heater (Fan)":[2000,1000],
                    "Electric Thermal Radiator":[500,0],
                    "Electric Water Heater":[4000,0],
                    "Electric Water Heater (Immersion)":[3000,0],
                    "Electricater Heater (Tankless)":[6600,2200],
                    "Evaporative AC":[2600,0],
                    "Furnace Fan Blower (1/2 HP)":[800,2350],
                    "Furnace Fan Blower (1/3 HP)":[700,1400],
                    "Garage Door Opener (1/2 HP)":[875,2350],
                    "Heat Pump":[4700,4500],
                    "Humidifier (13 Gal.)":[175,0],
                    "Light Bulb (Common)":[75,0],
                    "Light Bulb (LED)":[9,0],
                    "Night Light":[1,0],
                    "Oversinkater Heater (Handash)":[3000,0],
                    "Space Heater":[1800,0],
                    "Sump Pump (1/2 HP)":[1050,	2150],
                    "Sump Pump (1/3 HP)":[800,1300],
                    "Tube Light (1500mm)":[22,0],
                    "Well Water Pump (1/2 HP)":[1000,2100],
                    "Window AC (10,000 BTU)":[1200,3600],
                    "Window AC (12,000 BTU)":[3250,9750],
                    "Air Fryer":[1500,0],
                    "Coffee Maker":[1000,0],
                    "Cooker Hood":[20,10],
                    "Deep Freezer":[500,1500],
                    "Dishwasher":[1500,1500],
                    "Electric Can Opener":[170,0],
                    "Electric Kettle":[1200,3000],
                    "Electric Oven":[2150,0],
                    "Electric Stove (8 Element)":[2100,0],
                    "Espresso Coffee Machine":[1300,200],
                    "Food Dehydrator":[800,0],
                    "Food Processor/Blender":[400,0],
                    "Fryer":[1,000,0],
                    "Hotater Dispenser":[1200,100],
                    "Induction Hob (Per Hob)":[1400,400],
                    "Microwave":[1000,0],
                    "Modern Fridge (2001-2020)":[400,600],
                    "Percolator":[800,300],
                    "Pressure Cooker":[700,0],
                    "Refrigerator / Freezer":[700,2200],
                    "Rice Cooker":[200,500],
                    "Sandwich Maker":[700,300],
                    "Side-by-Side Fridge":[800,1200],
                    "Slow Cooker":[160,20],
                    "Smart Fridge":[500,750],
                    "Steriliser":[650,0],
                    "Toaster":[850,0],
                    "Water Dispenser":[100,0],
                    "Water Filter & Cooler":[70,30],
                    "Wine Cooler (18 Bottles)":[83,0],
                    "Bathroom Towel Heater":[60,90],
                    "Clothes Dryer (Electric)":[5400,6750],
                    "Clothes Dryer (Gas)":[700,1800],
                    "Curling Iron":[1500,0],
                    "Electric Shaver":[15,20],
                    "Extractor Fan":[12,0],
                    "Hair Dryer":[1250,0],
                    "Heated Bathroom Mirror":[50,50],
                    "Iron":[1200,0],
                    "Power Shower":[7500,10500],
                    "Steam Iron":[2200,300],
                    "Straightening Iron":[75,300],
                    "Vacuum Cleaner":[200,200],
                    "Washing Machine":[1150,2250],
                    "Amazon Echo":[3,0],
                    "Amazon Echo Show":[2,2],
                    "Apple TV":[3,3],
                    "AV Receiver":[450,0],
                    "Computer Monitor":[25,5],
                    "Desktop Computer":[100,350],
                    "Guitar Amplifier":[20,10],
                    "Home Internet Router":[5,15],
                    "Home Phone":[3,5],
                    "Home Sound System":[95,0],
                    "Laptop":[50,0],
                    "Mi Box":[5,2],
                    "Monitor":[250,0],
                    "Nintendo Switch AC Adapter":[7,33],
                    "Playstation":[485,5],
                    "Set Top Box":[27,3],
                    "Stereo":[450,0],
                    "Television (22 LED)":[17,0],
                    "Television (49 LED)":[85,0],
                    "Television (82 LED)":[230,65],
                    "Television (CRT)":[500,0],
                    "VCR / DVD Player":[100,0],
                    "Video Game System":[40,0],
                    "Xbox One":[50,60],
                    "2-Way Radio (12A)":[360,0],
                    "2-Way Radio (23A)":[840,0],
                    "2-Way Radio (35A)":[960,0],
                    "Air Purifier":[25,5],
                    "Cell Phone Battery Charger":[25,0],
                    "Clock Radio":[200,0],
                    "Copy Machine":[1600,0],
                    "DAB Mains Radio":[5,4],
                    "Electric Blanket":[200,0],
                    "Electric Doorbell Transformer":[2,0],
                    "Electric Mower":[1500,0],
                    "Electric Trimmer":[300,500],
                    "EV Home Charger":[1600,1800],
                    "Fan (Pedestal)":[50,10],
                    "Fan (Table)":[10,15],
                    "Fan (Wall)":[45,15],
                    "Fax":[80,0],
                    "Garage Door Opener (1/2 HP)":[875,2350],
                    "Outdoor Light String":[250,0],
                    "Paper Shredder":[200,220],
                    "Printer (Inkjet)":[20,10],
                    "Printer (Laser)":[600,200],
                    "Projector":[220,270],
                    "Scanner":[10,18],
                    "Security System":[500,0],
                    "Sewing Machine":[70,10],
                    "Tablet Charger":[10,5],
                    "Treadmill":[280,900],
                    "Water Feature":[35,0]}

        # creates a list of all the electronic items from the dictionary
        dev_list = []
        
        for item in devices:
            if item != "item":
                dev_list.append(item)

        # creates a list of all the items that the user has selected
        devices_calc_list = []

        # adds items from the selected dropdown boxes into the list above
        def on_select(event):
            selected_device = devices_list.get()
            devices_calc_list.append(selected_device)
            print(devices_calc_list)

        def on_select_two(event):
            selected_device = devices_list_two.get()
            devices_calc_list.append(selected_device)
            print(devices_calc_list)

        def on_select_three(event):
            selected_device = devices_list_three.get()
            devices_calc_list.append(selected_device)
            print(devices_calc_list)

        def on_select_four(event):
            selected_device = devices_list_four.get()
            devices_calc_list.append(selected_device)
            print(devices_calc_list)

        def on_select_five(event):
            selected_device = devices_list_five.get()
            devices_calc_list.append(selected_device)
            print(devices_calc_list)

        def on_select_six(event):
            selected_device = devices_list_six.get()
            devices_calc_list.append(selected_device)
            print(devices_calc_list)

        def on_select_seven(event):
            selected_device = devices_list_seven.get()
            devices_calc_list.append(selected_device)
            print(devices_calc_list)

        def on_select_eight(event):
            selected_device = devices_list_eight.get()
            devices_calc_list.append(selected_device)
            print(devices_calc_list)

        def on_select_nine(event):
            selected_device = devices_list_nine.get()
            devices_calc_list.append(selected_device)
            print(devices_calc_list)

        def on_select_ten(event):
            selected_device = devices_list_ten.get()
            devices_calc_list.append(selected_device)
            print(devices_calc_list)

        # Device No. 1
        devices_list = ttk.Combobox(
                self,
                width = 30,
                textvariable = StringVar()
                )

        devices_list.place(x = 100, y = y_pos)

        devices_list['values'] = dev_list

        devices_list.current()

        devices_list.bind("<<ComboboxSelected>>", on_select)

        # Device No. 2
        devices_list_two = ttk.Combobox(
                self,
                width = 30,
                textvariable = StringVar()
                )

        devices_list_two.place(x = 100, y = y_pos + 30)

        devices_list_two['values'] = dev_list

        devices_list_two.current()

        devices_list_two.bind("<<ComboboxSelected>>", on_select_two)

        # Device No. 3
        devices_list_three = ttk.Combobox(
                self,
                width = 30,
                textvariable = StringVar()
                )

        devices_list_three.place(x = 100, y = y_pos + 60)

        devices_list_three['values'] = dev_list

        devices_list_three.current()

        devices_list_three.bind("<<ComboboxSelected>>", on_select_three)

        # Device No. 4
        devices_list_four = ttk.Combobox(
                self,
                width = 30,
                textvariable = StringVar()
                )

        devices_list_four.place(x = 100, y = y_pos + 90)

        devices_list_four['values'] = dev_list

        devices_list_four.current()

        devices_list_four.bind("<<ComboboxSelected>>", on_select_four)

        # Device No. 5
        devices_list_five = ttk.Combobox(
                self,
                width = 30,
                textvariable = StringVar()
                )

        devices_list_five.place(x = 100, y = y_pos + 120)

        devices_list_five['values'] = dev_list

        devices_list_five.current()

        devices_list_five.bind("<<ComboboxSelected>>", on_select_five)

        # Device No. 6
        devices_list_six = ttk.Combobox(
                self,
                width = 30,
                textvariable = StringVar()
                )

        devices_list_six.place(x = 100, y = y_pos + 150)

        devices_list_six['values'] = dev_list

        devices_list_six.current()

        devices_list_six.bind("<<ComboboxSelected>>", on_select_six)

        # Device No. 7
        devices_list_seven = ttk.Combobox(
                self,
                width = 30,
                textvariable = StringVar()
                )

        devices_list_seven.place(x = 100, y = y_pos + 180)

        devices_list_seven['values'] = dev_list

        devices_list_seven.current()

        devices_list_seven.bind("<<ComboboxSelected>>", on_select_seven)

        # Device No. 8
        devices_list_eight = ttk.Combobox(
                self,
                width = 30,
                textvariable = StringVar()
                )

        devices_list_eight.place(x = 100, y = y_pos + 210)

        devices_list_eight['values'] = dev_list

        devices_list_eight.current()

        devices_list_eight.bind("<<ComboboxSelected>>", on_select_eight)

        # Device No. 9
        devices_list_nine = ttk.Combobox(
                self,
                width = 30,
                textvariable = StringVar()
                )

        devices_list_nine.place(x = 100, y = y_pos + 240)

        devices_list_nine['values'] = dev_list

        devices_list_nine.current()

        devices_list_nine.bind("<<ComboboxSelected>>", on_select_nine)

        # Device No. 10
        devices_list_ten = ttk.Combobox(
                self,
                width = 30,
                textvariable = StringVar()
                )

        devices_list_ten.place(x = 100, y = y_pos + 270)

        devices_list_ten['values'] = dev_list

        devices_list_ten.current()

        devices_list_ten.bind("<<ComboboxSelected>>", on_select_ten)

class results_Screen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        style = ttk.Style()
        style.configure("Heading.TLabel", background = "blue", foreground = "white", font = ("ariel", 20, "bold"))
        
        title = ttk.Label(
            self,
            text = "TechCheck's Power Usage Quiz",
            style = "Heading.TLabel",
            width = 105
            )

        title.place(x = 0, y = 2)

        style.configure("TButton", background = "black", foreground = "white", font = ("ariel", 16, "bold"))

        #start_button = ttk.Button(
            #self,
            #text = "Start Again",
            #command = lambda:controller.show_frame(start_Screen),
            #width = 10
            #)

        #start_button.place(x = 20, y = 50)

        end_button = ttk.Button(
            self,
            text = "End Quiz",
            command = lambda:quiz.destroy(),
            width = 10
            )

        end_button.place(x = 20, y = 50)

        #back_button = ttk.Button(
            #self,
            #text = "Back",
            #command = lambda:controller.show_frame(devices_Screen),
            #width = 5
            #)

        #back_button.place(x = 700, y = 50)

        titles_y_pos = 110
        
        main_title = ttk.Label(
            self,
            text = "Thank you for using our Power Usage Quiz, tech responsibly!",
            )

        main_title.place(x = 20, y = titles_y_pos)
        titles_y_pos += 50

        #instruction_titles = ["This is your total initial watt usage if you were to run all your devices at once: " + str(watt_values_list[0]),
                                  #"This is your watt usage if you were to run all your devices at once per second: " + str(watt_values_list[1]),
                                  #"Press Start Again to try another round"
                                  #]

        #for instruction in instruction_titles:

            #explanation_title = ttk.Label(
                #self,
                #text = instruction,
                #)

            #explanation_title.place(x = 20, y = titles_y_pos)
            #titles_y_pos += 50

        #y_pos = titles_y_pos

quiz = Sustainability_Quiz_App()
quiz.mainloop()
