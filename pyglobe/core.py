import urllib2

from .exceptions import *


__all__ = ['PyGlobeDisplay', 'PyGlobeMWI', 'PyGlobeCoding', 'PyGlobeReturnCode', 'PyGlobe',
           'PyGlobeInvalidURLException', 'PyGlobeInvalidServiceException', 'PyGlobeServerFaultException']

WSDL_URL = 'http://iplaypen.globelabs.com.ph:1881/axis2/services/Platform?wsdl'

class PyGlobeDisplay:
    SEND_DIRECTLY_TO_DISPLAY = "0"
    SEND_TO_PHONE = "1"
    SEND_TO_SIM = "2"


class PyGlobeMWI:
    NONE = ""
    VOICE_MAIL_ICON_ACTIVATE = "0"
    FAX_ICON_ACTIVATE = "1"
    EMAIL_ICON_ACTIVATE = "2"
    OTHER_ACTIVATION = "3"
    DEACTIVATE_VOICE_MAIL_ICON = "4"
    DEACTIVATE_FAX_ICON = "5"
    DEACTIVATE_EMAIL_ICON = "6"
    DEACTIVATE_OTHER_ICON = "7"


class PyGlobeCoding:
    BIT_7 = "0"
    BIT_8 = "1"
    USC_2 = "2"


class PyGlobeReturnCode:
    NOT_ALLOWED = "301"
    EXCEEDED_DAILY_CAP = "302"
    INVALID_MESSAGE_LENGTH = "303"
    MAX_NUMBER_CONNECTION = "304"
    INVALID_LOGIN_CREDENTIALS = "305"
    SMS_SENDING_FAILED = "401"
    MMS_SENDING_FAILED = "402"
    INVALID_TARGET = "501"
    INVALID_DISPLAY = "502"
    INVALID_MWI = "503"
    BAD_XML = "506"
    INVALID_CODING = "504"
    EMPTY_VALUE = "505"
    ARGUMENT_TOO_LARGE = "507"
    SMS_ACCEPTED = "201"
    MMS_ACCEPTED = "202"


class PyGlobe(object):
    def __init__(self, **kwargs):
        self.wsdl = kwargs.get('wsdl', WSDL_URL)
        self.uname = kwargs.get('uname','')
        self.pin = kwargs.get('pin','')
        self.msisdn = kwargs.get('msisdn','')
        self.display = kwargs.get('display', PyGlobeDisplay.SEND_TO_PHONE)
        self.udh = kwargs.get('udh','')
        self.mwi = kwargs.get('mwi', PyGlobeMWI.NONE)
        self.coding = kwargs.get('coding', PyGlobeCoding.BIT_7)
        self.service = None
        try:
            import suds
            self.service = suds.client.Client(self.wsdl)
        except urllib2.URLError:
            raise PyGlobeInvalidServiceException('Service Unknown')
        except ValueError:
            raise PyGlobeInvalidURLException('Invalid URL')

    def sendSMS(self, message = ""):
        try:
            ret = self.service.service.sendSMS(self.uname, self.pin, self.msisdn, message, self.display, self.udh, self.mwi, self.coding)
            
            if ret == PyGlobeReturnCode.SMS_ACCEPTED:
                return True
            elif ret == PyGlobeReturnCode.NOT_ALLOWED:
                raise PyGlobeServerFaultException("User is not allowed to access this service")
            elif ret == PyGlobeReturnCode.EXCEEDED_DAILY_CAP:
                raise PyGlobeServerFaultException("User exceeded daily cap")
            elif ret == PyGlobeReturnCode.INVALID_MESSAGE_LENGTH:
                raise PyGlobeServerFaultException("Invalid message length")
            elif ret == PyGlobeReturnCode.MAX_NUMBER_CONNECTION:
                raise PyGlobeServerFaultException("Maximum Number of simultaneous connections reached")
            elif ret == PyGlobeReturnCode.INVALID_LOGIN_CREDENTIALS:
                raise PyGlobeServerFaultException("Invalid login credentials")
            elif ret == PyGlobeReturnCode.SMS_SENDING_FAILED:
                raise PyGlobeServerFaultException("SMS sending failed")
            elif ret == PyGlobeReturnCode.INVALID_TARGET:
                raise PyGlobeServerFaultException("Invalid target MSISDN")
            elif ret == PyGlobeReturnCode.INVALID_DISPLAY:
                raise PyGlobeServerFaultException("Invalid display type")
            elif ret == PyGlobeReturnCode.INVALID_MWI:
                raise PyGlobeServerFaultException("Invalid MWI")
            elif ret == PyGlobeReturnCode.BAD_XML:
                raise PyGlobeServerFaultException("Badly formed XML in SOAP request")
            elif ret == PyGlobeReturnCode.INVALID_CODING:
                raise PyGlobeServerFaultException("Invalid Coding")
            elif ret == PyGlobeReturnCode.EMPTY_VALUE:
                raise PyGlobeServerFaultException("Empty value given in required argument")
            elif ret == PyGlobeReturnCode.ARGUMENT_TOO_LARGE:
                raise PyGlobeServerFaultException("Argument given too large")
        except urllib2.URLError:
            raise PyGlobeInvalidServiceException('Service Unknown')

    def sendMMS(self):
        pass
