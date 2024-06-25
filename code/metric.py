# -*- coding: UTF-8 -*-
"""
@File    ：metric.py
@Author  ：zfk
@Date    ：2024/5/9 16:15
"""
import json
from typing import List, Tuple
import nltk
from rouge import Rouge


def metric(pred: str, answer_list: List[str]) -> Tuple[float, dict]:
    # 计算BLEU
    print(pred, answer_list)
    reference = [answer.split() for answer in answer_list]
    candidate = pred.split()
    bleu_score = nltk.translate.bleu_score.sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25))

    # 计算ROUGE
    rouge = Rouge()
    rouge_scores = rouge.get_scores(pred, ' '.join(answer_list))

    return bleu_score, rouge_scores[0]['rouge-l']


if __name__ == '__main__':
    with open('../data/baidu_chat_results_BGE_automerge_plus.jsonl', 'r') as f:
        lines = f.readlines()
    
    bleu_scores = []
    rouge_l_p = []
    rouge_l_r = []
    rouge_l_f = []
    skipped_lines = []

    for i, line in enumerate(lines):
        data = json.loads(line)
        query = data.get('query')
        answer = data.get('answer')
        pred = data.get('pred')

        if answer is None or pred is None:
            print(f"Skipping line {i+1} due to None value: {data}")
            skipped_lines.append(i + 1)
            continue

        bleu, rouge_l = metric(pred.lower().strip(), [answer.lower().strip()])
        bleu_scores.append(bleu)
        rouge_l_p.append(rouge_l['p'])
        rouge_l_r.append(rouge_l['r'])
        rouge_l_f.append(rouge_l['f'])

    if bleu_scores:
        print(f"BLEU: {sum(bleu_scores) / len(bleu_scores)}")
    else:
        print("No valid BLEU scores calculated.")

    if rouge_l_p:
        print(f"ROUGE-L P: {sum(rouge_l_p) / len(rouge_l_p)}")
    else:
        print("No valid ROUGE-L P scores calculated.")

    if rouge_l_r:
        print(f"ROUGE-L R: {sum(rouge_l_r) / len(rouge_l_r)}")
    else:
        print("No valid ROUGE-L R scores calculated.")

    if rouge_l_f:
        print(f"ROUGE-L F: {sum(rouge_l_f) / len(rouge_l_f)}")
    else:
        print("No valid ROUGE-L F scores calculated.")
    
    if skipped_lines:
        print(f"Skipped lines: {skipped_lines}")
