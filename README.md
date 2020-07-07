# wget_warc_converter

## Requirements

* [Python3](https://www.python.org/downloads/)
* [warcio](https://github.com/webrecorder/warcio): `pip3 install warcio` (or `pip install warcio`)

## Usage

Base command:

```console
python3 wget_warc_converter.py -i $input_warc -o $output_warc
```

For example

```console
python3 wget_warc_converter.py -i /Users/nastasia/Desktop/wget-warc.warc.gz -o /Users/nastasia/Desktop/converted-warc.gz
```
