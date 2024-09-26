from enum import Enum 
 
class Gui(object) : 
 
  class WidgetType(Enum) : 
    PushButton = 0 
    ToolButton = 1 
    ProgressBar = 2 
    LineEdit = 3 
    Dial = 4 
    Slider = 5 
    CheckBox = 6 
    Label = 7 
    OpenFileButton = 8 
    ToolButtonWithLed = 9 
    ToolButtonWithProgress = 10 
    VerticalSlider = 11 
    HorizontalSlider = 12 
    DigitalIOControl = 13 
    AnalogIOControl = 14 
    CurrentGcodesWidget = 15 
    MdiLineWidget = 16 
    PythonConsole = 17 
    GCodeList = 18 
    SimGLWidget = 19 
    OffsetTable = 20 
    GroupBox = 21 
    Frame = 22 
    TabWidget = 23 
    ScrollArea = 24 
    Splitter = 25 
    FreeLayout = 26 
    HorizontalLayout = 27 
    VerticalLayout = 28 
    GridLayout = 29 
    FormLayout = 30 
 
  def __init__(self, comm) : 
    self.comm = comm 
    self.createObjects() 
 
  def getIds(self) : 
    return [i for i in self.comm.sendAndWait( "gui_getWidgetsId:" ).split(";")] 
 
  class Widget(object) : 
 
    def __init__(self, name, comm) : 
      self.name = name 
      self.comm = comm 
 
    def getOutputs(self) : 
      return [] 
 
    def getAttributes(self) : 
      return [] 
 
    def executeOutput( self, outputName : str ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":" + outputName ) 
 
    def setAttribute( self, attribName : str, value ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":" + attribName + ":"+ type(value).__name__ +":" + str(value) ) 
 
    def getAttribute( self, attribName : str ) : 
      res = self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":" + attribName ) 
      pos = res.find(":") 
      if pos < 0: 
        raise "Attribute type error" 
      t = res[:pos] 
      val = res[pos+1:] 
      if t == "int": 
        return int(val) 
      elif t == "float": 
        return float(val) 
      elif t == "bool": 
        return bool(val) 
      elif t == "str": 
        return str(val) 
      else: 
        raise "Attribute type error" 
 
  class PushButton(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.PushButton 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "clicked", 
        "pressed", 
        "released", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeClickedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":clicked") 
 
    def executePressedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":pressed") 
 
    def executeReleasedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":released") 
 
 
 
  class ToolButton(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.ToolButton 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "clicked", 
        "pressed", 
        "released", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeClickedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":clicked") 
 
    def executePressedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":pressed") 
 
    def executeReleasedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":released") 
 
 
 
  class ProgressBar(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.ProgressBar 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class LineEdit(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.LineEdit 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "returnPressed", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeReturnPressedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":returnPressed") 
 
 
 
  class Dial(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.Dial 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "valueChanged", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeValueChangedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":valueChanged") 
 
 
 
  class Slider(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.Slider 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "valueChanged", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeValueChangedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":valueChanged") 
 
 
 
  class CheckBox(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'checkboxstate', 'type' : 'bool'}, 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.CheckBox 
 
 
    def setCheckboxState( self, v : bool ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":checkboxstate:" + "bool:" + str(v)  ) 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getCheckboxState( self ) -> bool : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":checkboxstate") ) 
      resSplit = res.split(":") 
      return bool(":".join(resSplit[1:])) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "stateChanged", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeStateChangedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":stateChanged") 
 
 
 
  class Label(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.Label 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class OpenFileButton(ToolButton) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.OpenFileButton 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class ToolButtonWithLed(ToolButton) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'ledstate', 'type' : 'bool'}, 
        {'name' : 'ledinterval', 'type' : 'int'}, 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.ToolButtonWithLed 
 
 
    def setLedState( self, v : bool ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":ledstate:" + "bool:" + str(v)  ) 
 
    def setLedInterval( self, v : int ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":ledinterval:" + "int:" + str(v)  ) 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getLedState( self ) -> bool : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":ledstate") ) 
      resSplit = res.split(":") 
      return bool(":".join(resSplit[1:])) 
 
    def getLedInterval( self ) -> int : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":ledinterval") ) 
      resSplit = res.split(":") 
      return int(":".join(resSplit[1:])) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class ToolButtonWithProgress(ToolButton) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
        {'name' : 'text', 'type' : 'str'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.ToolButtonWithProgress 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class VerticalSlider(Slider) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.VerticalSlider 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class HorizontalSlider(Slider) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.HorizontalSlider 
 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class DigitalIOControl(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
        {'name' : 'state', 'type' : 'bool'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.DigitalIOControl 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def setState( self, v : bool ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":state:" + "bool:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getState( self ) -> bool : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":state") ) 
      resSplit = res.split(":") 
      return bool(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "stateChanged", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeStateChangedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":stateChanged") 
 
 
 
  class AnalogIOControl(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
        {'name' : 'text', 'type' : 'str'}, 
        {'name' : 'value', 'type' : 'float'}, 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.AnalogIOControl 
 
 
    def setText( self, v : str ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":text:" + "str:" + str(v)  ) 
 
    def setValue( self, v : float ) : 
      self.comm.sendAndWait( "gui_setAttribute:" + self.name + ":value:" + "float:" + str(v)  ) 
 
    def getText( self ) -> str : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":text") ) 
      resSplit = res.split(":") 
      return str(":".join(resSplit[1:])) 
 
    def getValue( self ) -> float : 
      res = (self.comm.sendAndWait( "gui_getAttribute:" + self.name + ":value") ) 
      resSplit = res.split(":") 
      return float(":".join(resSplit[1:])) 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
        "valueChanged", 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
    def executeValueChangedOutput( self ) : 
      self.comm.sendAndWait( "gui_executeOutput:" + self.name + ":valueChanged") 
 
 
 
  class CurrentGcodesWidget(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.CurrentGcodesWidget 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class MdiLineWidget(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.MdiLineWidget 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class PythonConsole(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.PythonConsole 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class GCodeList(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.GCodeList 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class SimGLWidget(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.SimGLWidget 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class OffsetTable(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.OffsetTable 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class GroupBox(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.GroupBox 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class Frame(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.Frame 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class TabWidget(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.TabWidget 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class ScrollArea(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.ScrollArea 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class Splitter(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.Splitter 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class FreeLayout(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.FreeLayout 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class HorizontalLayout(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.HorizontalLayout 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class VerticalLayout(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.VerticalLayout 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class GridLayout(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.GridLayout 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  class FormLayout(Widget) : 
 
    def getAttributes(self) : 
      parentAttributes = super().getAttributes() 
      thisClassAttributes =  [ 
      ] 
      res = parentAttributes + thisClassAttributes 
      return res 
 
    def getType(self) : 
      return Gui.WidgetType.FormLayout 
 
 
    def getOutputs(self) : 
      parentOutputs = super().getOutputs() 
      thisClassOutputs =  [ 
      ] 
      res = parentOutputs + thisClassOutputs 
      return res 
 
 
 
  def createObjects( self ) :
    self.MainLayout = Gui.VerticalLayout("MainLayout", self.comm)
    self.splCentral = Gui.Splitter("splCentral", self.comm)
    self.VBoxLayout_3 = Gui.VerticalLayout("VBoxLayout_3", self.comm)
    self.btnEnable1 = Gui.ToolButtonWithLed("btnEnable1", self.comm)
    self.btnStart = Gui.ToolButton("btnStart", self.comm)
    self.btnPause = Gui.ToolButtonWithLed("btnPause", self.comm)
    self.btn_ref_axes = Gui.ToolButton("btn_ref_axes", self.comm)
    self.splToolGCodePython = Gui.Splitter("splToolGCodePython", self.comm)
    self.frToolAndGCode = Gui.Frame("frToolAndGCode", self.comm)
    self.gcodeList = Gui.GCodeList("gcodeList", self.comm)
    self.pythonConsole = Gui.PythonConsole("pythonConsole", self.comm)
    self.Label_1 = Gui.Label("Label_1", self.comm)
    self.VBoxLayout_1 = Gui.VerticalLayout("VBoxLayout_1", self.comm)
    self.PathView_1 = Gui.SimGLWidget("PathView_1", self.comm)
    self.grFro = Gui.GroupBox("grFro", self.comm)
    self.edFro = Gui.LineEdit("edFro", self.comm)
    self.loutFro = Gui.HorizontalLayout("loutFro", self.comm)
    self.slFro = Gui.VerticalSlider("slFro", self.comm)
