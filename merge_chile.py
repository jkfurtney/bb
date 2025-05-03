from pikepdf import Pdf
import pikepdf
from glob import glob
import numpy as np

pdf = Pdf.new()
data = (('c:/users/jfurtney/dropbox/home/bb/chile/00_Geography of Chile - Wikipedia.pdf',
         [16,17,18,19]),
        ('c:/users/jfurtney/dropbox/home/bb/chile/01_History of Chile - Wikipedia.pdf',
         list(range(19,30))),
        ('c:/users/jfurtney/dropbox/home/bb/chile/02_Pablo Neruda - Wikipedia.pdf',
         list(range(17,23))))


for fn, drop_indices in data:
    print(fn)
    src = Pdf.open(fn)
    drop_indices = np.array(drop_indices)-1
    keep = [i for j, i in enumerate(src.pages) if j not in drop_indices]
    pdf.pages.extend(keep)

pdf.save('chile_merged.pdf')

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

with pikepdf.open('chile_merged.pdf') as pdf:
    num_pages = len(pdf.pages)
    sig_sheets = 4
    sig_pages = sig_sheets*4
    for i, chunk in enumerate(chunks(pdf.pages, sig_pages)):
        print(len(chunk))
        dst = Pdf.new()
        for pg in chunk:
            dst.pages.append(pg)
        dst.save(f'cm_{i:02d}.pdf')

    # del pdf.pages[16:]
    # pdf.save('output.pdf')
