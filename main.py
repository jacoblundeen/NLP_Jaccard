from string import *

import pandas as pd
import numpy as np
# from plotnine import *
from typing import *


def read_docs(doc_name: str) -> List[List[str]]:
    f = open(doc_name, 'r')
    doc = f.readlines()
    return doc


def create_list(doc_A: List[List[str]]) -> List[str]:
    list_A = [x.lower() for x in doc_A]
    list_A = [x.split() for x in list_A]
    list_A = [item for row in list_A for item in row]
    list_A = [x.strip(punctuation) for x in list_A]
    list_A = set(list_A)
    return list_A


def calc_jaccard(list_A: List[str], list_B: List[str]) -> float:
    intersection = list_A.intersection(list_B)
    union = list_A.union(list_B)
    return float(len(intersection) / len(union))


def main():
    doc_A = read_docs('(original) nfr.txt')
    doc_B = read_docs('(original) nfr2.txt')
    list_A = create_list(doc_A)
    list_B = create_list(doc_B)
    jaccard_sim = calc_jaccard(list_A, list_B)
    print(jaccard_sim)


if __name__ == "__main__":
    main()
