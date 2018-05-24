import docx
def read_docx(file_name):
    doc= docx.Document(file_name)
    content= '\n'.join([para.text for para in doc.paragraphs])
    return content

print read_docx('ss.docx')
