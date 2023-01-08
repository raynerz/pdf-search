import pypdf

def flatten_list(nested_list):
  """
  Flattens a n-dimensional nested list
  """
  # check if list is empty
  if not(bool(nested_list)):
      return nested_list

    # to check instance of list is empty or not
  if isinstance(nested_list[0], list):

      # call function with sublist as argument
      return flatten_list(*nested_list[:1]) + flatten_list(nested_list[1:])

  # call function with sublist as argument
  return nested_list[:1] + flatten_list(nested_list[1:])

 

# Find the lenght of each chapter
def bookmark_dict(bookmark_list, reader):
    result = []
    counter=0
    for i in range(len(bookmark_list)):
      try:
        dic = {
            "bookmark_title" : bookmark_list[i]["/Title"],
            "start_page" : reader.get_destination_page_number(bookmark_list[i])+1,
            "end_page" : reader.get_destination_page_number(bookmark_list[i+1])+1
        }
      except:
        dic = {
            "bookmark_title" : bookmark_list[i]["/Title"],
            "start_page" : reader.get_destination_page_number(bookmark_list[i])+1,
            "end_page": len(reader.pages)
        }
      result.append(dic)

    return result

def find_bookmarks(reader):
    flat_list = flatten_list(reader.outline)
    bookmarks = bookmark_dict(flat_list, reader)
    
    return bookmarks

def split_book_chapters(bookmarks, pdf_reader):
    chapters = []
    for i in bookmarks:
        concat_pages = ""
        for j in range(i["start_page"]-1, i["end_page"]):
            print(i["bookmark_title"] +str(j) + " -> " + str(i["start_page"]) + ":" + str(i["end_page"]))
            concat_pages = concat_pages + "\n" + pdf_reader.pages[j].extract_text().replace('\n', '')
            print("* Processed chapter *")
        chapters.append({"content": concat_pages, "meta": {"book_title": "DAMA-DMBOK Data Management Book of Knowledge", "chapter": i["bookmark_title"], "start_page" : i["start_page"], "end_page": i["end_page"]}})
    
    return chapters
    
def preprocess(book_location):
    reader = pypdf.PdfReader(book_location)
    bookmarks = find_bookmarks(reader)
    book = split_book_chapters(bookmarks, reader)

    return book