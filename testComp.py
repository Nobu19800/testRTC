# -*- coding: utf-8 -*-

import rtcControl
import sys
import time

import RTC
import OpenRTM_aist


class testComponent(rtcControl.SubCtlComp):
    def __init__(self, manager):
        self.PortList = {"test":['/', 'localhost', 'SequenceInComponent0', 'Long'],
                         "test2":['/', 'localhost', 'SequenceOutComponent0', 'Long'],
                         "test3":['/', 'localhost', 'SequenceOutComponent0', 'LongSeq']}
        rtcControl.SubCtlComp.__init__(self, manager)
        
        

    def onExecute(self, ec_id):
        if self.Port["test2"]._port.isNew() and self.Port["test3"]._port.isNew():
            data1 = self.Port["test2"]._port.read()
            data2 = self.Port["test3"]._port.read()

            ans = data1.data
            for i in data2.data:
                ans += i

            self.Port["test"]._data.data = ans
            self.Port["test"]._port.write()

        return RTC.RTC_OK


class testComponent2(rtcControl.SubCtlComp):
    def __init__(self, manager):
        self.PortList = {"test":['/', 'localhost', 'SequenceInComponent0', 'Short'],
                         "test2":['/', 'localhost', 'SequenceOutComponent0', 'Short']}
        rtcControl.SubCtlComp.__init__(self, manager)
        
        

    def onExecute(self, ec_id):
        if self.Port["test2"]._port.isNew():
            data = self.Port["test2"]._port.read()
            print data.data

            self.Port["test"]._data.data = 100
            self.Port["test"]._port.write()
        return RTC.RTC_OK
        #print self.InPort["test"]

rtcControl.CompList.append(testComponent)
rtcControl.CompList.append(testComponent2)

rtcControl.SetComp()
