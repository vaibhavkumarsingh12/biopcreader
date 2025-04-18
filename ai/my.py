from google import genai

# Initialize the client with your API key
client = genai.Client(api_key="AIzaSyBhJs5B7iB_OOWcedHBFQLkr0PawsIG0RE")

def generate_blog(paragraph_topic):
    response = client.models.generate_content(
        model='gemini-2.0-flash-lite',
        contents='Write a paragraph about the following topic. ' + paragraph_topic,
        config={
            'temperature': 1.0,
            'max_output_tokens': 1000,
            'top_p': 0.8,
        }
    )

    # Correctly access the text from the Google Generative AI response
    return response.text

print(generate_blog('Why NYC is better than patna'))