from docarray import DocumentArray
from jina import Flow, Client
flow = Flow.load_config("/home/aswin/documents/papers-search/backend/src/flow.yml")
with flow:
    flow.block()