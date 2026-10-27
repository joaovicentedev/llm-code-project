from knowledge_base import knowledge_base


PROMPT = (
    "Answer questions about BEON.tech briefly using only the facts below. "
    "If the answer is not supported, say you don't know.\n\n"
    + "\n".join(f"- {fact}" for fact in knowledge_base)
)
