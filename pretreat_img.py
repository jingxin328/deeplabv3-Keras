from PIL import Image
import os


def recursive_glob(rootdir='.', suffix=''):
    """Performs recursive glob with given suffix and rootdir
        :param rootdir is the root directory
        :param suffix is the suffix to be searched
    """
    return [os.path.join(looproot, filename)
            for looproot, _, filenames in os.walk(rootdir)
            for filename in filenames if filename.endswith(suffix)]


root = 'D:\\workspace\\deeplabv3-\\datasets\\cityscapes'
split = "train"
images_base = os.path.join(root, 'leftImg8bit', split)
results = recursive_glob(rootdir=images_base, suffix='.png')
print(len(results))

'''
image_folder = "imgs"

files = os.listdir(image_folder)
photo_num = 0

for file in files:  # 遍历文件夹
    im=Image.open(image_folder + "/" + file)  # 打开文件
    im.convert('RGB').save(image_folder + "/"+str(photo_num)+".jpg", "JPEG")
    photo_num = photo_num+1
print(photo_num, 'photo change!')
'''




