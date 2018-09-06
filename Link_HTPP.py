################# A hyperlink widget############################ 
"""
The first example will create a hyperlink. The hyperlink widget will be based on an existing wx.lib.stattext.GenStaticText widget. 
"""

import wx
from wx.lib.stattext import GenStaticText
import webbrowser

class Link(wx.Button):


    def __init__(self, *args, **kw):

        super(Link, self).__init__(*args, **kw)
        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)
        self.Bind(wx.EVT_MOTION, self.OnMouseEvent)

    def SetUrl(self, url):
        self.url = url


    def OnMouseEvent(self, e):

        if e.Moving():

            self.SetCursor(wx.Cursor(wx.CURSOR_HAND))


        elif e.LeftUp():

            webbrowser.open_new(self.url)

        else:
            self.SetCursor(wx.NullCursor)


        e.Skip()