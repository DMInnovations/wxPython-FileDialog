# Created By: DMInnovations

import wx

class YourClass(wx.Frame):
  # Your code

  def fileDialog(self, event):
    # FileDialog = Parent (window)*, Title*, Directory, Default File, File Type*
    yourFileDialogName = wx.FileDialog(self, "Your message/title/caption", "", "", "Files (*.file; *.file) | *.file; *.file", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)'

    yourFileDialogName.ShowModal()
