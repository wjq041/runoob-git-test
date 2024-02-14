import clr
clr.AddReference("wpf\PresentationFramework")
from System.IO import *
from System.Windows.Markup import XamlReader
from System.Windows import *
from System.Threading import Thread, ThreadStart, ApartmentState
from System.Windows.Controls import *

class MyWindow(Window):
    def __init__(self):
        try:
            stream = StreamReader('MainWindow.xaml')
            self.window = XamlReader.Load(stream.BaseStream)
            ButtoninXAML = LogicalTreeHelper.FindLogicalNode(self.window, "button1")
            ButtoninXAML.Click +=  RoutedEventHandler(self.Button_Click)
            Application().Run(self.window)
        except Exception as ex:
            print(ex)
    def Button_Click(self, sender, e):
        print('clicked')


if __name__ == '__main__':
    thread = Thread(ThreadStart(MyWindow))
    thread.SetApartmentState(ApartmentState.STA)
    thread.Start()
    thread.Join()
