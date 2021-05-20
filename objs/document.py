from io import BytesIO, StringIO
import os
from pathlib import Path

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

class FineDocument:

    @classmethod
    def from_pdf_file (cls, filename :str, dir=None):
       
        output_string = StringIO()

        if dir is not None:

            workdir = dir

        else:
            os.chdir(os.path.dirname(__file__))
            root_dir = Path(Path.cwd().parents[0])
            workfile_dir = root_dir.joinpath(Path("docs")).joinpath(filename)

        
        with workfile_dir.open("rb") as fp:

            parser = PDFParser(fp)
            document = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)
            
            print(output_string.getvalue())

        return cls, output_string.getvalue()



        return cls, workdir

    def __init__(self, file : str):

        self.mtic = self.__get_mtic(file)

    def __parse_pdf_for_pattern (self, pattern:str, file:str):
        pass

    def __get_mtic(self, file:str):

        pattern = "(?!Montante total areembolsar MTIC)(.*\d)"

