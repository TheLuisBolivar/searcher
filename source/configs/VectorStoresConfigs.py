from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from configs.ModelsConfigs import OpenAIConfig;

class VectorStoresConfigs:
    """
    Configuration class for vector store operations.
    Handles the creation and management of FAISS vector stores with OpenAI embeddings.
    """

    @staticmethod
    def get_faiss_vector_store(docs):
        """
        Create a FAISS vector store with OpenAI embeddings from the provided documents.
        
        Args:
            docs (list): List of text documents to create embeddings for
            
        Returns:
            FAISS: A FAISS vector store containing the document embeddings
            
        Note:
            If no documents are provided, returns an empty FAISS index initialized with a dummy text
        """
        openai_api_key = OpenAIConfig.load_openai_api_key()
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        
        if not docs:
            # Initialize with a dummy text to set up the embedding dimension
            dummy_text = "This is a dummy text to initialize the FAISS index."
            return FAISS.from_texts([dummy_text], embeddings)
            
        vector_store = FAISS.from_texts(docs, embeddings)
        return vector_store