import os
from blockfunctions import markdown_to_html_node

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

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.strip("# ")
    raise ValueError("h1 header not found")

def generate_page(src_path, template_path, dest_path):
    print(f"Generating page from {src_path} to {dest_path} using {template_path}")

    base_path = "/home/threatt_zm/static-site-generator"
    src = os.path.join(base_path, src_path)
    temp = os.path.join(base_path, template_path)
    dest = os.path.join(base_path, dest_path)

    try:
        open_src = open(src, 'r')
        md = open_src.read()

        open_temp = open(temp, 'r')
        template = open_temp.read()

        node = markdown_to_html_node(md)
        html_string = node.to_html()
        title = extract_title(md)
        new_template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

        if not os.path.exists(os.path.dirname(dest)):
            os.makedirs(os.path.dirname(dest))
        open_dest = open(dest, 'w')
        open_dest.write(new_template)

        open_src.close()
        open_temp.close()
        open_dest.close()
    except Exception as e:
        print(f"Exception found: {e}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    base_path = "/home/threatt_zm/static-site-generator"
    src = os.path.join(base_path, dir_path_content)
    temp = os.path.join(base_path, template_path)
    dest = os.path.join(base_path, dest_dir_path)

    try:
        for item in os.listdir(src):
            new_src = os.path.join(dir_path_content, item)
            new_dest = os.path.join(dest_dir_path, item)
            item_path = os.path.join(src, item)
            if os.path.isfile(item_path):
                generate_page(new_src, template_path, new_dest.replace(".md", ".html"))
            else:
                generate_pages_recursive(new_src, template_path, new_dest)
    except:
        print(f"Exception found: {e}")  