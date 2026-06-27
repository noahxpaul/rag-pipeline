# prompt_builder.py

def estimate_tokens(text: str) -> int:
    """
    Rough token estimate: characters / 4
    """
    return len(text) // 4


def build_rag_prompt(question: str, chunks: list[dict]) -> str:
    """
    Builds a RAG prompt from retrieved chunks + user question.
    
    Each chunk should look like:
    {
        "source": "doc1.txt",
        "text": "chunk content here..."
    }
    """

    system_prompt = (
        "You are a helpful assistant. "
        "Answer the user's question ONLY using the provided context. "
        "If the answer is not in the context, say you don't know. "
        "Always cite sources using the source label in brackets."
    )

    # Format retrieved chunks
    context_block = "\n\n".join(
        [f"[Source: {chunk['source']}]\n{chunk['text']}" for chunk in chunks]
    )

    # Assemble final prompt
    full_prompt = f"""
{system_prompt}

-------------------------
CONTEXT:
-------------------------
{context_block}

-------------------------
QUESTION:
-------------------------
{question}

-------------------------
INSTRUCTIONS:
- Use only the context above
- Cite sources like [Source: doc_name]
- If missing info, say "I don't know based on the provided context"
"""

    return full_prompt.strip()


def run_test(question, chunks):
    prompt = build_rag_prompt(question, chunks)
    tokens = estimate_tokens(prompt)

    print("\n" + "=" * 80)
    print("ASSEMBLED PROMPT:\n")
    print(prompt)
    print("\n" + "-" * 80)
    print(f"Estimated tokens: {tokens}")
    print("=" * 80 + "\n")


if __name__ == "__main__":

    # Test Case 1
    chunks_1 = [
        {
            "source": "neural_nets.txt",
            "text": "Neural networks are composed of layers of nodes that transform input data."
        },
        {
            "source": "deep_learning.txt",
            "text": "Deep learning is a subset of machine learning using multi-layer neural networks."
        }
    ]

    question_1 = "What is deep learning?"
    run_test(question_1, chunks_1)

    # Test Case 2
    chunks_2 = [
        {
            "source": "python_basics.txt",
            "text": "Python lists are ordered collections that are mutable."
        },
        {
            "source": "python_advanced.txt",
            "text": "Decorators in Python modify the behavior of functions."
        }
    ]

    question_2 = "What are Python decorators?"
    run_test(question_2, chunks_2)