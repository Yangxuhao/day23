##中文

import urllib.request
import pdfminer.pdfinterp
import pdfminer.converter
import pdfminer.layout
import io


def readpdf(psdfile):
    rsmgr=pdfminer.pdfinterp.PDFResourceManager()
    retstr=io.StringIO()
    lap=pdfminer.layout.LAParams()
    device=pdfminer.converter.TextConverter(rsmgr,retstr,laparams=lap)
    pdfminer.pdfinterp.process_pdf(rsmgr,device,pdffile)
    device.close()
    content=retstr.getvalue()
    retstr.close()
    return content
    pass

pdffile=urllib.request.urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputstring=readpdf(pdffile)
print(outputstring)