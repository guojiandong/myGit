'''
Created on 2015-5-5

@author: hzguojiandong15
'''
import wx
import os
import cPickle

wildcard1 = "All files (*.*)|*.*|" \
            "Python source (*.py; *.pyc)|*.py;*.pyc"
wildcard2 = "Python source (*.py; *.pyc)|*.py;*.pyc|" \
            "All files (*.*)|*.*"

class SubClass(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, 'SubClass', size=(500, 400))
        subPanel = wx.Panel(self, wx.ID_ANY)
        okBtn = wx.Button(subPanel, label='OK', pos=(310, 310))
        cancleBtn = wx.Button(subPanel, label='Cancle', pos=(330, 310))
        okBtn.SetDefault()
        
class SkillEd(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'SkillEditor', size=(950, 800))
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour('White')
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        global Text01, contents
        
        statusBar = self.CreateStatusBar()
        toolBar = self.CreateToolBar()
        bmp01 = wx.Image('one.png', type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        toolBar.AddSimpleTool(wx.NewId(), bmp01, "New", "Long")
        bmp02 = wx.Image('two.png', type=wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        toolBar.AddSimpleTool(wx.NewId(), bmp02, "Back", "Long")
        toolBar.Realize()      
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1, "File")
        openItem = menu1.Append(wx.NewId(), 'Open', 'open')
        menu2 = wx.Menu()
        CopyItem = menu2.Append(wx.NewId(), "Copy", "copy in status")
        CutItem = menu2.Append(wx.NewId(), "cut", "")
        menu2.Append(wx.NewId(), "color", 'color')
        menu2.AppendSeparator()
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import from--001')
        imp.Append(wx.ID_ANY, 'Import from--002')
        menu2.AppendMenu(wx.ID_ANY, 'Import', imp)
        menu2.Append(wx.NewId(), "paste", "")
        menuBar.Append(menu2, "Edit")
        self.SetMenuBar(menuBar)
        
#        #Static TextLabel----------------------------------------------------------------
#        staticTX = wx.StaticText(panel, -1, 'Value01', (580, 100), (60, 20), wx.ALIGN_LEFT)
#        staticTX.SetForegroundColour('white')
#        staticTX.SetBackgroundColour('black')
#        
#        #Text input
#        BasicText = wx.TextCtrl(panel, -1, 'Make it', (660, 100), (100, 20), wx.ALIGN_LEFT)
#        
#        #Bmp button
#        bmpBtn = wx.Image('01.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
#        self.buttonBmp = wx.BitmapButton(panel, -1, bmpBtn, pos=(780, 100))
#        self.Bind(wx.EVT_BUTTON, self.OnClick, self.buttonBmp)
#        
#        #Slider---------------------------------------------------------------------
#        slider = wx.Slider(panel, 100, 25, 1, 100, pos=(600, 200), size=(250, -1), \
#                           style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
#        slider.SetTickFreq(5, 1)
#        
#        #SpinCtrl-------------------------------------------------------------------
#        sc = wx.SpinCtrl(panel, -1, "", (600, 250), (80, -1))
#        sc.SetRange(1, 100)
#        sc.SetValue(5)
#        
#        #CheckBox-------------------------------------------------------------------
#        wx.CheckBox(panel, -1, 'Alpha', (600, 270), (150, 20))
#        wx.CheckBox(panel, -1, 'Beta', (600, 290), (150, 20))
#        wx.CheckBox(panel, -1, 'Gamma', (600, 310), (150, 20))
#        
##        #RadioButton-------------------------------------------------------------------
##        radio01 = wx.RadioButton(panel, -1, 'one', pos=(600, 350), style=wx.RB_GROUP)
##        radio02 = wx.RadioButton(panel, -1, 'two', pos=(600, 370))
##        radio03 = wx.RadioButton(panel, -1, 'three', pos=(600, 390))
#
#        #RadioBox-------------------------------------------------------------------
#        
#        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
#        wx.RadioBox(panel, -1, 'Radio Box', (600, 350), wx.DefaultSize, sampleList, 2, wx.RA_SPECIFY_COLS)
#        
#        #ListBox-------------------------------------------------------------------
#        sampleListbox = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
#        listBox = wx.ListBox(panel, -1, (800, 290), (80, 120), sampleListbox, wx.LB_SINGLE)
#        listBox.SetSelection(3)
#        
#        #ListBoxxiala-------------------------------------------------------------------
#        sampleListboxLa = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
#        wx.StaticText(panel, -1, 'Select one:', (600, 500))
#        wx.Choice(panel, -1, (680, 500), choices=sampleListboxLa)
#        
      
        vbox = wx.BoxSizer(wx.HORIZONTAL)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        contents = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox1.Add(contents, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox1, proportion=2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        
        vbox.Add((-1, 25))
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        Text01 = wx.TextCtrl(panel)
        btnOpen = wx.Button(panel, label='Open')
        btnSave = wx.Button(panel, label='Save')
        hbox2.Add(Text01, proportion=2)
        hbox2.Add(btnOpen, proportion=0)
        hbox2.Add(btnSave, proportion=0)
        vbox.Add(hbox2, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, CopyItem)
        self.Bind(wx.EVT_BUTTON, self.OnOpen, btnOpen)
        self.Bind(wx.EVT_BUTTON, self.OnSave, btnSave)
        self.Bind(wx.EVT_MENU, self.OnClickSubMenu, CutItem)
        
        #panel.SetSizer(vbox)
        panel.SetSizerAndFit(vbox)
        
        
    def OnQuit(self, e):
        self.Close()
    def OnClickSubMenu(self, e):
        print 'OnClickSubMenu'
        dialog = SubClass()
        #dialog.Destroy()
        
    def OnClose(self, e):
        dial = wx.MessageBox('Are you sure to Quit?', 'Confirm', wx.OK | wx.CANCEL)
        if dial == wx.OK:
            self.Destroy()
        else:
            pass
        
    def OnOpen(self, e):
        dialog = wx.FileDialog(self, 'Open File....', os.getcwd(), \
                               style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR, wildcard=wildcard1)
        if dialog.ShowModal() == wx.ID_OK:
            self.filename = dialog.GetPath()
            Text01.SetValue(self.filename)
            self.OnRead()
            self.SetTitle(self.filename)
        dialog.Destroy()
    def OnSave(self, e):
        dlg = wx.FileDialog(self, message='select the save file style', defaultFile='', wildcard=wildcard2, style=wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            
            filename = dlg.GetPath()
            file = open(filename, 'w')
            file.write(contents.GetValue())
            file.close()
            Text01.SetValue(filename)

    def OnRead(self):
        if self.filename:
            try:
                fd = open(self.filename, 'r')
                #data = cPickle.load(fd)
                line = fd.read()
                contents.SetValue(line)
                print line
                fd.close()
            except:
                wx.MessageBox("%s is not a match file." % self.filename, "oopsS!", \
                               style=wx.OK | wx.ICON_EXCLAMATION)
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = SkillEd(parent=None, id= -1)
    frame.Show()
    app.MainLoop()
        
        
    
