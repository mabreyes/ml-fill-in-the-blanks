from django.shortcuts import render
from pytorch_transformers import BertTokenizer, BertForMaskedLM
import torch
import nltk

from .forms import GeneratorForm


nltk.download('punkt')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained(
    'bert-base-uncased', output_attentions=True)
model.eval()

def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)

def generate_missing(value):
    status = None

    if '____' not in value:
        status = "success"
        return status, value

    try:
        sentence = value.replace('____', 'MASK')
        tokens = nltk.word_tokenize(sentence)
        sentences = nltk.sent_tokenize(sentence)
        sentence = " [SEP] ".join(sentences)
        sentence = "[CLS] " + sentence + " [SEP]"
        tokenized_text = tokenizer.tokenize(sentence)
        masked_index = tokenized_text.index('mask')
        tokenized_text[masked_index] = "[MASK]"
        indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)

        segments_ids = []
        sentences = sentence.split('[SEP]')
        for i in range(len(sentences)-1):
            segments_ids.extend([i]*len(sentences[i].strip().split()))
            segments_ids.extend([i])

        tokens_tensor = torch.tensor([indexed_tokens])
        segments_tensors = torch.tensor([segments_ids])

        with torch.no_grad():
            outputs = model(tokens_tensor, token_type_ids=segments_tensors)
            predictions = outputs[0]
            attention = outputs[-1]

        dim = attention[2][0].shape[-1]*attention[2][0].shape[-1]
        a = attention[2][0].reshape(12, dim)
        b = a.mean(axis=0)
        c = b.reshape(attention[2][0].shape[-1], attention[2][0].shape[-1])
        avg_wgts = c[masked_index]

        focus = [tokenized_text[i] for i in avg_wgts.argsort().tolist(
        )[::-1] if tokenized_text[i] not in ['[SEP]', '[CLS]', '[MASK]']][:5]

        predicted_index = torch.argmax(predictions[0, masked_index]).item()
        predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]

        for f in focus:
            value = value.replace(
                f, '<span class="attention">'+f+'</span>')

        status = "success"

        return status, value.replace('____', '<span class="predicted"><strong>'+predicted_token+'</strong></span>')

    except:
        status = "error"
        return status, "Sentence invalid. Please try a simpler sentence or remove symbols and special characters."


def base(request):
    submit_button = request.POST.get("submit")
    status = None
    g_val = None

    form = GeneratorForm(request.POST or None)

    if form.is_valid():
        text_area = form.cleaned_data.get("textarea")
        status, g_val = generate_missing(text_area)

    context = {
        'form': form,
        'status': status,
        'generated_value': g_val,
        'submit_button': submit_button
    }

    return render(request, 'generator.html', context)
