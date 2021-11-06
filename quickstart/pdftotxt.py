def pdf_to_txt(path):
    from tika import parser

    raw_pdf = parser.from_file(path)
    contents = raw_pdf['content']
    contents = contents.strip()
    contents = contents.split(". ")

    for i in range(len(contents)):
        contents[i] = contents[i].replace("\r\n", "")

    return contents


def books_to_list(path):
    contents = pdf_to_txt(path)
    for i in range(len(contents)):
        contents[i] = contents[i].replace("\n", "")

    return contents