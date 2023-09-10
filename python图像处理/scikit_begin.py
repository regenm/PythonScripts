from PIL import Image
from skimage import exposure, img_as_float, io    # 导入所需要的 skimage 库
import os

old_path = r"C:\Users\Regen\Pictures\screenshots"    # 原始文件路径
save_path = r"C:\Users\Regen\Pictures\screenshots_save"     # 需要存储的文件路径

file_list = os.walk(old_path)

