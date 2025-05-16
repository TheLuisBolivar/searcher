from typing_extensions import TypedDict

class DeepSearch(TypedDict):
    """
    A TypedDict class representing the structure for deep search results.
    
    Attributes:
        query (str): The main search query
        keyword (str): The main search keyword used for the query
        keywords (list[str]): List of related or expanded keywords from the search
        results (list[str]): List of search results or findings
        companies (list[str]): List of companies or organizations found in the search
    """
    query: str
    keyword: str
    keywords: list[str]
    results: list[str]
    companies: list[str]