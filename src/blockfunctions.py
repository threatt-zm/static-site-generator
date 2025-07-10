

def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    strip_blocks = list(map(lambda x: x.strip(), split_blocks))
    new_blocks = filter(lambda x: x != "", strip_blocks)
    return new_blocks