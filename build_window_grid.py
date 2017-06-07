#!/usr/bin/python
from tkinter import ttk
import tkinter as tk
import pypyodbc


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.myParent = master
        self.create_widgets()


    def create_widgets(self):

        # Inventory Column 1
        self.lb_inventory = tk.Label(text="Inventory", justify="center", bg='white')
        self.lb_inventory.place(x=5, y=10, height=23, width=85)

        self.bt_services = tk.Button(text="Services", command=self.bt_services_action, \
                                      justify="left")
        self.bt_services.place(x=11, y=35, height=21, width=85)

        self.bt_servers = tk.Button(text="Servers", command=self.bt_servers_action, \
                                     justify="left")
        self.bt_servers.place(x=11, y=60, height=21, width=85)

        self.bt_instances = tk.Button(text="Instances", command=self.bt_instances_action, \
                                       justify="left")
        self.bt_instances.place(x=11, y=85, height=21, width=85)

        self.bt_databases = tk.Button(text="Databases", command=self.bt_databases_action, \
                                       justify="left")
        self.bt_databases.place(x=11, y=110, height=21, width=85)

        self.bt_jobs = tk.Button(text="Jobs", command=self.bt_jobs_action, \
                                      justify="left")
        self.bt_jobs.place(x=11, y=135, height=21, width=85)

        self.bt_full_inventory = tk.Button(text="Full Inventory", command=self.bt_full_inventory_action, \
                                           justify="left")
        self.bt_full_inventory.place(x=11, y=168, height=21, width=85)

        # Inventory Column 2
        self.bt_server_instance = tk.Button(text="Server\Instance", command=self.bt_server_instance_action, \
                                            justify="left")
        self.bt_server_instance.place(x=102, y=72, height=21, width=85)

        self.bt_instance_database = tk.Button(text="Instance\DB", command=self.bt_instance_database_action, \
                                              justify="left")
        self.bt_instance_database.place(x=102, y=97, height=21, width=85)

        self.bt_jobs_extended= tk.Button(text="Jobs Extended", command=self.bt_jobs_extended_action, \
                                              justify="left")
        self.bt_jobs_extended.place(x=102, y=135, height=21, width=85)


        # Reporting Column
        self.lb_reporting = tk.Label(text="Reporting", justify="center", bg='white')
        self.lb_reporting.place(x=260, y=9, height=23, width=85)

        self.bt_getserversgroup_os_sp = tk.Button(text="Servers Grouped by\nOS and OS Service Pack", \
                                command=self.bt_getserversgroup_os_sp_action, justify="center")
        self.bt_getserversgroup_os_sp.place(x=273, y=37, height=35, width=185)

        self.bt_getinstancesgroup_sqlver = tk.Button(text="Instances Grouped by\nSQL Version", \
                                                  command=self.bt_getinstancesgroup_sqlver_action, justify="center")
        self.bt_getinstancesgroup_sqlver.place(x=273, y=78, height=35, width=185)

        self.bt_getinstancesgroup_sqlver_sqled = tk.Button(text="SQL Instances Grouped By\nSQL Version, Edition", \
                                                     command=self.bt_getinstancesgroup_sqlver_sqled_action, justify="center")
        self.bt_getinstancesgroup_sqlver_sqled.place(x=273, y=119, height=35, width=185)

        self.bt_getinstancesgroup_sqlver_sqled_sqlsp = tk.Button(text="SQL Instances Grouped By\nSQL Version, Edition and SP", \
                                                           command=self.bt_getinstancesgroup_sqlver_sqled_sqlsp_action,
                                                           justify="center")
        self.bt_getinstancesgroup_sqlver_sqled_sqlsp.place(x=273, y=160, height=35, width=185)

        ## Exit button
        self.bt_quit = tk.Button(text="Exit", command=root.destroy)
        self.bt_quit.place(x=374, y=210, height=21, width=85)

    # Inventory Column 1

    def bt_services_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetServerServices", "Server Services Inventory")

    def bt_servers_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetServers", "Server Inventory")

    def bt_instances_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetInstances", "Instances Inventory")

    def bt_databases_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetDatabasesAndSize", "Database Inventory")

    def bt_jobs_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetJobs", "Jobs Inventory")

    def bt_full_inventory_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetInventory", "Full Inventory")

    # Inventory Column 2

    def bt_server_instance_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetServersAndInstances", "Server\Instance Inventory")

    def bt_instance_database_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetInstancesAndDatabases", "Instance\Database Inventory")

    def bt_jobs_extended_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetJobsExt", "Jobs Extended Inventory")

    # Reporting Column

    def bt_getserversgroup_os_sp_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetServersGroup_OS_SP", \
                       "Servers Grouped by OS and OS Service Pack")

    def bt_getinstancesgroup_sqlver_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetInstancesGroup_SQLVer", \
                       "Instances Grouped by SQL Version")

    def bt_getinstancesgroup_sqlver_sqled_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetInstancesGroup_SQLVer_SQLEd", \
                       "SQL Instances Grouped By SQL Version and Edition")

    def bt_getinstancesgroup_sqlver_sqled_sqlsp_action(self):
        show_inventory("DBAdmin", "localhost", "dbo.prGetInstancesGroup_SQLVer_SQLEd_SQLSP", \
                       "SQL Instances Grouped By SQL Version, Edition and Service Pack")


def show_inventory(database, server, stored_procedure, window_title):

    server_string = "Server=" + server + ";"
    database_string = "Database=" + database +";"

    connection = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            + server_string
                            + database_string
                            + "Trusted_Connection=yes;")

    connection_sample = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            + server_string
                            + database_string
                            + "Trusted_Connection=yes;")

    cursor = connection.cursor()
    row_sample = connection_sample.cursor()

    cursor.execute('EXEC ' + stored_procedure)
    row_sample.execute('EXEC ' + stored_procedure)

    column_length = []
    column_height = []
    for row in row_sample:
        for item in row:
            column_length.append(125 + len(str(item))*2)
            column_height.append(str(item).count('\n'))
        row_sample.close()
        break

    row_height = 14 * (max(column_height)+1)
    rows_per_page = 50 - (max(column_height)*10)

    win = tk.Tk()
    win.iconbitmap(r'SDIM_bw_icon.ico')
    win.resizable(width=0, height=0)
    win.wm_title(window_title)

    style = ttk.Style(win)
    style.configure('Treeview', rowheight=row_height)

    tree = ttk.Treeview(win, selectmode='browse', height=rows_per_page)
    tree.pack(side='left')

    vsb = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')

    tree.configure(yscrollcommand=vsb.set)

    column_label_count = 0
    row_data_count = 2
    column_data_count = 0

    column_list = []
    column_name_list = []
    for column in cursor.description:
        column_list.append(column_label_count)
        column_name_list.append(column[0])
        column_label_count += 1

    tree["columns"] = tuple(column_list)

    tree['show'] = 'headings'

    for column in column_list:
        tree.column(str(column), width=column_length[column],  anchor='c')
        tree.heading(str(column), text=column_name_list[column])

    for row in cursor:
        tree.insert("", 'end', values=(row))

    win.mainloop()


root = tk.Tk()
root.iconbitmap(r'SDIM_bw_icon.ico')
root.title('SDIMpy - v0.1b')
root.configure(background='white')

root.resizable(width=0,height=0)

app = Application(master=root)
app.master.minsize(473, 250)
app.master.maxsize(473, 250)

app.mainloop()