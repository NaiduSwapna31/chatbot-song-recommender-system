pip install boto3
python tools/test_api.py -f 127.0.0.1 -p 8080 \
-c "Hi, Eddie, what's up?" \
-c "Not much, what about you?" \
-c "Fine, thanks. Are you going to the movies tomorrow?"
{'response': "Yes. I was going to go but didn't know you're coming!"}
pip install PyJWT==1.7.1

{
"document_tone": {
"tones": [
{
"score": 0.6165,
"tone_id": "sadness",
"tone_name": "Sadness"
},
{
"score": 0.829888,
"tone_id": "analytical",
"tone_name": "Analytical"
}
]
},
"sentences_tone": [
{
"sentence_id": 0,
"text": "Team, I know that times are tough!",
"tones": [
{
"score": 0.801827,
"tone_id": "analytical",
"tone_name": "Analytical"
}
]
},
{
"sentence_id": 1,
"text": "Product sales have been disappointing for the past three
quarters.",
"tones": [
{
"score": 0.771241,
"tone_id": "sadness",
"tone_name": "Sadness"
},
{
"score": 0.687768,
"tone_id": "analytical",
"tone_name": "Analytical"
}
]
},
{
"sentence_id": 2,
"text": "We have a competitive product, but we need to do a better
job of selling it!",
"tones": [
{
"score": 0.506763,
"tone_id": "analytical",
"tone_name": "Analytical"
}
]
}
]
}
{
"document_tone": {
"tones": [
{
"score": 0.66525,
"tone_id": "joy",
"tone_name": "Joy"
}
]
},
"sentences_tone": [
{
"sentence_id": 0,
"text": "Hey there!! What's up?",
"tones": []
},
{
"sentence_id": 1,
"text": "How's the day?",
"tones": []
}
]
}
{
"anger": "anger",
"fear":"sadness",
"joy":"joy",
"sadness":"sadness",
"analytical":"neutral",
"confident":"neutral",
"tentative":"neutral"
}
{ "context": [
"Hey there!! What's up? How's the day?"
],
"emotion": "joy"
}
{ "response": "It's been good. How about you?" }
{
"tracks": {
"track": [
{...},
{...}
],
"@attr": {
"tag": "analytical",
"page": "1",
"perPage": "5",
"totalPages": "1",
"total": "2"
}
}
}
