from cat.looking_glass.stray_cat import StrayCat
from langchain.docstore.document import Document as Document
from starlette.datastructures import UploadFile

class RabbitHole:
    """Manages content ingestion. I'm late... I'm late!"""
    def ingest_memory(self, stray: StrayCat, file: UploadFile):
        """Upload memories to the declarative memory from a JSON file.

        Parameters
        ----------
        file : UploadFile
            File object sent via `rabbithole/memory` hook.

        Notes
        -----
        This method allows uploading a JSON file containing vector and text memories directly to the declarative memory.
        When doing this, please, make sure the embedder used to export the memories is the same as the one used
        when uploading.
        The method also performs a check on the dimensionality of the embeddings (i.e. length of each vector).

        """
    def ingest_file(self, stray: StrayCat, file: str | UploadFile, chunk_size: int | None = None, chunk_overlap: int | None = None, metadata: dict = {}):
        """Load a file in the Cat's declarative memory.

        The method splits and converts the file in Langchain `Document`. Then, it stores the `Document` in the Cat's
        memory.

        Parameters
        ----------
        file : str, UploadFile
            The file can be a path passed as a string or an `UploadFile` object if the document is ingested using the
            `rabbithole` endpoint.
        chunk_size : int
            Number of tokens in each document chunk.
        chunk_overlap : int
            Number of overlapping tokens between consecutive chunks.
        metadata : dict
            Metadata to be stored with each chunk.

        Notes
        ----------
        Currently supported formats are `.txt`, `.pdf` and `.md`.
        You cn add custom ones or substitute the above via RabbitHole hooks.

        See Also
        ----------
        before_rabbithole_stores_documents
        """
    def file_to_docs(self, stray: StrayCat, file: str | UploadFile, chunk_size: int | None = None, chunk_overlap: int | None = None) -> list[Document]:
        """Load and convert files to Langchain `Document`.

        This method takes a file either from a Python script, from the `/rabbithole/` or `/rabbithole/web` endpoints.
        Hence, it loads it in memory and splits it in overlapped chunks of text.

        Parameters
        ----------
        file : str, UploadFile
            The file can be either a string path if loaded programmatically, a FastAPI `UploadFile`
            if coming from the `/rabbithole/` endpoint or a URL if coming from the `/rabbithole/web` endpoint.
        chunk_size : int
            Number of tokens in each document chunk.
        chunk_overlap : int
            Number of overlapping tokens between consecutive chunks.

        Returns
        -------
        docs : List[Document]
            List of Langchain `Document` of chunked text.

        Notes
        -----
        This method is used by both `/rabbithole/` and `/rabbithole/web` endpoints.
        Currently supported files are `.txt`, `.pdf`, `.md` and web pages.

        """
    def string_to_docs(self, stray: StrayCat, file_bytes: str, source: str = None, content_type: str = 'text/plain', chunk_size: int | None = None, chunk_overlap: int | None = None) -> list[Document]:
        """Convert string to Langchain `Document`.

        Takes a string, converts it to langchain `Document`.
        Hence, loads it in memory and splits it in overlapped chunks of text.

        Parameters
        ----------
        file_bytes : str
            The string to be converted.
        source: str
            Source filename.
        content_type:
            Mimetype of content.
        chunk_size : int
            Number of tokens in each document chunk.
        chunk_overlap : int
            Number of overlapping tokens between consecutive chunks.

        Returns
        -------
        docs : List[Document]
            List of Langchain `Document` of chunked text.
        """
    def store_documents(self, stray: StrayCat, docs: list[Document], source: str, metadata: dict = {}) -> None:
        """Add documents to the Cat's declarative memory.

        This method loops a list of Langchain `Document` and adds some metadata. Namely, the source filename and the
        timestamp of insertion. Once done, the method notifies the client via Websocket connection.

        Parameters
        ----------
        docs : List[Document]
            List of Langchain `Document` to be inserted in the Cat's declarative memory.
        source : str
            Source name to be added as a metadata. It can be a file name or an URL.
        metadata : dict
            Metadata to be stored with each chunk.

        Notes
        -------
        At this point, it is possible to customize the Cat's behavior using the `before_rabbithole_insert_memory` hook
        to edit the memories before they are inserted in the vector database.

        See Also
        --------
        before_rabbithole_insert_memory
        """
    @property
    def file_handlers(self): ...
    @property
    def text_splitter(self): ...
