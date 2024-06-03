import json

from llm_openai import safe_call_llm
from tqdm import tqdm

if __name__ == '__main__':

    table_file = '../dbgpt_hub/data/CSpider/tables.json'
    tables = json.load(open(table_file))
    save_path = '../dbgpt_hub/data/CSpider/tables_cn_gpt_new.json'

    prompt = '帮我翻译成中文,只保留翻译内容,格式为list不变,不要省略,号:\n{}'
    tables_new = []
    for x in tqdm(tables):
        
        for i in range(3):
            try:
                res_cols = safe_call_llm(prompt.format(x['column_names_original']))
                x['cn_column_names_original'] = eval(res_cols)
                break
            except:
                print('解析错误,重新推理: ', res_cols)
        for i in range(3):
            try:
                res_table = safe_call_llm(prompt.format(x['table_names_original']))
                x['cn_table_names_original'] = eval(res_table)
                break
            except:
                print('解析错误,重新推理: ', res_table)
        tables_new.append(x)

        # 存储
        with open(save_path, 'a') as jsonl_file:
            json_line = json.dumps(x, ensure_ascii=False)
            jsonl_file.write(json_line + '\n')