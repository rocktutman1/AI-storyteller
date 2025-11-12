from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")

while True:
    try:
        desired = int(input ("How many story segments would you like to try? \n"))
        if desired > 0:
            print ("Do better")
            break
    except:
        print ("Do better")
prompt = input ("Write the start of your prompt: \n")
story = ""
story += prompt
for i in range(desired):
    result = generator(story[-100:], num_return_sequences=1, pad_token_id=generator.tokenizer.eos_token_id)
    print(result[0]['generated_text'])
    story += result[0]['generated_text']
    if i < desired - 1:
        prompt = input ("How should the story continue? \n")
        story += prompt


