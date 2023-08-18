from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI
import os
from langchain.chains.summarize import load_summarize_chain

class Summarizer:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = "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"
        self.llm = ChatOpenAI(temperature=0)
    def summary(self, file):
        loader=PyPDFLoader(file)
        document=loader.load()
        summerizer=load_summarize_chain(self.llm, chain_type="map_reduce")
        summary=summerizer.run(document)
        return summary