from objs.document import FineDocument

def run ():
    #instantiate parser

    fine = FineDocument.from_pdf_file("test_fine.pdf")

    print(fine.mtic)


    

if __name__ == "__main__":

    run()