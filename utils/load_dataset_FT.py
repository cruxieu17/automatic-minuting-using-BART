import json
from datasets import load_dataset, load_metric, Dataset

def load(fn_dataset, train_size=20000):
    
    if fn_dataset == 'mediasum':
        with open('/content/drive/MyDrive/Journal/Datasets/mediasum_train.json', 'r') as out:
            train = json.load(out)
        id1 = train['id'][0:train_size]
        dial1 = train['dialogue'][0:train_size]
        summ1 = train['summary'][0:train_size]
        train = {}
        train['id'] = id1
        train['dialogue'] = dial1
        train['summary'] = summ1
        train_data = Dataset.from_dict(train)

        with open('/content/drive/MyDrive/Journal/Datasets/mediasum_dev.json', 'r') as out:
            val = json.load(out)
        val_data = Dataset.from_dict(val)

    if fn_dataset == 'samsum':
        raw_dataset = load_dataset("samsum")
        train_data = raw_dataset['train']
        val_data = raw_dataset['validation']

    if fn_dataset == 'dialogsum':
        with open('/content/drive/MyDrive/Journal/Datasets/DialSumm/dialogsum_train.json', 'r') as out:
            train = json.load(out)
        train_data = Dataset.from_dict(train)
        with open('/content/drive/MyDrive/Journal/Datasets/DialSumm/dialogsum_val.json', 'r') as out:
            val = json.load(out)
        val_data = Dataset.from_dict(val)

    return train_data, val_data
