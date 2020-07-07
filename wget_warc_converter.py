#! /usr/bin/env python3

# imports
import sys
from warcio.archiveiterator import ArchiveIterator
from warcio.warcwriter import WARCWriter
from argparse import ArgumentParser

def main(args):
    output = open(args.output, 'wb')
    writer = WARCWriter(output, gzip=True)

    with open(args.input, 'rb') as stream:
        for record in ArchiveIterator(stream):
            if 'WARC-Target-URI' in record.rec_headers:
                record.rec_headers['WARC-Target-URI'] = record.rec_headers['WARC-Target-URI'].lstrip('<').rstrip('>')
            writer.write_record(record)

    output.close()

if __name__ == "__main__":
    parser = ArgumentParser(description="Convert WARC files created by Wget to WARC 1.1")
    parser.add_argument('-i', '--input', help="input WARC file", required=True)
    parser.add_argument('-o', '--output', help="output WARC file", required=True)
    args = parser.parse_args()
    main(args)