import os

print(os.path.dirname(__file__))  # 현재 스크립트가 속한 디렉토리까지의 경로
print(os.listdir(os.path.curdir))  # current directory list
print(os.listdir(os.path.pardir))  # parent directory list


# 지정한 경로의 상위 경로를 포함한 모든 경로를 생성한다.
def _make_dirs(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise


# 파일명 변경(파일 경로 포함한 Parameter 사용)
def _change_name(original_file, changed_file):
    os.rename(original_file, changed_file)
