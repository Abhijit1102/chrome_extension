import re
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
class DocumentProcessor:
    def __init__(self, url):
        self.url = url
        self.chunk_size = 1000
        self.chunk_overlap = 50
        self.cleaned_chunks = None

    def process_all(self):
        """Load, split, and clean the content from the URL."""
        loader = WebBaseLoader(self.url)
        documents = loader.load()

        # Combine all page contents into one string
        full_text = " ".join(doc.page_content for doc in documents)

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        chunks = splitter.split_text(full_text)

        # Clean each chunk
        self.cleaned_chunks = [
            re.sub(r'\s+', ' ', chunk).strip()
            for chunk in chunks
        ]

    def get_cleaned_chunks(self):
        return self.cleaned_chunks

