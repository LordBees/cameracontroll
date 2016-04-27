##need to rewrite the control code for the camera as it isnt working properly and v2 = best way
##the rotation calc is off

import urllib.request,urllib.parse, tkinter

##TODO
##get conversion of 170 base to abs 340
##redo/revise cgi parsing and construction
##Tk gui for cam control + possibly preview of video
##optimise http cgi sending
##add easy interaction functs for most features
class camera:
    cam_name = 0
    cam_ip = '0.0.0.0'
    cam_deg = 0 ##current cam pos zero = straight##should have called pan and tilt really
    cam_elev = 0##need to find zero value  that cam resets to from the 100 deg range of operation
    cam_reqhead = '/axis-cgi/com/ptz.cgi'#'http://192.168.1.151/axis-cgi/com/ptz.cgi'
    #dataval = {}##temp unused better solution atm found with datasuff
    datasuff=[]#data suffix used as an internal cache of the cgi suffix ##temp fix to get working
    authdat = ('usr','pwd')
    #camurl = 'http://192.168.1.151/axis-cgi/com/ptz.cgi'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'##because faking user agent.
    headers = { 'User-Agent' : user_agent }
    def __init__(self):
        pass        
    def s2tst(self):
        pass
        
        
    
##    def prep_cgi(self,datasuff):##will merge with get_cgi when done
##        #prepares the raw data into cgi format for joining if not already done
##        pre_id = 0
##        if datasuff != None:
##            for x in range(len(datasuff)):
##                if 'camera=' in datasuff[x]:##checks if camname present and verifies it & if wrong corrects it
##                    pre_id = int(datasuff[x][7:len(datasuff[x])])
##                    if int(pre_id)!= int(self.cam_name):
##                        datasuff[x] == 'camera='+str(self.cam_name)
##                        print('expected |'+str(self.cam_name)+'|'+' got |'+str(pre_id)+'|\n-->Overwritten item-> ['+str(pre_id)+'] with ['+str(self.cam_name)+']')
##                        
##                
##    def get_cgi(self):
##        print(self.datasuff)
##        temp = '?'##easier than appending later
##        #for arg in self.datasuff:
##        for x in range(len(self.datasuff)-1): ##joins with and all processed data 
##            temp+=self.datasuff[x]+'&'
##        if len(self.datasuff)>0:
##            temp+=self.datasuff[len(self.datasuff)-1]##could use.size()
##        print('CGI: '+str(temp))
##        return temp
    def make_cgi(self):## needs to read the cache of data  to CGI the data cache  and return as a string the cgi suffix
        print('data in: ',self.datasuff)
        temp = '?'##easier than appending later
        #for arg in self.datasuff:
        
        for x in range(len(self.datasuff)-1):
            temp+=self.datasuff[x]+'&'
        if len(self.datasuff)>0:##bounds check if not zero no need to append  ----move as will break due to being called AFTER the loop
            temp+=self.datasuff[len(self.datasuff)-1]##could use.size()
        print('CGI: '+str(temp))
        if returnable:
            print('returning value:')
            return temp
        else:
            self.datasuff
    
    def calcrot(self,currdegrees):#degtoabs(self,currdegrees):
        #convert+- 170 degrees format into absolute degrees
        if currdegrees < 0:
            print('c<0')
            currdegrees = (170+currdegrees)
        elif currdegrees > 0:
            print('c>0')
            currdegrees = (170+currdegrees)
        elif currdegrees == 0:
            print('c==0')
            currdegrees = 170
        print(currdegrees)
        return currdegrees
        ##currdegrees = absolute 0-340 Deg rather than -+170
        
    def movecalc(self,degoffs):#camera takes degrees to rotate rather than an absolute value to rotate to (maxrot - 340)
        ##accepts 170 thru -170 and turns into absolute rotation of 0-340
        #deg2centre = -self.cam_deg##current degrees to zero
        #degabs = 340-self.cam_deg
        self.cam_deg += degoffs##update position of cam
        #diff =
        nxt = self.degtoabs(self.cam_deg)
        print(nxt)
        #print('['+str(deg2centre)+']',degabs)
        
