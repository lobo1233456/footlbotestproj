# from qt4s.service import Channel
# from qt4s.conn2 import HttpConn
from testbase.conf import SettingsMixin

class MyChannel(Channel, SettingsMixin):
    """define a pseudo channel
    """
    class Settings(object):
        MYCHANNEL_URL = "http://www.xxxx.com"

    def __init__(self):
        self._conn = HttpConn()

    def get(self, uri, params):
        return self._conn.get(self.settings.MYCHANNEL_URL + uri, params)