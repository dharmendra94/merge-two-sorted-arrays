FROM python:3

ADD code/merge_two_sorted_arrays.py /

ENTRYPOINT [ "python", "./merge_two_sorted_arrays.py"]