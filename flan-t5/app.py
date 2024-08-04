from fastapi import FastAPI
from transformers import pipeline
 
# Create a new FastAPI app instance
app = FastAPI()
 
# Initialize the text generation pipeline
# This function will be able to generate text
# given an input.
pipe = pipeline("text2text-generation", model="google/flan-t5-small")
 
# Define a function to handle the GET request at `/generate`
# The generate() function is defined as a FastAPI route that takes a 
# string parameter called text. The function generates text based on the # input using the pipeline() object, and returns a JSON response 
# containing the generated text under the key "output"
@app.get("/generate")
def generate(text: str):
    """
    Using the text2text-generation pipeline from `transformers`, generate text
    from the given input text. The model used is `google/flan-t5-small`, which
    can be found [here](<https://huggingface.co/google/flan-t5-small>).
    """
    # Use the pipeline to generate text from the given input text
    output = pipe(text)
     
    # Return the generated text in a JSON response
    return {"output": output[0]["generated_text"]}