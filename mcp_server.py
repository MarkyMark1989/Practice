from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.tool()
def read_doc(doc_id: str) -> str:
    """Read the contents of a document by its ID."""
    if doc_id not in docs:
        return f"Error: document '{doc_id}' not found. Available docs: {', '.join(docs.keys())}"
    return docs[doc_id]


@mcp.tool()
def update_doc(doc_id: str, content: str) -> str:
    """Update the contents of a document by its ID."""
    if doc_id not in docs:
        return f"Error: document '{doc_id}' not found. Available docs: {', '.join(docs.keys())}"
    docs[doc_id] = content
    return f"Document '{doc_id}' updated successfully."
@mcp.resource("docs://list")
def list_doc_ids() -> str:
    """Returns all available document IDs."""
    return "\n".join(docs.keys())


@mcp.resource("docs://{doc_id}")
def get_doc_contents(doc_id: str) -> str:
    """Returns the contents of a specific document."""
    if doc_id not in docs:
        return f"Error: document '{doc_id}' not found."
    return docs[doc_id]


@mcp.prompt()
def rewrite(doc_id: str) -> str:
    """Prompt to rewrite a document in markdown format."""
    if doc_id not in docs:
        return f"Error: document '{doc_id}' not found."
    return f"Rewrite the following document in clean markdown format with appropriate headings, bullet points, and formatting:\n\n{docs[doc_id]}"


@mcp.prompt()
def summarize(doc_id: str) -> str:
    """Prompt to summarize a document."""
    if doc_id not in docs:
        return f"Error: document '{doc_id}' not found."
    return f"Please provide a concise summary of the following document:\n\n{docs[doc_id]}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
