import os
import shutil
from pagemethods import generate_page


def copy_static(src, dest):
    base_dir = "/home/threatt_zm/static-site-generator"
    src_path = os.path.join(base_dir, src)
    dest_path = os.path.join(base_dir, dest)

    try:
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        os.mkdir(dest_path)
        if os.path.exists(src_path):
            for item in os.listdir(src_path):
                file_path = os.path.join(src_path, item)
                if os.path.isfile(file_path):
                    shutil.copy(file_path, dest_path)
                else:
                    new_src = os.path.join(src, item)
                    new_dest = os.path.join(dest, item)
                    copy_static(new_src, new_dest)
    except Exception as e:
        print(f"Exception encountered: {e}")

def main():
    copy_static("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == '__main__':
    main()