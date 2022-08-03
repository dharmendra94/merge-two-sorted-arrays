FROM python:3

ADD merge-two-sorted-arrays.py /

RUN pip install pystrich

ENTRYPOINT [ "python", "./merge-two-sorted-arrays.py"]CMD [ "[1,2]", "[3,4,5]" ]