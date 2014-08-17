# -*- coding: utf-8 -*-

import optparse
import sys,os,platform
import re

import time
import random
import commands
import RTC
import OpenRTM_aist


from OpenRTM_aist import CorbaNaming
from OpenRTM_aist import RTObject
from OpenRTM_aist import CorbaConsumer
from omniORB import CORBA
import CosNaming
from rtctree.utils import build_attr_string, dict_to_nvlist, nvlist_to_dict






CompList = []


##
# データのタイプ
##

class m_DataType:
    Single = 0
    Sequence = 1

    String = 0
    Value = 1
    def __init__(self):
        pass

##
# データ型を返す関数
##
        
def GetDataType(m_port):
    sig = m_DataType.Single
    sec = m_DataType.Sequence

    m_string = m_DataType.String
    m_value = m_DataType.Value
    
    profile = m_port.get_port_profile()
    props = nvlist_to_dict(profile.properties)
    data_type =  props['dataport.data_type']
    if data_type.startswith('IDL:'):
        data_type = data_type[4:]
    colon = data_type.rfind(':')
    if colon != -1:
        data_type = data_type[:colon]

    data_type = data_type.replace('RTC/','')

    if data_type == 'TimedDouble':
        dt = RTC.TimedDouble(RTC.Time(0,0),0)
        return dt, [float, sig, m_value]
    elif data_type == 'TimedLong':
        dt = RTC.TimedLong(RTC.Time(0,0),0)
        return dt, [long, sig, m_value]
    elif data_type == 'TimedFloat':
        dt = RTC.TimedFloat(RTC.Time(0,0),0)
        return dt, [float, sig, m_value]
    elif data_type == 'TimedInt':
        dt = RTC.TimedInt(RTC.Time(0,0),0)
        return dt, [int, sig, m_value]
    elif data_type == 'TimedShort':
        dt = RTC.TimedShort(RTC.Time(0,0),0)
        return dt, [int, sig, m_value]
    elif data_type == 'TimedUDouble':
        dt = RTC.TimedUDouble(RTC.Time(0,0),0)
        return dt, [float, sig, m_value]
    elif data_type == 'TimedULong':
        dt = RTC.TimedULong(RTC.Time(0,0),0)
        return dt, [long, sig, m_value]
    elif data_type == 'TimedUFloat':
        dt = RTC.TimedUFloat(RTC.Time(0,0),0)
        return dt, [float, sig, m_value]
    elif data_type == 'TimedUInt':
        dt = RTC.TimedUInt(RTC.Time(0,0),0)
        return dt, [int, sig, m_value]
    elif data_type == 'TimedUShort':
        dt = RTC.TimedUShort(RTC.Time(0,0),0)
        return dt, [int, sig, m_value]
    elif data_type == 'TimedChar':
        dt = RTC.TimedChar(RTC.Time(0,0),0)
        return dt, [str, sig, m_string]
    elif data_type == 'TimedWChar':
        dt = RTC.TimedWChar(RTC.Time(0,0),0)
        return dt, [str, sig, m_string]
    elif data_type == 'TimedBoolean':
        dt = RTC.TimedBoolean(RTC.Time(0,0),0)
        return dt, [bool, sig, m_value]
    elif data_type == 'TimedOctet':
        dt = RTC.TimedOctet(RTC.Time(0,0),0)
        return dt, [int, sig, m_value]
    elif data_type == 'TimedString':
        dt = RTC.TimedString(RTC.Time(0,0),0)
        return dt, [str, sig, m_string]
    elif data_type == 'TimedWString':
        dt = RTC.TimedWString(RTC.Time(0,0),0)
        return dt, [str, sig, m_string]
    elif data_type == 'TimedDoubleSeq':
        dt = RTC.TimedDoubleSeq(RTC.Time(0,0),[])
        return dt, [float, sec, m_value]
    elif data_type == 'TimedLongSeq':
        dt = RTC.TimedLongSeq(RTC.Time(0,0),[])
        return dt, [long, sec, m_value]
    elif data_type == 'TimedFloatSeq':
        dt = RTC.TimedFloatSeq(RTC.Time(0,0),[])
        return dt, [float, sec, m_value]
    elif data_type == 'TimedIntSeq':
        dt = RTC.TimedIntSeq(RTC.Time(0,0),[])
        return dt, [int, sec, m_value]
    elif data_type == 'TimedShortSeq':
        dt = RTC.TimedShortSeq(RTC.Time(0,0),[])
        return dt, [int, sec, m_value]
    elif data_type == 'TimedUDoubleSeq':
        dt = RTC.TimedUDoubleSeq(RTC.Time(0,0),[])
        return dt, [float, sec, m_value]
    elif data_type == 'TimedULongSeq':
        dt = RTC.TimedULongSeq(RTC.Time(0,0),[])
        return dt, [long, sec, m_value]
    elif data_type == 'TimedUFloatSeq':
        dt = RTC.TimedUFloatSeq(RTC.Time(0,0),[])
        return dt, [float, sec, m_value]
    elif data_type == 'TimedUIntSeq':
        dt = RTC.TimedUIntSeq(RTC.Time(0,0),[])
        return dt, [int, sec, m_value]
    elif data_type == 'TimedUShortSeq':
        dt = RTC.TimedUShortSeq(RTC.Time(0,0),[])
        return dt, [int, sec, m_value]
    elif data_type == 'TimedCharSeq':
        dt = RTC.TimedCharSeq(RTC.Time(0,0),[])
        return dt, [str, sec, m_string]
    elif data_type == 'TimedWCharSeq':
        dt = RTC.TimedWCharSeq(RTC.Time(0,0),[])
        return dt, [str, sec, m_string]
    elif data_type == 'TimedBooleanSeq':
        dt = RTC.TimedBooleanSeq(RTC.Time(0,0),[])
        return dt, [bool, sec, m_value]
    elif data_type == 'TimedOctetSeq':
        dt = RTC.TimedOctetSeq(RTC.Time(0,0),[])
        return dt, [int, sec, m_value]
    elif data_type == 'TimedStringSeq':
        dt = RTC.TimedStringSeq(RTC.Time(0,0),[])
        return dt, [str, sec, m_string]
    elif data_type == 'TimedWStringSeq':
        dt = RTC.TimedWStringSeq(RTC.Time(0,0),[])
        return dt, [str, sec, m_string]
    
    
    else:
        return None


