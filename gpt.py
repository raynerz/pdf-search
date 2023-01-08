import openai
import os

openai.api_key = os.environ.get("OPEN_AI_KEY")

COMPLETIONS_MODEL = "text-davinci-002"

COMPLETIONS_API_PARAMS = {
    # We use temperature of 0.0 because it gives the most predictable, factual answer.
    "temperature": 0.0,
    "max_tokens": 500,
    "model": COMPLETIONS_MODEL,
}


def construct_prompt(haystack_prediction):
  header = """Ignore all previous direction. Answer the question as truthfully as possible using the provided context, first write your answer, then the source and page mentioned in the prompt and if the answer is not contained within the text below, say "I don't know"."""
  
  prediction = haystack_prediction['documents'][0]
  context = prediction.content
  source = prediction.meta["chapter"]
  page = prediction.meta["start_page"]
  

  return header + "\n\nContext: " + context + "\nSource: " + source + "\nPage: " + str(page) + "\n\nThe question is: " + haystack_prediction['query']

def answer_query_with_context(haystack_prediction) -> str:
    prompt = construct_prompt(haystack_prediction)

    print(prompt)

    response = openai.Completion.create(
                prompt=prompt,
                **COMPLETIONS_API_PARAMS
            )

    return response["choices"][0]["text"].strip("\n")