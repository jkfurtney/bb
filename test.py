import pikepdf
from pikepdf import Pdf


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

with pikepdf.open('Nature_drawing_and_design_removed.pdf') as pdf:
    num_pages = len(pdf.pages)
    sig_sheets = 4
    sig_pages = sig_sheets*4
    for i, chunk in enumerate(chunks(pdf.pages, sig_pages)):
        print(len(chunk))
        dst = Pdf.new()
        for pg in chunk:
            dst.pages.append(pg)
        dst.save(f'sub_{i:02d}.pdf')

    # del pdf.pages[16:]
    # pdf.save('output.pdf')
