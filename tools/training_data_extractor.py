import json
import requests


# This python program builds custom prompts out of the input dataset and optinoally shortens the open source training dataset for conversations. 
# This allows us to be cost-effective while being experimental. 
# Open Source dataset credits - https://huggingface.co/datasets/samsum/viewer/samsum/train
def build_prompt_file(rows, shorten):
    modified_data = {}
    count = 0
    with open('mini-summarization-training-ds-forllama_text.jsonl', 'a') as json_file:
        for row in rows:
            if count > 299 & shorten == True:
                break
            #print (row)
            dialogue = row['row']['dialogue']
            summary= row['row']['summary']
            modified_data['text']= f"[INST] <<SYS>>\nUse the Input to provide a summary of a conversation.\n<<\/SYS>>\n\nInput:\n{dialogue} [\/INST]\n\nSummary: {summary}"
            json.dump(modified_data, json_file)
            json_file.write("\n")
            count += 1

    return count


total_rows_so_far = 0

while (True):
    print (f"pulling 100 rows from {total_rows_so_far}")
    r = requests.get(f"https://datasets-server.huggingface.co/rows?dataset=samsum&config=samsum&split=train&offset={total_rows_so_far}&limit=100")
    rdata = r.json()

    rows = rdata["rows"]
    row_data = []
    count = build_prompt_file(rows, False)
    total_rows_so_far += count
    if count < 100:
        break;

print (f"Total rows processed in current iteration = {total_rows_so_far}")
