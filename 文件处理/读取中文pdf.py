
import urllib.request
import pdfminer.pdfinterp
import pdfminer.converter
import pdfminer.layout
import pdfminer.pdfparser
import io


path=r"C:\Users\xuhao_yang\PycharmProjects\day23\谢宇进.pdf"

file=open(path,"rb")
pdffile=pdfminer.pdfparser.PDFParser(file)
doc=pdfminer.pdfparser.PDFDocument()
pdffile.set_document(doc)#解析工具链接pdf
doc.initialize()#为空为没有密码


rsmgr=pdfminer.pdfinterp.PDFResourceManager()
lap = pdfminer.layout.LAParams()
device = pdfminer.converter.PDFPageAggregator(rsmgr, laparams=lap)

interpreter=pdfminer.pdfinterp.PDFPageInterpreter(rsmgr,device)

for page in doc.get_pages():
    interpreter.process_page(page)#抓取每一页
    layout=device.get_result()
    for x in layout:
        text=x.get_text()
        print(text)