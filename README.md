# ML Fill-in-the-Blanks
![Google BERT Representative Image](https://cdn-images-1.medium.com/max/1000/1*-oQKmzvHrzqeSQEnM9f_kQ.png)

ML Fill-in-the-Blanks is a natural language processing (NLP) model that is trained to predict the missing word in the sentence. This project uses pre-trained `bert-base-uncased` as the prediction model. 

Learn more about BERT [in this explainer](https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270). and [A visual guide](http://jalammar.github.io/a-visual-guide-to-using-bert-for-the-first-time/) is also available for access.


## Details
* Model - `bert-base-uncased`
* Pre-trained task - `MaskedLM`

## Usage
```bash
git clone git@github.com:mabreyes/tf-plant-disease-prediction.git
cd tf-plant-disease-prediction
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```
Visit the site in your local machine at `127.0.0.1:8000`

## Notes
The attention visualization is done for layer 3 across all attention heads by taking their average. Read more about heads and what they mean  [on this article](https://towardsdatascience.com/deconstructing-bert-part-2-visualizing-the-inner-workings-of-attention-60a16d86b5c1).