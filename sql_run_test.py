import pypyodbc
import tkinter


cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=localhost;"
                        "Database=DBAdmin;"
                        "Trusted_Connection=yes;")


def display_servers():
    cursor = cnxn.cursor()
    cursor.execute('EXEC dbo.prGetInstances')



    root = tkinter.Tk()

    column_label_count = 0

    row_data_count = 2
    column_data_count = 0

    for column in cursor.description:
        tkinter.Label(root, text=str(column[0]).upper(), borderwidth=2).grid(row=1, column=column_label_count)
        column_label_count += 1
        print(column[0])

    for row in cursor:
        for column in row:
            tkinter.Label(root, text=str(column), borderwidth=2).grid(row=row_data_count, column=column_data_count)
            column_data_count += 1
        column_data_count = 0
        row_data_count += 1

    root.mainloop()

display_servers()





#print ([column[0] for column in cursor.description])



# for row in cursor:
#     print('row = %r' % (row,))
