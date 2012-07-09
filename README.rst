FIRST OF ALL
--------------
Register to https://www.globelabs.com.ph to access Globe Labs API


HOW TO INSTALL
--------------
To install run ``pip install pyglobe`` or ``easy_install pyglobe``.


SEND SMS
------------
::

    import pyglobe

    try:
        service = pyglobe.PyGlobe(uname='<globe API uname>',
                                  pin='<globe API pin>',
                                  msisdn='<11 digit mobile number>')
        service.sendSMS('Message through Globe Labs API')
    except (pyglobe.PyGlobeInvalidServiceException,
            pyglobe.PyGlobeInvalidURLException,
            pyglobe.PyGlobeServerFaultException) as e:
        print "An error occurred: %s" % e

SEND MMS
------------
::

    import pyglobe
    
    #Valid SMIL (Synchronized Multimedia Integration Language)
    smil = "<smil><head><layout><root-layout height='96' width='122' /><region height='67%' fit='meet' id='Image' width='100%' left='0%' top='0%' /><region height='33%' fit='scroll' id='Text' width='100%' left='0%' top='67%' /></layout></head><body><par dur='8000ms'><img src='https://www.globelabs.com.ph/Style%20Library/en-us/Core%20Styles/MasterPageStyles/images/globe_logo_NOtag_155x60px.png' region='Image' /><text src='http://ferdinandsilva.com/hello.txt' region='Text' /></par></body></smil>"

    try:
        service = pyglobe.PyGlobe(uname='<globe API uname>',
                                  pin='<globe API pin>',
                                  msisdn='<11 digit mobile number>')
        service.sendMMS('<subject>', smil)
    except (pyglobe.PyGlobeInvalidServiceException,
            pyglobe.PyGlobeInvalidURLException,
            pyglobe.PyGlobeServerFaultException) as e:
        print "An error occurred: %s" % e
