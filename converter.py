import markdown

def convert(md_text):
    return markdown.markdown(md_text)

if __name__ == "__main__":
    md_text = "# Hello, World!\nThis is a test."
    print(convert(md_text))
