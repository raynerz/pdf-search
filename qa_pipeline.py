# In-Memory Document Store

from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import TfidfRetriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline


def build_document_store(docs):
    document_store = InMemoryDocumentStore()
    document_store.write_documents(docs)
    return document_store

def build_retriever(document_store):
    retriever = TfidfRetriever(document_store=document_store)
    return retriever

def build_reader():
    # Load a  local model or any of the QA models on
    # Hugging Face's model hub (https://huggingface.co/models)
    reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)

    return reader

def build_pipeline(book):
    # Extractive Pipeliline
    document_store = build_document_store(book)
    retriever = build_retriever(document_store)
    reader = build_reader()
    pipeline = ExtractiveQAPipeline(reader, retriever)
    return pipeline

def query(query, pipeline):
    prediction = pipeline.run(query, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}})
    return prediction
