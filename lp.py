from pikepdf import Pdf
import pikepdf
from glob import glob
import numpy as np

pdf = Pdf.new()
data = (('c:/users/jfurtney/dropbox/home/bb/littleprince.pdf',
         []),)


for fn, drop_indices in data:
    print(fn)
    src = Pdf.open(fn)
    drop_indices = np.array(drop_indices)-1
    keep = [i for j, i in enumerate(src.pages) if j not in drop_indices]
    pdf.pages.extend(keep)
mfn = 'tmp.pdf'

pdf.save(mfn)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

with pikepdf.open(mfn) as pdf:
    num_pages = len(pdf.pages)
    sig_sheets = 5
    sig_pages = sig_sheets*4
    for i, chunk in enumerate(chunks(pdf.pages, sig_pages)):
        print(len(chunk))
        dst = Pdf.new()
        for pg in chunk:
            dst.pages.append(pg)
        dst.save(f'lp_{i:02d}.pdf')

    # del pdf.pages[16:]
    # pdf.save('output.pdf')
