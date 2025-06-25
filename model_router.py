# router.py

from llm_api import ask_llm

# model_router.py

def classify_query(text):
    """
    Classify a user query into one of the supported modes:
    - 'pdf_qa': Document-based questions
    - 'web_search': Queries that require external search
    - 'legal': Legal or law-related questions
    - 'general': General LLM chat
    """

    lowered = text.lower().strip()

    # Explicit reset or mode change request
    if any(kw in lowered for kw in ["change topic", "new topic", "reset", "restart", "start over", "clear chat","exit", "exit document", "stop this", "abandon", "forget this", "switch context"]
):
        return "reset"

    # PDF-related keywords
    pdf_keywords = [
        "in the document", "from the file", "from pdf", "the contract says", "what does it say", 
    "document summary","section" "according to the document", "based on this file", 
    "this clause", "this section",  "clause", "page", "highlighted part", 
    "excerpt", "text says", "in this passage", "in this agreement", "this paragraph"
    ]

    if any(kw in lowered for kw in pdf_keywords):
        return "pdf_qa"

    # Web search queries
    search_keywords = ["last", "search", "look up", "find", "latest", "news", "trending", 
    "who is", "when is", "how to", "current", "what's new", 
    "update", "real-time", "breaking news", "recent", "happening", "right now"
    "top stories", "check online", "google", "bing", "yahoo", "reddit", 
    "show me", "tell me about", "learn about", "lookup", "trends", 
    "forecast", "statistic", "report", "live score", "weather", "event"]
    if any(kw in lowered for kw in search_keywords):
        return "web_search"

    return "general"

