from docarray import DocumentArray
from jina import Flow, Client
#DATA_FILE = "/home/aswin/documents/pepsearch/data/papers.csv"
DATA_FILE = "/home/aswin/documents/example-knowledge-base-stackoverflow/data/small/Questions.csv"


def index(num_docs: int):
    print(f"Processing {num_docs} Documents")
    docs = DocumentArray.from_csv(
        DATA_FILE, field_resolver={"Title":"text"}
    )
    # if cloud:
    # client = Client("grpcs://nowapi-194b153979.wolf.jina.ai")
    # client.post(
    #     "/index", docs, show_progress=True, parameters={"traversal_path": "@r"}
    # )
    #else:
    flow = Flow.load_config("/home/aswin/documents/papers-search/backend/src/flow.yml")
    with flow:
        docs = flow.index(
            docs, show_progress=True, parameters={"traversal_path": "@r"}
        )
index(11)