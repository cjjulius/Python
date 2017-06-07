#!/usr/bin/python

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):

        self.frame_left = tk.Frame(root)
        self.frame_left.pack(side="left", anchor="nw")

        self.frame_right = tk.Frame(root)
        self.frame_right.pack(side="right", fill='both')

        self.bt_services = tk.Button(text="Services", command=self.bt_services_action, justify="left")
        #self.bt_services["text"] = "Services"
        #self.bt_services["command"] = self.bt_services_action
        self.bt_services.pack(side="top")

        self.bt_servers = tk.Button(text="Servers", command=self.bt_servers_action, justify="left")
        #self.bt_servers["text"] = "Servers"
        #self.bt_servers["command"] = self.bt_servers_action
        self.bt_servers.pack(side="top")

        self.bt_instances = tk.Button(text="Instances", command=self.bt_instances_action, justify="left")
        # self.bt_servers["text"] = "Servers"
        # self.bt_servers["command"] = self.bt_servers_action
        self.bt_instances.pack(side="top")

        self.bt_quit = tk.Button(self.frame_right, text="Exit", command=root.destroy)
        self.bt_quit.pack(side="bottom")

    def bt_services_action(self):
        print("Show Services!")

    def bt_servers_action(self):
        print("Show Servers!")

    def bt_instances_action(selfs):
        print("Show Instances!")


root = tk.Tk()
app = Application(master=root)
app.master.maxsize(1000, 400)
app.mainloop()

