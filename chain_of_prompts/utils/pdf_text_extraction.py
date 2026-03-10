import fitz

def read_pdf(pdf_path):

    doc = fitz.open(pdf_path["pdf_path"])

    text_blocks = []

    for page in doc:
        blocks = page.get_text("blocks")

        blocks.sort(key=lambda b:(b[1],b[0]))

        for block in blocks:
            text_blocks.append(block[4])

    doc.close

    return "\n".join(text_blocks)

# if __name__ =="__main__":
#     pdf_path = "resume.pdf"
#     resume_text = read_pdf(pdf_path)

#     print(resume_text)