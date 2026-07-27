"""
Simple RAG Engine
Version 1
"""


from backend.rag.knowledge_base import KNOWLEDGE_BASE


class RAGEngine:

    def search(self, query):

        query = query.lower()

        if "route" in query:
            return KNOWLEDGE_BASE["routes"]

        elif "time" in query:
            return KNOWLEDGE_BASE["timings"]

        elif "fare" in query:
            return KNOWLEDGE_BASE["fare"]

        elif "cancel" in query:
            return KNOWLEDGE_BASE["cancellation"]

        elif "support" in query:
            return KNOWLEDGE_BASE["support"]

        return KNOWLEDGE_BASE["welcome"]
