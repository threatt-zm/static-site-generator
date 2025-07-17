import os
from blockfunctions import markdown_to_html_node

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
