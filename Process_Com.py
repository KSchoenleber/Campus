# You need to read Size_myText.py to know the size of your Text. This help you to know the position of your Text in the Fenster.

import wx 
class Process (wx.Frame):
      """"""

      #----------------------------------------------------------------------
      def __init__(self):
           """Constructor"""
           wx.Frame.__init__(self, None,title="Gas-CHP", size=(680, 334))

           self.Centre()
           panel = wx.Panel(self)
           
           # Seperation_Line between Economic and Technical 
           wx.StaticLine(panel , pos=(338,0), size=(4,334) , style= wx.LI_VERTICAL)

           # Text (Economic and Technical)
           txt_1 = wx.StaticText(panel, label="Economic", pos= (134.5, 14))
           txt_2 = wx.StaticText(panel, label="Technical", pos= (478.5, 14)) 
           # Change Text_Colour 
           txt_1.SetForegroundColour((204,0,102)) 
           txt_2.SetForegroundColour((204,0,102))
           

           Liste_Economic = ["Installed capacity (MW)", "Lifetime of inst-cap (years)", "Minimum capacity (MW)", "Maximum capacity (MW)", "Investment cost (Euro/MW)", "Annual fix cost (Euro/MW/a)", "Variable costs (Euro/MWh)"]
           

           Liste_Technical = ["Maximal power gradient (1/h)","Minimum load fraction", "Depreciation period (a)", "Area use per capacity (m^2/MW)"]

           
           self.Show ()  

           for i in range (0 , len (Liste_Economic)): 

            wx.StaticText(panel, label=Liste_Economic[i], pos= (10, 40+30*i))
            wx.TextCtrl(panel, pos= (188 , 40+30*i), size=(100,20)) 

           for i in range (0 , len (Liste_Technical)): 

            wx.StaticText(panel, label=Liste_Technical[i], pos= (348, 40+30*i )) 
            wx.TextCtrl(panel, pos= (528, 40+30*i), size=(100,20))

            #wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos= (0 , b+2), size=(210,15))

            self.Show ()  



          






           






   





