# PDF - Search

## Requirements

1. In a fresh virtual environment run

```
$ pip3 install -r requirements.txt

```

2. Go to [openai.com/api](https://openai.com/api/) and create an API token. Create the following environment variable. 

```
$ export OPEN_AI_KEY="<your openai api token>"
```

## How to use

1. In the project root folder run the following command

```
$ python3 main.py
```
You should receive the following prompt

```
Welcome to your source of infinite knowledge


Select an option please:
1 to read a book,
2 to query
3 to exit
```
3. Select 1 and give the address of a .pdf

```
$ 1
$Enter the location of your book: ./books/any.pdf
```

4. After being prompted to select an option select

```
$ 2
$ Enter your query: <your query here>
```

## Known limitations

- No error handling, if an error occurs, you just need to run the program again and repeat the steps
- Your pdf's need to have a table of contents and being subdivided by chapters.
- The `preprocess.py` script divides the books by chapters located in the [PDF's xref table](https://pypdf2.readthedocs.io/en/latest/dev/pdf-format.html) if your chapters are longer than 4096 [open api tokens](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) or about 300 words you will get the following error

```
$ openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens, however you requested 6711 tokens (6211 in your prompt; 500 for the completion). Please reduce your prompt; or completion length.

```

In that case you have two options
1. You can choose a book/pdf with shorter chapters for example (Kimball's data warehouse toolkit)[https://www.amazon.com/Data-Warehouse-Toolkit-Definitive-Dimensional/dp/1118530802]
2. You can modify `preprocess.py` to account for shorter amount of text when splitting the chapters. Issuing a PR would be cool :P



