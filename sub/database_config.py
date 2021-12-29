# sub.database_config.py

import sys

sys.path.insert(0, '/dbconfig')  # Database 접속정보가 담긴 Config 파일을 저장한 폴더 경로
import dbconfig as config  # 나의 Database 접속정보를 가져온다.


def get_db_info(db_name):
    return {"Maria": config.Maria, "Postgresql": config.Postgresql}.get(db_name, config.nodb)
