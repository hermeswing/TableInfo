from requests import get

from utils.fileUtils import _make_dirs


# 파일 다운로드
# target_dir : '/Temp'
def _download(target_dir, img_url, file_name=None):
    if not file_name:
        file_name = img_url.split('/')[-1]

    _make_dirs(target_dir)

    # with open(file_name, "wb") as file:  # 같은 폴더 내에 다운로드
    with open(target_dir + '/' + file_name, "wb") as file:  # 지정폴더 내에 다운로드
        response = get(img_url)
        file.write(response.content)
