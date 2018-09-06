import wx
from wx.lib.floatcanvas import FCObjects 
#from Arrow_Class import DrawObject

# Link with HTTP 
from Link_HTPP import Link  
from Process_Com import Process
from Com_Supplier import Supply
from Com_Demand import Demand
from Storage import Storage 


## Main window container

class Main_window(wx.Frame):

    def __init__(self, parent, title):
        super(Main_window, self).__init__(parent, title=title ) 
        
        self.Maximize(True)
        self.Centre()
        self.Tool_Bar()

        # Create a panel and notebook (tabs holder)
        panel = wx.Panel(self)
        nb = wx.Notebook(panel)
 
        # Create the tab windows 
        tab1 = TabOverview(nb)
        tab2 = TabRES(nb)
        tab3 = TabPreview(nb)
        tab4 = TabFour(nb)
        tab5 = TabFive(nb)

        # Add the tabs and name them.
        nb.AddPage(tab1, "Overview")
        nb.AddPage(tab2, "RES")
        nb.AddPage(tab3, "Preview")
        nb.AddPage(tab4, "Parameter")
        nb.AddPage(tab5, "Info")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        panel.SetSizer(sizer)

    
    def Tool_Bar (self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        fileItem_2 = fileMenu.Append(wx.ID_EXIT, 'Downlood', 'Downlood')

        menubar.Append(fileMenu, '&File')

        self.SetMenuBar(menubar)


## Tabs

# General inforamtion about the App
class TabOverview(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour("gray")

        Lehrstuhl = wx.StaticBitmap(self, wx.ID_ANY,
                                    wx.Bitmap("Fac.jpg", wx.BITMAP_TYPE_ANY))
        Lehrstuhl.SetPosition((0, 50))
        Prof = wx.StaticBitmap(self, wx.ID_ANY,
                               wx.Bitmap("Profi.jpg", wx.BITMAP_TYPE_ANY))
        Prof.SetPosition((890, 50)) 

        link_wid = Link(self, label="Lehrstuhl für Erneuerbare und Nachhaltige"
                                    "Energiesysteme_TUM", size=(720, 50))
        link_wid.SetUrl('http://www.ens.ei.tum.de/homepage/')
        link_wid = Link(self ,label="Prof. Dr. Thomas Hamacher",
                        size=(628, 50), pos=(730, 0))
        link_wid.SetUrl('http://www.professoren.tum.de/en/hamacher-thomas/')


# Main input window with reference energy system (RES) representation     
class TabRES(wx.Panel):

    def __init__(self, parent):

        wx.Panel.__init__(self, parent)

        # Buttons Explanation & Run 
        btn2_0 = wx.Button(self, label="Explanation", size=(1000 , 100))
        btn2_1 = wx.Button(self, label="Run", size=(348 , 100),pos=(1010, 0))
        btn2_2 = wx.Button(self, label="TBF", size=(1358 , 50), pos=(0, 608))


        # Buttons for Energy commodities
        #btn2_3 = wx.Button(self, label="Supply", size=(350 , 50), pos=(0, 110))
        btn2_4 = wx.Button(self, label="Gas", size=(110 , 50), pos=(0, 160))
        btn2_5 = wx.Button(self, label="Oil", size=(110 , 50), pos=(240, 160))
        
        supply_Buttons = [btn2_4, btn2_5]

        # Buttons for Process_Com 
        btn2_6 = wx.Button(self, label="PV", size=(110 , 50), pos=(384, 230))
        btn2_7 = wx.Button(self, label="Wind", size=(110 , 50), pos=(384, 290)) 
        btn2_8 = wx.Button(self, label="Sol-Thermal", size=(110 , 50),
                           pos=(384, 350))
        btn2_9 = wx.Button(self, label="Bio-CHP", size=(110 , 50),
                           pos=(384, 410))
        btn2_10 = wx.Button(self, label="Gas-CHP", size=(110 , 50),
                            pos=(384, 470))
        btn2_11 = wx.Button(self, label="TBF", size=(110 , 50), pos=(384, 530)) 

        process_Buttons = [btn2_6, btn2_7 ,btn2_8 , btn2_9, btn2_10, btn2_11]

        # Buttons for Demand 
        #btn2_12 = wx.Button(self, label="Demand", size=(830, 50),
        #                    pos=(528, 110))
        btn2_13 = wx.Button(self, label="Elec", size=(110, 50), pos=(528, 160))
        btn2_14 = wx.Button(self, label="Heat", size=(110, 50), pos=(823, 160))
        btn2_15 = wx.Button(self, label="Cold", size=(110, 50),
                            pos=(1128, 160))	 

        demand_Buttons = [btn2_13, btn2_14, btn2_15]

        
        # Buttons_Stock  (between Elec/Heat **  Heat/Cold ** Elec/Cold) 
        # Row Nr: 1: 
        btn2_16 = wx.Button(self, label="Battery", size=(137.5 , 23), pos=(672, 274.5))       
        btn2_17 = wx.Button(self, label="Cold-KV", size=(110 , 23), pos=(1248, 274.5))  

        # Row Nr 2:
        btn2_18 = wx.Button(self, label="Heat-Pump", size=(137.5 , 23), pos=(672, 334.5))     
        btn2_19 = wx.Button(self, label="ABS", size=(137.5 , 23), pos=(972, 334.5))  

        # Row Nr 3: 
        btn2_20 = wx.Button(self, label="Compressor cooler", size=(137.5 , 23), pos=(672, 393.5)) 

        # Row Nr 4: 
        btn2_21 = wx.Button(self, label="Both", size=(137.5 , 23), pos=(672, 453.5))  

        # Row Nr 5:  (change it Later) 
        btn2_22 = wx.Button(self, label="Heat-KV", size=(137.5 , 23), pos=(972, 513.5))  

        storage_Buttons = [btn2_16, btn2_17, btn2_18, btn2_19, btn2_20, btn2_21, btn2_22 ]

        # Line_Vertical21
        line2_1 = wx.StaticLine(self , pos=(53,210), size=(4,398) , style= wx.LI_VERTICAL)
        line2_2 = wx.StaticLine(self , pos=(293,210), size=(4,398) , style= wx.LI_VERTICAL)
        line2_3 = wx.StaticLine(self , pos=(582,210), size=(4,398) , style= wx.LI_VERTICAL)
        line2_4 = wx.StaticLine(self , pos=(877,210), size=(4,398) , style= wx.LI_VERTICAL)
        line2_5 = wx.StaticLine(self , pos=(1182,210), size=(4,398) , style= wx.LI_VERTICAL)
   
        # Line_Horizental: 
        line_H_2_1 = wx.StaticLine(self , pos=(53,495), size=(384,4) , style=wx.LI_HORIZONTAL) 

        ####################################################################
        # clicked Button -> Open New Fenster 

        for i in range(0, len(supply_Buttons)): 
            supply_Buttons[i].Bind(wx.EVT_BUTTON, self.OnA)

        for i in range (0, len(process_Buttons)): 
            process_Buttons[i].Bind(wx.EVT_BUTTON, self.OnB) 

        for i in range (0, len(demand_Buttons)): 
            demand_Buttons[i].Bind(wx.EVT_BUTTON, self.OnC)

        for i in range (0, len(storage_Buttons)):
            storage_Buttons[i].Bind(wx.EVT_BUTTON, self.OnD) 



        
        #print (btn2_12.GetLabel () )
    
    # Function for Supply_Buttons  
    # Go to Com_Supplier.py

    def OnA(self, event):
        frame = Supply() 
        frame.Show()           

    # Function for Process_Buttons 
    # Go to Process_Com.py 
    def OnB(self, event ):

        frame = Process ()
        frame.Show()

    # Function for Demand_Buttons 
    # Go to Com_Demand.py 
    def OnC(self, event):
        frame = Demand()
        frame.Show()   

    # Function for Storage_Buttons 
    # Go to Storage.py 
    def OnD(self, event):
        frame = Storage()
        frame.Show()   
    


    #Arrow ([200,100],100, 50,LineColor = "Black", LineStyle = "Solid", LineWidth = 2, ArrowHeadSize = 8, ArrowHeadAngle = 30, InForeground = False)

 ############# Tab3 : Preview 
 
class TabPreview(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        Arrow = wx.lib.floatcanvas.FCObjects.Arrow ((20,350),100,50,LineColor = "Black", LineStyle = "Solid", LineWidth = 2, ArrowHeadSize = 8, ArrowHeadAngle = 30, InForeground = False)  
        #DrawObject(Arrow) 
 

############# Tab4 : Parameter    
class TabFour(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

############# Tab5 : Info 

class TabFive (wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)


#
def main():

    app = wx.App()
    ex = Main_window(None, title='Lehrstuhl_Erneuerbare und Nachhaltige Energiesysteme_TUM')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()