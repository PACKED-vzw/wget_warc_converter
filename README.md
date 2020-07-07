# wget_warc_converter

## Requirements

* [Python3](https://www.python.org/downloads/)
* [warcio](https://github.com/webrecorder/warcio): `pip3 install warcio` (or `pip install warcio`)

## Usage

Base command:

```shell
python3 wget_warc_converter.py --input $input_warc --output $output_warc
```

For example

```shell
python3 wget_warc_converter.py --input /Users/nvanderperren/Desktop/wget-warc.warc.gz --output /Users/nvanderperren/Desktop/converted-warc.gz
```