##    def cam_pan(self,deg,incremental = False):##in easy methods now
##        pass
    def send2cam(self,dataval):
        authMGR = urllib.request.HTTPBasicAuthHandler()
        authMGR.add_password(None, self.getcamstr(),self.authdat[0],self.authdat[1])#authMGR.add_password('realm', 'host', 'username', 'password')
        data = urllib.parse.urlencode(dataval)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(self.getcamstr(), data,self.headers)
        response = urllib.request.urlopen(req)
        the_page = response.read()


        
    def send2cam2(self,datarr):##it seems to have inc/dec when inputting pan/tilt thats why not absolute val
##        ###UPDTATE VALUES HERE###
##        for x in range(len(datarr)):##could merge with bounds check and updates
##            if 'rpan=' in datarr[x]:
##                self.cam_deg += int(datarr[x][5:len(datarr[x])])#chops off the rpan bit and passes the rest to be added to the degrees moved variable
##            if 'rtilt=' in datarr[x]:
##                self.cam_elev += int(datarr[x][6:len(datarr[x])])#chops off the rtilt bit and passes the rest to be added to the degrees tilted variable
##        ###END update values###  ## gets the values out of thearray to be added to the watchdog variables 
##
##
##        ##EVENT CHECKING##  ##checks the values before compiling them into the CGI request to ensure they are all valid
##                
##        deg_overflow = 0##cant remember use for this but its here anyway
##        elev_overflow = 0
##        
##        
##        if self.cam_deg > 170:##bounds check for the cam rot degrees
##            deg_overflow = self.cam_deg - 170##dunno
##            self.cam_deg = 170
##        elif self.cam_deg <-170:
##            deg_overflow = self.cam_deg +170
##            self.cam_deg = -170
##        print('Overflow value deg:'+str(deg_overflow),'rotation = '+str(self.cam_deg))
##
##        if self.cam_elev > 100:##bounds check for the cam elev degrees
##            elev_overflow = self.cam_elev - 100##dunno
##            self.cam_elev = 100
##        elif self.cam_elev <-100:
##            elev_overflow = self.cam_elev +100
##            self.cam_elev = -100
##        print('Overflow value elev:'+str(elev_overflow),'elevation = '+str(self.cam_elev))
##        #end event checks
##
##        ##EVENT UPDATES##  ##updates all the values into the respective cgi variables
##        for x in range(len(datarr)):
##            if 'rpan=' in datarr[x]:
##                datarr[x] = 'rpan='+str(self.cam_deg)
##            if 'rtilt=' in datarr[x]:
##                datarr[x] = 'rtilt='+str(self.cam_elev)
##                
##        ##END event updates##

        
        ##SUPERCHECK##      ##merged the above into the supercheck
        deg_overflow = 0##cant remember use for this but its here anyway
        elev_overflow = 0
        for x in range(len(datarr)):##could merge with bounds check and updates
            print('\n________ITER:'+str(x)+'________')
            if 'rpan=' in datarr[x]:
                self.cam_deg += int(datarr[x][5:len(datarr[x])])#chops off the rpan bit and passes the rest to be added to the degrees moved variable

                if self.cam_deg > 170:##bounds check for the cam rot degrees
                    deg_overflow = self.cam_deg - 170##dunno
                    self.cam_deg = 170
                elif self.cam_deg <-170:
                    deg_overflow = self.cam_deg +170
                    self.cam_deg = -170
                print('Overflow value deg:'+str(deg_overflow),'rotation = '+str(self.cam_deg))
                datarr[x] = 'rpan='+str(self.cam_deg)

            if 'rtilt=' in datarr[x]:
                self.cam_elev += int(datarr[x][6:len(datarr[x])])#chops off the rtilt bit and passes the rest to be added to the degrees tilted variable

                if self.cam_elev > 100:##bounds check for the cam elev degrees
                    elev_overflow = self.cam_elev - 100##dunno
                    self.cam_elev = 100
                elif self.cam_elev <-100:
                    elev_overflow = self.cam_elev +100
                    self.cam_elev = -100
                print('Overflow value elev:'+str(elev_overflow),'elevation = '+str(self.cam_elev))
                datarr[x] = 'rtilt='+str(self.cam_elev)
                
        ##END SUPERCHECK##
        print('\n________END___________')
        print('new: '+str(self.datasuff)+'\nold: '+str(datarr))
        self.set_datasuff(datarr)##override new values into cache
        
        #url = self.getcamstr()
        #theurl = 'http://www.someserver.com/toplevelurl/somepage.htm'
        #username = 'johnny'
        #password = 'XXXXXX'
        # a great password

        passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()# this creates a password manager
        passman.add_password(None, self.getcamstr(), self.authdat[0],self.authdat[1])# because we have put None at the start it will always use this username/password combination for  urls for which `theurl` is a super-url

        authhandler = urllib.request.HTTPBasicAuthHandler(passman)# create the AuthHandler
        opener = urllib.request.build_opener(authhandler)
        urllib.request.install_opener(opener)# All calls to urllib2.urlopen will now use our handler Make sure not to include the protocol in with the URL, or HTTPPasswordMgrWithDefaultRealm will be very confused. You must (of course) use it when fetching the page though.

        pagehandle = urllib.request.urlopen(self.getcamstr()+self.get_cgi())
        page = pagehandle.read()
        print('response; '+str(page))
        # authentication is now handled automatically for us




    ##set/get methods##
    def getcamstr(self):#stitches http cgi request prefix
        return 'http://'+str(self.cam_ip)+str(self.cam_reqhead)



    
    def set_camname(self,number):#camname is an int as each camera is numerically id'ed
        self.cam_name = int(number)
        
    def get_camname(self):
        return self.cam_name
    
    def set_camip(self,ipaddr):
        self.cam_ip = str(ipaddr)
        
    def get_camip(self):
        return self.cam_ip

    def set_camreqhead(self,req_header):##for other cams that have similar methods
        self.cam_reqhead = str(req_header)
        
    def get_camip(self):
        return self.cam_reqhead
    
    def set_dataval(self,array):
        self.dataval = array
        
    def get_dataval(self):
        return self.dataval
    
    def set_datasuff(self,array):
        self.datasuff = array
        
    def get_datasuff(self):
        return self.datasuff
    ##END set/get methods##
    
    ##easy methods##

    def AF_camera(self,OnOff):##auto focus on/off
        pass
    def AF_camera_on(self):
        self.AF_camera(True)
    def AF_camera_off(self):
        self.AF_camera(False)

    def AI_camera(self,OnOff):##auto iris on/off
        pass
    def AI_camera_on(self):
        self.AI_camera(True)
    def AI_camera_off(self):
        self.AI_camera(False)

    def BL_camera(self,OnOff):##backlight on/off
        pass
    def BL_camera_on(self):
        self.BL_camera(True)
    def BL_camera_off(self):
        self.BL_camera(False)

    def JC_camera(self,jORc):##navigation mode center/joystick
        pass
    def JC_camera_joy(self):
        self.JC_camera('joystick')
    def JC_camera_center(self):
        self.JC_camera('center')

    def XH_camera(self,OnOff):##crosshair on/off
        pass
    def XH_camera_on(self):
        self.XH_camera(True)
    def XH_camera_off(self):
        self.XH_camera(False)

    def IR_Shutter(self,OnOff):##ir shutter on/off
        pass
    def IR_Shutter_on(self):
        self.IR_Shutter(True)
    def IR_Shutter_off(self):
        self.IR_Shutter(False)

    def IR_light(self,OnOff):##ir shutter on/off
        pass
    def IR_light_on(self):
        self.IR_light(True)
    def IR_light_off(self):
        self.IR_light(False)

    def cpan(self,deg,incremental = False):##incremental  is 0 - 340 non incremental is -170 - 170
        pass
    def ctilt(self,deg,incremental = False):##incremental  is 0 - 340 non incremental is -170 - 170
        pass
    def czoom(self,percent):##0-100
        pass
    def cfocus(self,percent):##-100 to 100
        pass
    def ciris(self,percent):##-100 to 100
        pass

    ##END easy methods##
    
    
c=camera()
c.s2tst()
print('setup test')
def ct():
    dat = ['rpan=190', 'camera=1']
    c.s2tst()
    c.send2cam2(dat)
def cd(currdegrees):##currdegrees(degrees)
    if currdegrees < 0:
        print('c<0')
        currdegrees = (170+currdegrees)
    elif currdegrees > 0:
        print('c>0')
        currdegrees = (170+currdegrees)
    elif currdegrees == 0:
        print('c==0')
        currdegrees = 170
    return currdegrees
#class httpmanager:
