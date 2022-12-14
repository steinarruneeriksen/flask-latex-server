
import subprocess
import os
class TexManager:
    @staticmethod
    def ceate_pdf(tex_content):
        fname="dummy"
        with open(fname + ".tex", "w") as tex_file:
            tex_file.write(tex_content)
        subprocess.call(["pdflatex", fname + ".tex"])
        pdf_file_in_bytes = open(fname + ".pdf", 'rb').read()
        for suffix in ['tex', 'log', 'aux', 'pdf']:
            os.remove(fname + "." + suffix)
        return pdf_file_in_bytes