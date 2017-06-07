from tkinter import ttk
import tkinter as tk
import pypyodbc



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

    row_sample.execute('EXEC ' + stored_procedure)
    cursor.execute('EXEC ' + stored_procedure)

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

    print(max(column_height)+1)
    print(rows_per_page)

    win = tk.Tk()
    win.resizable(width=0, height=0)
    win.wm_title(window_title)

    tree = ttk.Treeview(win, selectmode='browse', height=rows_per_page)
    tree.pack(side='left')

    vsb = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')

    tree.configure(yscrollcommand=vsb.set)

    ttk.Style().configure('Treeview', rowheight=row_height)

    column_label_count = 0

    row_data_count = 2
    column_data_count = 0

    column_list = []
    column_name_list = []
    for column in cursor.description:
        column_list.append(column_label_count)
        column_name_list.append(column[0])
        column_label_count += 1
    print(column_list)
    print(column_name_list)

    tree["columns"] = tuple(column_list)

    print(tree["columns"])

    tree['show'] = 'headings'

    print(column_length)
    print(column_height)

    for column in column_list:
        tree.column(str(column), width=column_length[column],  anchor='c')
        tree.heading(str(column), text=column_name_list[column])

    for row in cursor:
        tree.insert("", 'end', values=(row))

    win.mainloop()

show_inventory("DBAdmin", "localhost", "dbo.prGetInstances", "Instance Inventory")