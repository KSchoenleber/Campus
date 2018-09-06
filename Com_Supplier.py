import wx 
class   Supply (wx.Frame):

      def __init__(self):

           wx.Frame.__init__(self, None, title="Gas",size=(680, 334))
           self.Centre()
           panel = wx.Panel(self)

           Choose = ['Fixed Price', 'Timeseries']
           cb = wx.ComboBox(panel, pos=(20, 15), size =(630, 50), choices=Choose, style=wx.CB_READONLY) 

           self.st = wx.StaticText(panel, label='', pos=(24, 50 ))
 

           cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)

           Liste_Fixed = ["Commodity price (Euro/MWh)", "Maximum commodity use", "Maximum commodity use per step"]

           Liste_Timeseries = ["Supp Buy", "Supp sell" ] 


           #txt = wx.StaticText(panel, label="Gas-CHP")

           self.Show ()  


      def OnSelect(self, e): 

        i = e.GetString()
        self.st.SetLabel(i)




      


