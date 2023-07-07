# Created by: DMInnovations

import wx

class YourClass(wx.Frame):
        # Your code with def __init__()

    # Create the dialog for open
    def openDialog(self, event):
        # FileDialog = Parent (window)*, Title*, Directory, Default File, File Type*
        yourOpenFileButton = wx.FileDialog(self, "Your Dialog Caption/Title", "", "", "File Name (*.file) | *.file", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        yourOpenFileButton.ShowModal()
