#%%
from docarray import DocumentArray
from jina import Flow, Client
docs = DocumentArray.from_csv("/home/aswin/documents/pepsearch/data/papers.csv", field_resolver={"abstract": "str"})
#%%
    # if cloud:
    # client = Client(host=HOST)
    # client.post(
    #     "/index", docs, show_progress=True, parameters={"traversal_path": "@r"}
    # )
    #else:
flow = Flow.load_config("flow-notebook.yml")
with flow:
    docs = flow.index(
        docs, show_progress=True, parameters={"traversal_path": "@r"}
    )
# %%