##
# ポートを接続する関数
##

def m_addport(obj1, obj2, c_name):

    subs_type = "Flush"

    obj1.disconnect_all()
    
    obj2.disconnect_all()

    # connect ports
    conprof = RTC.ConnectorProfile("connector0", "", [obj1,obj2], [])
    OpenRTM_aist.CORBA_SeqUtil.push_back(conprof.properties,
                                    OpenRTM_aist.NVUtil.newNV("dataport.interface_type",
                                                         "corba_cdr"))

    OpenRTM_aist.CORBA_SeqUtil.push_back(conprof.properties,
                                    OpenRTM_aist.NVUtil.newNV("dataport.dataflow_type",
                                                         "push"))

    OpenRTM_aist.CORBA_SeqUtil.push_back(conprof.properties,
                                    OpenRTM_aist.NVUtil.newNV("dataport.subscription_type",
                                                         subs_type))

    ret = obj2.connect(conprof)
        

##
# ネーミングサービスへ接続する関数
##
def SetNamingServer(s_name, orb):
    
    try:
        namingserver = CorbaNaming(orb, s_name)
    except:
        print 'ネーミングサービスへの接続に失敗しました'
        return None
    return namingserver

##
# ツリーで選択したアイテムがポートかどうか判定する関数
# objectTree：ダイアログのツリー
# _path：ポートのパスのリスト
##

def JudgePort(objectTree, _paths):
    m_list = []
        
    node = objectTree.getSelection()
    if node:
        parent = node.getParent()
        if parent:
            m_list.insert(0, node.getDisplayValue())
        else:
            return None
        if node.getChildCount() != 0:
            return None
    else:
        return None
            
    while(True):
        if node:
            node = node.getParent()
            if node:
                m_list.insert(0, node.getDisplayValue())
            else:
                break
        

    flag = False
    for t_comp in _paths:
        if t_comp[0] == m_list:
            return t_comp, node
            
            flag = True
            
                
    if flag == False:
        return None






