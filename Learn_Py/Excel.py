from win32com.client import Dispatch

xlApp = Dispatch('Excel.Application')

result = xlApp.Run("test1.xlsx") 

xlApp.Quit()
