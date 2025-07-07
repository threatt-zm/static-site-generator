from textnode import TextNode, TextType

def main():
    my_textnode = TextNode("This text is bolded", TextType.BOLD_TEXT)

    print(my_textnode)


if __name__ == '__main__':
    main()