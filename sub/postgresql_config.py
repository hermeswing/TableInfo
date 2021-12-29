# sub.postgresql_config.py
# https://wiki.python.org/moin/DbApiModuleComparison
import psycopg2 as psycopg2


class PostgresqlConfig:

    def __init__(self, host, port, user, pw, name):
        self._host = host
        self._port = port
        self._user = user
        self._pw = pw
        self._name = name

    # Postgresql Connection
    def get_connection(self):
        try:
            info = "host=" + self._host + " dbname=" + self._name + " user=" + self._user + " password=" + self._pw
            conn = psycopg2.connect(info)
            return conn
        except (Exception, psycopg2.Error):
            return False

    # Postgresql 접속 테스트
    def connection_test(self):
        print('[PostgresqlConfig > connection_test]')
        try:
            conn = self.get_connection()
            conn.close()
            return True
        except (Exception, psycopg2.Error):
            return False

    # Postgresql Table List
    def get_table_list(self):
        print('[PostgresqlConfig > get_table_list]')
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()  # 2. 커서 생성 (트럭, 연결로프)
            sql = 'SELECT RELNAME AS TABLE_NAME' \
                  '  FROM PG_STAT_USER_TABLES'
            cur.execute(sql)
            rows = cur.fetchall()

            return rows

        except (Exception, psycopg2.Error):
            return False
        finally:
            cur.close()
            conn.close()

    # Postgresql Column List
    def get_column_list(self, table_name):
        print('[PostgresqlConfig > get_column_list]')
        conn = None
        cur = None
        try:
            conn = self.get_connection()
            cur = conn.cursor()  # 2. 커서 생성 (트럭, 연결로프)
            sql = "SELECT ORDINAL_POSITION" \
                  "     , COLUMN_NAME" \
                  "     , DATA_TYPE" \
                  "  FROM INFORMATION_SCHEMA.COLUMNS" \
                  " WHERE TABLE_CATALOG = %s" \
                  "   AND TABLE_NAME    = %s" \
                  " ORDER BY ORDINAL_POSITION"
            data = (self._name, table_name)
            cur.execute(sql, data)
            rows = cur.fetchall()

            return rows

        except (Exception, psycopg2.Error):
            return False
        finally:
            cur.close()
            conn.close()