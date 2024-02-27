import os
from typing import List
import fitz

class PDFFileLoader:
    def __init__(self, path: str):
        self.documents = []
        self.path = path

    def load_documents(self):
        extracted_text = ""
        doc = fitz.open(self.path)
        for page in doc:
            text = page.get_text()
            extracted_text += text 
        doc.close()
        self.documents.append(extracted_text)
        return self.documents

class CharacterTextSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        assert (
            chunk_size > chunk_overlap
        ), "Chunk size must be greater than chunk overlap"

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str) -> List[str]:
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunks.append(text[i : i + self.chunk_size])
        return chunks

    def split_texts(self, texts: List[str]) -> List[str]:
        chunks = []
        for text in texts:
            chunks.extend(self.split(text))
        return chunks
