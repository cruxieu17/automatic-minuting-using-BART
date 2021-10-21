import torch
from transformers import BertTokenizer, BertForNextSentencePrediction
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForNextSentencePrediction.from_pretrained('bert-base-uncased')
device = torch.device('cuda')
model.to(device)
softmax = torch.nn.Softmax(dim=0)

def get_score(prompt, next_sentence):
    encoding = tokenizer(prompt, next_sentence, truncation=True, max_length=512, return_tensors='pt').to(device)
    outputs = model(**encoding, labels=torch.tensor([1], dtype=torch.long, device=device))
    logits = outputs['logits'].clone().detach().cpu()
    if logits[0][0] < logits[0][1]:
        score = -float(logits[0][1])
    else:
        score = float(logits[0][0])
    
    return score

def normalize(x, min_, max_):
    return (x-min_)/(max_-min_)

def get_seg_scores(utterances):
    wt=[2.71**(5*(_+1)/25) for _ in range(25)]
    seg_scores = []
    for i in range(1, len(utterances)):
        raw_scores = []
        for it in range(20):
            if i-it>=0:
                score = get_score(utterances[i-it], utterances[i])
                raw_scores.append(score)
            else:
                break
        
        sg_scr = 0
        min_ = min(raw_scores)
        max_ = max(raw_scores)
        normal_scores = []
        for rs in raw_scores:
            ns = normalize(rs, min_, max_)
            normal_scores.append(ns)
        # raw_scores = softmax(torch.tensor(raw_scores))
        for i_ in range(len(raw_scores)):
            sg_scr = sg_scr + wt[i_]*float(normal_scores[i_])
        
        sg_scr = sg_scr/(sum(wt[:i_+1]))
        seg_scores.append(round(sg_scr, 3))

    return seg_scores