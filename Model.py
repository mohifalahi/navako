from transformers import pipeline

pipe = pipeline("text-classification", model="HooshvareLab/bert-fa-base-uncased-sentiment-digikala")

results = pipe.predict('این جمله دیدگاه مثبتی دارد')

print(results)
#>>> [{'label': 'recommended', 'score': 0.613567054271698}]