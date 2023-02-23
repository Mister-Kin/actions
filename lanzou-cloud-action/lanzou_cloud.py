from lanzou.api import LanZouCloud
import os


def show_download_failed(code, filename):
    """显示失败文件的回调函数"""
    print(f"下载失败,错误码: {code}, 文件名: {filename}")


def show_upload_failed(code, filename):
    """显示失败文件的回调函数"""
    print(f"上传失败,错误码: {code}, 文件名: {filename}")


def after_downloaded(file_name):
    """下载完成后的回调函数"""
    print(f"下载成功，绝对路径为:{file_name}")


def handler(fid, is_file):
    if is_file:
        lzy.set_desc(fid, '由Github Action蓝奏云脚本批量上传', is_file=True)


lzy = LanZouCloud()
lzy.ignore_limits()
cookie = {
    'ylogin': os.environ['lanzou_cookie_id'],
    'phpdisk_info': os.environ['lanzou_cookie_value']
}

print("开始执行蓝奏云脚本")

if lzy.login_by_cookie(cookie) == LanZouCloud.SUCCESS:
    print("登录成功")
else:
    print("登录失败")
if os.environ['lanzou_is_download'] == 'true':
    print("开始执行下载")
    if os.environ['lanzou_is_file'] == 'true':
        lzy.down_file_by_id(os.environ['lanzou_target_id'],
                            os.environ['lanzou_target_path'],
                            overwrite=True,
                            downloaded_handler=after_downloaded)
    else:
        lzy.down_dir_by_id(os.environ['lanzou_target_id'],
                           os.environ['lanzou_target_path'],
                           mkdir=True,
                           failed_callback=show_download_failed,
                           overwrite=True,
                           downloaded_handler=after_downloaded,
                           recursive=True)
else:
    print("开始执行上传")
    if os.environ['lanzou_is_file'] == 'true':
        lzy.upload_file(os.environ['lanzou_target_path'],
                        os.environ['lanzou_target_id'],
                        uploaded_handler=handler)
    else:
        lzy.upload_dir(os.environ['lanzou_target_path'],
                       os.environ['lanzou_target_id'],
                       failed_callback=show_upload_failed,
                       uploaded_handler=handler)
