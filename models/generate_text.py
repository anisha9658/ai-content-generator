from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-small")

def generate_text(title, content_type, genre, style, audience):
    prompt = f"Write a {style} {content_type} in the {genre} genre for {audience or 'a general audience'} titled '{title}'."
    result = generator(
        prompt,
        max_length=500,         # Increase max output length
        do_sample=True,
        temperature=0.9,        # Add randomness
        top_k=50,
        top_p=0.95
    )[0]['generated_text']
    return result
