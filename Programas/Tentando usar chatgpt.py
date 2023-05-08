import openai
openai.api_key = "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"
prompt=input('Me pergunte algo: ')

#model_engine= "davinci"
model_engine = "text-davinci-002"

max_tokens = 150
temperature = 0.1

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature
)
print(response.choices[0].text)