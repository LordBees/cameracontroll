import urllib.request,urllib.parse
class camera:
    cam_name = 0
    cam_ip = '0.0.0.0'
    cam_reqhead = '/axis-cgi/com/ptz.cgi'#'http://192.168.1.151/axis-cgi/com/ptz.cgi'
    #dataval = {}##temp unused better solution atm found with datasuff
    datasuff=[]#data sufffix ##temp fix to get working
    authdat = ('usr','pwd')
    #camurl = 'http://192.168.1.151/axis-cgi/com/ptz.cgi'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    def __init__(self):
        pass
    def t(self):
        self.s2tst()
        self.send2cam(self.dataval)
    def t2(self):
        self.s2tst()
        self.send2cam2()#self.dataval)
        
    def s2tst(self):##quick setup for testing
        self.cam_name = 1
        self.cam_ip = '192.168.0.1'
        self.cam_reqhead = '/axis-cgi/com/ptz.cgi'
        self.authdat = ('usr','pass')
        #self.dataval = {'rpan' : '190', 'camera' : '1'}
        self.datasuff = ['rpan=190', 'camera=1']
        
    def getcamstr(self):#stitches http cgi request prefix
        return 'http://'+str(self.cam_ip)+str(self.cam_reqhead)
    
    def get_cgi(self):
        temp = '?'##easier than appending later
        #for arg in self.datasuff:
        for x in range(len(self.datasuff)-1):
            temp+=self.datasuff[x]+'&'
        if len(self.datasuff)>0:
            temp+=self.datasuff[len(self.datasuff)-1]##could use.size()
        return temp
            
    
    def send2cam(self,dataval):
        authMGR = urllib.request.HTTPBasicAuthHandler()
        authMGR.add_password(None, self.getcamstr(),self.authdat[0],self.authdat[1])#authMGR.add_password('realm', 'host', 'username', 'password')
        data = urllib.parse.urlencode(dataval)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(self.getcamstr(), data,self.headers)
        response = urllib.request.urlopen(req)
        the_page = response.read()
        
    def send2cam2(self,datarr):
        self.dataval = datarr
        #url = self.getcamstr()
        #theurl = 'http://www.someserver.com/toplevelurl/somepage.htm'
        #username = 'johnny'
        #password = 'XXXXXX'
        # a great password

        passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        # this creates a password manager
        passman.add_password(None, self.getcamstr(), self.authdat[0],self.authdat[1])
        # because we have put None at the start it will always
        # use this username/password combination for  urls
        # for which `theurl` is a super-url

        authhandler = urllib.request.HTTPBasicAuthHandler(passman)
        # create the AuthHandler

        opener = urllib.request.build_opener(authhandler)

        urllib.request.install_opener(opener)
        # All calls to urllib2.urlopen will now use our handler
        # Make sure not to include the protocol in with the URL, or
        # HTTPPasswordMgrWithDefaultRealm will be very confused.
        # You must (of course) use it when fetching the page though.

        pagehandle = urllib.request.urlopen(self.getcamstr()+self.get_cgi())
        # authentication is now handled automatically for us
        
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
c=camera()        
def ct():
    c.s2tst()
    c.send2cam2()
    

#class httpmanager:
