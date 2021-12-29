# sub.h2_config.py
# https://wiki.python.org/moin/DbApiModuleComparison
import jaydebeapi

import utils.logger as logger


class H2Config:

    def __init__(self, host, port, user, pw, name):
        self.logger = logger.logger_with_name("MainThread")

        self._host = host
        self._port = port
        self._user = user
        self._pw = pw
        self._name = name

    # h2 접속 테스트
    def connection_test(self):
        self.logger.info('[H2Config > connection_test]')
        try:
            driver = "org.h2.Driver"
            jar = "c:/Temp/h2-1.4.199.jar"
            conn = jaydebeapi.connect(driver, "jdbc:h2:tcp://localhost/~/jpashop", ["sa", "sa"], jar)
            conn.close()
            return True
        except jaydebeapi.DatabaseError as e:
            self.logger.error('[H2Config > connection_test]' + str(e))
            return False
