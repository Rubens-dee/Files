__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
import os
import zipfile
cache_dir = os.path.abspath('cache')
zip_file = os.path.abspath('data.zip')


def clean_cache():
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)
    else:
        for files in os.scandir(cache_dir):
            os.remove(files)


clean_cache()


def cache_zip(zip, cache):
    with zipfile.ZipFile(zip, 'r') as zip:
        zip.extractall(cache)


cache_zip(zip_file, cache_dir)


def cached_files():
    file_list = []
    for file in os.listdir(cache_dir):
        file_list.append(os.path.join(cache_dir, file))
    return file_list


(cached_files())


def find_password(cached_files):
    for file in cached_files:
        with open(file) as file_read:
            lines = file_read.readlines()
            for line in lines:
                if line.find('password') != -1:
                    return line[10:-1]


print(find_password(cached_files()))
