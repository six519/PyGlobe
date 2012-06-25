HOW TO INSTALL
--------------
To install run ``pip install pyglobe`` or ``easy_install pyglobe``.


EXAMPLE CODE
------------
::

    import pyglobe

    try:
        service = pyglobe.PyGlobe(uname='<globe API uname>', pin='<globe API pin>', msisdn='<11 digit mobile number>')
        service.sendSMS('Message through Globe Labs API')
    except (pyglobe.PyGlobeInvalidServiceException,
            pyglobe.PyGlobeInvalidURLException,
            pyglobe.PyGlobeServerFaultException) as e:
        print "An error occurred: %s" % e
