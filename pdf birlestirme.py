from PyPDF2 import PdfMerger


# PDF dosyalarını birleştir
def pdf_birlestir(pdf_listesi, cikti_pdf):
    birlestirici = PdfMerger()

    for pdf in pdf_listesi:
        birlestirici.append(pdf)

    birlestirici.write(cikti_pdf)
    birlestirici.close()
    print(f"{cikti_pdf} başarıyla oluşturuldu.")


# Kullanım
pdf_listesi = ['1.pdf', '2.pdf']  
cikti_pdf = 'yeni.pdf'  

pdf_birlestir(pdf_listesi, cikti_pdf)
