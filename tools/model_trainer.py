import replicate

training = replicate.trainings.create(
  version="replicate/llama-2-7b:4841472f9a9d279cf03ba0a8f633b13eccd0e0a033d3af0c9b58830982d33132",
  input={
    "train_data":"https://replicate.delivery/pbxt/JaMVbMYlH8WUAeToWyQHHslrBLSzOSlqIHikLdc4lxG6cAxk/mini-summarization-training-ds-forllama-text.jsonl",
    "num_train_epochs": 3
  },
  destination="coder-lgtm/summarizer-mega"
)

print(training)