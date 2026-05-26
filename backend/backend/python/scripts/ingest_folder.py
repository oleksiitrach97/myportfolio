r"""Simple script to ingest PDF files into ChromaDB.

Run from project root:

powershell
cd D:\Data\ForDev\ai-portfolio-copilot-main\backend\python
D:\Data\ForDev\ai-portfolio-copilot-main\venv\Scripts\python.exe scripts\ingest_folder.py
"""
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from langchain_core.documents import Document
from rag.retriever import retriever

# PDF extraction support using pdfplumber (recommended for complex PDFs).
try:
    import pdfplumber
    _HAS_PDF_LIB = True
except Exception:
    _HAS_PDF_LIB = False


def _extract_pdf_text(path: Path) -> str:
    if not _HAS_PDF_LIB:
        raise RuntimeError("pdfplumber not installed; install with 'pip install pdfplumber' to enable PDF ingestion")
    try:
        texts = []
        with pdfplumber.open(str(path)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    texts.append(text)
        return "\n".join(texts)
    except Exception as e:
        print(f"Failed to extract PDF {path}: {e}")
        return ""


def ingest_folder(folder_path: str):
    p = Path(folder_path)
    docs = []
    if not p.exists():
        print(f"Folder not found: {folder_path}")
        return

    for file in p.rglob("*"):
        if file.is_file():
            try:
                suffix = file.suffix.lower()
                if suffix == ".pdf":
                    if not _HAS_PDF_LIB:
                        print(f"Skipping PDF (pdfplumber not installed): {file}")
                        continue
                    text = _extract_pdf_text(file)
                    if text:
                        docs.append(Document(page_content=text, metadata={"source": str(file), "type": "pdf"}))
                else:
                    # This ingester is intentionally PDF-only.
                    print(f"Skipping unsupported file type: {file}")
            except Exception as e:
                print(f"Failed to read {file}: {e}")

    if not docs:
        print("No documents found to ingest.")
        return

    num_chunks = retriever.process_and_store_documents(docs)
    print(f"Stored {num_chunks} chunks in vector DB")


if __name__ == '__main__':
    project_root = Path(__file__).resolve().parents[3]
    target = project_root / 'data' / 'domain_docs'
    print(f"Ingesting from: {target}")
    ingest_folder(str(target))
