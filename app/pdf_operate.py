#!/usr/bin/env python
#coding:utf-8

import PyPDF2, subprocess


def read_pdf_pages(file):
    with open(file, 'rb') as pdfFileObj:
        try:
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        except:
            return None
        else:
            return pdfReader.numPages


def switch_topdf(filename):
    cmd = "libreoffice --headless --convert-to pdf:writer_pdf_Export ../static/Upload_Files/BeforeSwitchFile/{} " \
          "--outdir /../static/Upload_Files/" .format(filename)
    try:
        returnCode = subprocess.call(cmd, shell=True)
        if returnCode != 0:
            raise IOError("{} failed to switch" .format(filename))
    except Exception:
        return 1
    else:
        return 0
