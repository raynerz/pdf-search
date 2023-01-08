import preprocess
import qa_pipeline
import gpt



def welcome():
    print("Welcome to your source of infinite knowledge")

def do_processing(book_location):
    book = preprocess.preprocess(book_location)
    global pipeline
    pipeline = qa_pipeline.build_pipeline(book)

def query(query):
    answer = gpt.answer_query_with_context(query, pipeline)
    return answer

if __name__=="__main__":
    welcome()
    while True:
        input_value = int(input('\n\nSelect an option please:\n1 to read a book,\n2 to query\n3 to exit\n'))
        if input_value == 1:
            input_query = input("Enter the location of your book: ")
            do_processing(input_query)
        elif input_value == 2:
            input_query = input("Enter your query: ")
            answer = query(input_query)
            print("GPT Answer: " + answer)
        elif input_value == 3:
            exit()
        else:
            print('Please enter a valid input.')