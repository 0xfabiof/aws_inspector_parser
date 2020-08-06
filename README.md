# aws_inspector_parser

A simple python script to parse the current HTML report from AWS Inspector to a neat tabled format
vulnerable_package:identified_cve

# usage

python inspector_parser.py <html_report_path>

# sample output

libxml2-0:2.9.1-6.amzn2.3.3, libxml2-python-0:2.9.1-6.amzn2.3.3:CVE-2016-5131
libxml2-0:2.9.1-6.amzn2.3.3, libxml2-python-0:2.9.1-6.amzn2.3.3:CVE-2017-15412
libxml2-0:2.9.1-6.amzn2.3.3, libxml2-python-0:2.9.1-6.amzn2.3.3:CVE-2017-18258
libxml2-0:2.9.1-6.amzn2.3.3, libxml2-python-0:2.9.1-6.amzn2.3.3:CVE-2018-10360
file-0:5.11-35.amzn2.0.2, file-libs-0:5.11-35.amzn2.0.2:CVE-2018-14404
libxml2-0:2.9.1-6.amzn2.3.3, libxml2-python-0:2.9.1-6.amzn2.3.3:CVE-2018-14567
libxml2-0:2.9.1-6.amzn2.3.3, libxml2-python-0:2.9.1-6.amzn2.3.3:CVE-2018-20060
