#!/usr/bin/env python

import win32com.client # Allows to connect to Windows object using COM objects.
import os, time # Allows us to work with time and os functions.

# Set the Excel file name, working directory and path
old_file_name = '01032016 to 18032016 ratc.xlsx'
working_dir = r"Y:\ProductionDocuments\RATC Data" + os.sep
old_file_path = os.path.join(working_dir, old_file_name)

xlApp = win32com.client.Dispatch("Excel.Application")
xlApp.Visible = True

workbook = xlApp.Workbooks.Open(old_file_path)

time.sleep(10)
#1200 = 20 mins should be enough time for the bbg excel to load completely
workbook.Save()
workbook.Close(SaveChanges=True)

xlApp.Quit()


