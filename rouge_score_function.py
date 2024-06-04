#!pip install rouge
import pandas as pd
from rouge import Rouge

# 假设 df 是你的 DataFrame，并且有 'reference' 和 'generated' 两列
# df = pd.DataFrame({'reference': [...], 'generated': [...]})

# 初始化ROUGE计算器


# 函数来计算ROUGE分数
def compute_rouge_scores(row,generate="summaries",reference="articles"):
    rouge = Rouge()
    scores = rouge.get_scores(row[generate], row[reference], avg=True)
    return pd.Series({
        'rouge1_precision': scores['rouge-1']['p'],
        'rouge1_recall': scores['rouge-1']['r'],
        'rouge1_fmeasure': scores['rouge-1']['f'],
        'rouge2_precision': scores['rouge-2']['p'],
        'rouge2_recall': scores['rouge-2']['r'],
        'rouge2_fmeasure': scores['rouge-2']['f'],
        'rougeL_precision': scores['rouge-l']['p'],
        'rougeL_recall': scores['rouge-l']['r'],
        'rougeL_fmeasure': scores['rouge-l']['f']
    })

# 计算每行的ROUGE分数并将结果添加到DataFrame中

#df = df.join(df.apply(compute_rouge_scores, axis=1))

# 显示添加了ROUGE分数的新DataFrame
#print(df)