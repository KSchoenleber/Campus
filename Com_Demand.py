import wx 

Liste_Fixed = ["Commodity price (Euro/MWh)", "Maximum commodity use", "Maximum commodity use per step"]
Liste_Timeseries = ["Supp Buy", "Supp sell" ] 

class   Demand (wx.Frame):

      def __init__(self):

           wx.Frame.__init__(self, None, title="Gas",size=(680, 334))
           self.Centre()
           panel = wx.Panel(self)

           Choose = ['Fixed Price', 'Timeseries']
           cb = wx.ComboBox(panel, pos=(20, 15), size =(630, 50), choices=Choose, style=wx.CB_READONLY) 



           cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)


           
           self.Show ()  

      # e: event 
      # More about: https://wxpython.org/Phoenix/docs/html/wx.CommandEvent.html 
      def OnSelect(panel, e): 
        i = e.GetSelection () 
        if i == 0: 
          for j in range (0 , len (Liste_Fixed)): 
            wx.StaticText(panel, label=Liste_Fixed[j], pos= (24, 60+30*j )) 
            wx.TextCtrl(panel, pos= (288, 60+30*j), size=(100,20))


        #i = e.GetString()
        #self.st.SetLabel(i)
