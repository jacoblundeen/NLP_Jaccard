from string import *

import pandas as pd
import numpy as np
# from plotnine import *
from typing import *


def read_docs(doc_name: str) -> List[List[str]]:
    df = pd.read_csv(doc_name, header=None)
    return df


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


def compare_docs(doc_A, doc_B):
    columns = ['A_Index', 'B_Index', 'Jaccard_Score']
    output = pd.DataFrame(columns=columns)
    for index1, value1 in doc_A.iterrows():
        for index2, value2 in doc_B.iterrows():
            list_A = create_list(value1)
            list_B = create_list(value2)
            jaccard_sim = calc_jaccard(list_A, list_B)
            output = pd.concat([output, pd.DataFrame([[index1, index2, jaccard_sim]], columns=columns)],
                               ignore_index=True)
            if jaccard_sim == 1.0:
                break
    return output


def edit_df(diff):
    values = list(diff.query("Jaccard_Score == 1.0")['A_Index'])
    df1 = diff.drop(diff.query('A_Index == @values & Jaccard_Score != 1.0').index)
    return df1


def main():
    doc_A = read_docs('document_a.txt')
    doc_B = read_docs('document_b.txt')
    diff = compare_docs(doc_A, doc_B)
    output = edit_df(diff)
    output.to_csv('jaccard_comparison.csv', index=False)


if __name__ == "__main__":
    main()
