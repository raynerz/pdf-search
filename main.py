import preprocess
import qa_pipeline
import gpt

if __name__ == "__main__":
    book = preprocess.preprocess("./books/dmbok2.pdf")

    pipeline = qa_pipeline.build_pipeline(book)

    haystack_prediction = qa_pipeline.query("what is a fact table?", pipeline)

    answer = gpt.answer_query_with_context(haystack_prediction)

    print(answer)