#! /usr/bin/env python
from __future__ import print_function

import argparse

import numpy as np
import pdf2image
from pyzbar.pyzbar import decode, ZBarSymbol

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='path to source pdf file to read from')

    return parser


def extract_code128(input, extractor=pdf2image.convert_from_path):
    result = []
    for page_num, page in enumerate(extractor(input), 1):
        img = np.asarray(page)
        for barcode_ind, decoded_object in enumerate(decode(img, symbols=[ZBarSymbol.CODE128])):
            result.append({'page': page_num, 'barcode_ind': barcode_ind, 'data': decoded_object.data.decode()})

    return result


def main(pdf_path):
    for code_data in extract_code128(pdf_path):
        print('Page: #{page}, data: {data}'.format(**code_data))


if __name__ == '__main__':
    args = get_parser().parse_args()
    main(args.source)
