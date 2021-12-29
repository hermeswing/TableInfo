# sub.ini_config.py

# python 2.x
# from ConfigParser import SafeConfigParser
# config = SafeConfigParser()

# python 3.x
from configparser import ConfigParser, NoSectionError

config_path = '/dbconfig/dbconfig.ini'
config = ConfigParser()
config.read(config_path, encoding='utf-8')


# 설장파일 색션 확인
def get_sections():
    return config.sections()

#
def get_ini_config(db_name):
    rtn_map = None
    try:
        rtn_map = {"name": config.get(db_name, "name"), "ip": config.get(db_name, "ip"),
                   "user": config.get(db_name, "user"), "passwd": config.get(db_name, "passwd"),
                   "port": config.get(db_name, "port"), "charset": config.get(db_name, "charset")}
    except NoSectionError:
        rtn_map = {"name": "", "ip": "", "user": "", "passwd": "", "port": "", "charset": ""}

    return rtn_map


class SaveConfig:
    def __init__(self, section, name, ip, user, pw, port, charset):
        self.section = section
        self.name = name
        self.ip = ip
        self.user = user
        self.pw = pw
        self.port = port
        self.charset = charset

    def save_ini_config(self):
        config.add_section(self.section)
        config.set(self.section, 'name', self.name)
        config.set(self.section, 'ip', self.ip)
        config.set(self.section, 'user', self.user)
        config.set(self.section, 'passwd', self.pw)
        config.set(self.section, 'port', self.port)
        config.set(self.section, 'charset', self.charset)

        with open(config_path, 'w', encoding='utf-8') as f:
            config.write(f)
