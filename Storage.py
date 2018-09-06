import wx 
class Storage (wx.Frame):
      """"""

      #----------------------------------------------------------------------
      def __init__(self):
           """Constructor"""
           wx.Frame.__init__(self, None, title="Storage", size=(680, 334))
           self.Centre()
           panel = wx.Panel(self)
           self.Show ()  