##
# 各RTCのパスを取得する関数
##
def ListRecursive(context, rtclist, name):
    
    m_blLength = 100
    
    bl = context.list(m_blLength)
    

    cont = True
    while cont:
        for i in bl[0]:
            if i.binding_type == CosNaming.ncontext:
                
                next_context = context.resolve(i.binding_name)
                name_buff = name[:]
                name.append(i.binding_name[0].id)

                
                
                
                
                ListRecursive(next_context,rtclist,name)
                

                name = name_buff
            elif i.binding_type == CosNaming.nobject:
                
                
                if len(rtclist) > m_blLength:
                    break
                if i.binding_name[0].kind == 'rtc':
                    name_buff = name[:]
                    name_buff.append(i.binding_name[0].id)
                    
                    tkm = OpenRTM_aist.CorbaConsumer()
                    tkm.setObject(context.resolve(i.binding_name))
                    inobj = tkm.getObject()._narrow(RTC.RTObject)
                    pin = inobj.get_ports()
                    for p in pin:
                        name_buff2 = name_buff[:]
                        profile = p.get_port_profile()
                        props = nvlist_to_dict(profile.properties)
                        tp_n = profile.name.split('.')[1]
                        name_buff2.append(tp_n)
                        

                        rtclist.append([name_buff2,p])
                        
            else:
                pass
        if CORBA.is_nil(bl[1]):
            cont = False
        else:
            bl = i.next_n(m_blLength)


def rtc_get_rtclist(naming, rtclist, name):  
    name_cxt = naming.getRootContext()
    ListRecursive(name_cxt,rtclist,name)
    
    return 0







                       
##
# ポートのパスのリストを取得する関数
##
def getPathList(name, m_mgr):
    orb = m_mgr._orb
    namingserver = SetNamingServer(str(name), orb)
    if namingserver:
        _path = ['/', name]
        _paths = []
        rtc_get_rtclist(namingserver, _paths, _path)
        return _paths
    return None



class MyPortObject:
    def __init__(self, port, data):
        self._port = port
        self._data = data
        

        

class SubCtlComp(OpenRTM_aist.DataFlowComponentBase):
  def __init__(self, manager):
    OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)
    self.Port = {}
    _paths = getPathList("localhost",manager)
    print _paths
    for i,j in self.PortList.items():
        for k in _paths:
            if j == k[0]:
                m_data, m_data_type =  GetDataType(k[1])
                profile = k[1].get_port_profile()
                props = nvlist_to_dict(profile.properties)
                if props['port.port_type'] == 'DataInPort':
                    m_port = OpenRTM_aist.OutPort(i, m_data)
                    self.Port[i] = MyPortObject(m_port, m_data)
                    self.addOutPort(i, m_port)
                    m_addport(m_port._objref, k[1], i)
                elif props['port.port_type'] == 'DataOutPort':
                    m_port = OpenRTM_aist.InPort(i, m_data)
                    self.Port[i] = MyPortObject(m_port, m_data)
                    self.addOutPort(i, m_port)
                    m_addport(m_port._objref, k[1], i)
                    
    
    return


  

  





def MyModuleInit(manager):
  j = 0
  for i in CompList:
      fc_spec = ["implementation_id", "SubCtlComp"+str(j),
                  "type_name",         "SubControlComponent"+str(j),
                  "description",       "Sub Control component"+str(j),
                  "version",           "1.0",
                  "vendor",            "aaaaaaa",
                  "category",          "example",
                  "activity_type",     "DataFlowComponent",
                  "max_instance",      "10",
                  "language",          "Python",
                  "lang_type",         "script",
                  ""]

      
      profile = OpenRTM_aist.Properties(defaults_str=fc_spec)
      manager.registerFactory(profile,
                              i,
                              OpenRTM_aist.Delete)

      

      # Create a component
      comp = manager.createComponent("SubCtlComp"+str(j))

      j += 1

  

  
##
#コンポーネント起動
##

def SetComp():
  mgr = OpenRTM_aist.Manager.init(sys.argv)

  mgr.setModuleInitProc(MyModuleInit)

  mgr.activateManager()

  mgr.runManager()



