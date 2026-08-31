import streamlit as st

from src.generation.llm import generate_rag_answer
from src.ingestion.pipeline import ingest_documents
from src.processing.vector_store import collection
from src.ingestion.pdf_loader import extract_text_from_pdf

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="IntraMind CampusAI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* ===== MAIN APP ===== */

    .stApp {
        background-color: #F7F4EC;
        color: #2F4033;
    }

    [data-testid="stHeader"] {
        background-color: #F7F4EC;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 6rem;
    }


    /* ===== SIDEBAR ===== */

    [data-testid="stSidebar"] {
        background-color: #E6E9E0;
        border-right: 1px solid #D4D9CF;
    }

    [data-testid="stSidebarContent"] {
        padding: 2rem 1.4rem;
    }

    /* ===== SIDEBAR BRANDING ===== */

.sidebar-brand {
    padding: 1rem 0.2rem 1.5rem 0.2rem;
}

.brand-icon {
    font-size: 2.2rem;
    margin-bottom: 0.6rem;
}

.brand-name {
    font-size: 2.05rem;
    font-weight: 750;
    color: #2F4937;
    line-height: 1.1;
    letter-spacing: -0.5px;
}

.brand-name span {
    color: #667A5B;
}

.brand-tagline {
    margin-top: 0.7rem;
    color: #738073;
    font-size: 0.95rem;
    line-height: 1.5;
}

    /* ===== HEADINGS ===== */

    h1 {
        color: #2F4937 !important;
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.2rem !important;
    }

    h2, h3 {
        color: #344E3B !important;
    }


    /* ===== TEXT ===== */

    .subtitle-text {
        color: #68756A;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
    }


    /* ===== CARDS ===== */

    .stButton > button {
        width: 100%;
        min-height: 75px;
        border-radius: 14px;
        border: 1px solid #D8DDD3;
        background-color: #FFFDF8;
        color: #344E3B;
        font-size: 0.95rem;
        text-align: left;
        padding: 1rem;
    }

    .stButton > button:hover {
        background-color: #EDF1E9;
        border-color: #A8B7A2;
    }


    /* ===== CHAT ===== */

    [data-testid="stChatMessage"] {
        background-color: #FFFDF8;
        border: 1px solid #E0E4DA;
        border-radius: 14px;
        padding: 0.5rem;
        margin-bottom: 1rem;
    }


    /* ===== CHAT INPUT ===== */

    [data-testid="stChatInput"] {
        background-color: #FFFDF8;
        border: 1px solid #D8DDD3;
        border-radius: 14px;
    }


    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-brand">
            <div class="brand-icon">🎓</div>
            <div class="brand-name">IntraMind <span>CampusAI</span></div>
            <div class="brand-tagline">
                Your intelligent campus assistant
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.subheader("Navigation")

    if "page" not in st.session_state:
      st.session_state.page = "Chat"

    if st.button("💬 Chat", use_container_width=True):
      st.session_state.page = "Chat"

    if st.button("📄 Documents", use_container_width=True):
      st.session_state.page = "Documents"

    if st.button("📚 Knowledge Base", use_container_width=True):
      st.session_state.page = "Knowledge Base"

      st.divider()

      st.subheader("💡 Knowledge Base")

      st.caption(
        "Ask questions about the university documents "
        "currently available in the system."
    )

    st.write("")

    if st.button("🗑️ Clear chat"):

      st.session_state.messages = []

      st.rerun()

# --------------------------------------------------
# MAIN PAGE
# --------------------------------------------------

if st.session_state.page == "Chat":

    st.caption("WELCOME TO")

    st.title("IntraMind CampusAI")

    st.markdown(
        '<p class="subtitle-text">'
        'Your AI-powered assistant for university information.'
        '</p>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([6, 1])

    with col2:
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()


    # --------------------------------------------------
    # CHAT HISTORY
    # --------------------------------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []


    # --------------------------------------------------
    # EMPTY STATE
    # --------------------------------------------------

    if not st.session_state.messages:

        st.subheader("How can I help you today?")

        st.write(
            "Ask me questions based on the documents available "
            "in the IntraMind knowledge base."
        )

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            registration = st.button(
                "📚  Module registration\n\nWhen should students complete module registration?",
                use_container_width=True,
            )

            deadlines = st.button(
                "📅  Academic deadlines\n\nWhat are the important academic deadlines?",
                use_container_width=True,
            )

        with col2:

            policies = st.button(
                "📄  Academic policies\n\nWhat academic policies are available?",
                use_container_width=True,
            )

            knowledge = st.button(
                "🔍  Knowledge base\n\nWhat information is available?",
                use_container_width=True,
            )

    else:

        registration = False
        deadlines = False
        policies = False
        knowledge = False


    # --------------------------------------------------
    # DISPLAY MESSAGES
    # --------------------------------------------------

    for message in st.session_state.messages:

        if message["role"] == "user":

            st.markdown("##### 👤 You")
            st.info(message["content"])

        else:

            st.markdown("##### 🎓 IntraMind")
            st.success(message["content"])

            if "sources" in message and message["sources"]:

                st.markdown("**📚 Sources**")

                for source in message["sources"]:
                    st.caption(f"📄 {source}")


    # --------------------------------------------------
    # QUESTION INPUT
    # --------------------------------------------------

    question = st.chat_input("Ask IntraMind a question...")


    # --------------------------------------------------
    # SUGGESTION BUTTONS
    # --------------------------------------------------

    if registration:
        question = "When should students complete module registration?"

    elif deadlines:
        question = "What are the important academic deadlines?"

    elif policies:
        question = "What academic policies are available?"

    elif knowledge:
        question = "What information is available in the knowledge base?"


    # --------------------------------------------------
    # GENERATE ANSWER
    # --------------------------------------------------

    if question:

        st.session_state.messages.append(
          {
             "role": "user",
             "content": question,
          }
        )

        with st.spinner("IntraMind is thinking..."):

           result = generate_rag_answer(question)

        answer = result["answer"]
        sources = result["sources"]

        st.session_state.messages.append(
           {
              "role": "assistant",
              "content": answer,
              "sources": sources,
           }
       )

        st.rerun()

elif st.session_state.page == "Documents":

    st.caption("DOCUMENT LIBRARY")

    st.title("University Documents")

    st.markdown(
        '<p class="subtitle-text">'
        'Browse and read the documents currently available to IntraMind.'
        '</p>',
        unsafe_allow_html=True,
    )

    st.divider()

    st.subheader("📄 Available Documents")

    from pathlib import Path

    docs_path = Path(__file__).parent / "docs"

    if docs_path.exists():

        markdown_documents = list(
            docs_path.glob("*.md")
        )

        pdf_documents = list(
            docs_path.glob("*.pdf")
        )

        documents = markdown_documents + pdf_documents

        if documents:

            for document in documents:

                if document.suffix.lower() == ".md":

                    with st.expander(
                        f"📄 {document.name}"
                    ):

                        content = document.read_text(
                            encoding="utf-8"
                        )

                        st.text(content)

                elif document.suffix.lower() == ".pdf":

                    with st.expander(
                        f"📕 {document.name}"
                    ):

                        pdf_documents = extract_text_from_pdf(
                            str(document)
                        )

                        if pdf_documents:

                            for pdf_document in pdf_documents:

                                st.text(
                                    pdf_document.text
                                )

                        else:

                            st.warning(
                                "No text could be extracted "
                                "from this PDF."
                            )

        else:

            st.warning(
                "No documents were found."
            )

    else:

        st.error(
            "The docs folder could not be found."
        )




elif st.session_state.page == "Knowledge Base":

    st.caption("KNOWLEDGE BASE")

    st.title("IntraMind Knowledge Base")

    st.markdown(
        '<p class="subtitle-text">'
        'Explore the information currently available to IntraMind.'
        '</p>',
        unsafe_allow_html=True,
    )

    st.divider()

    st.subheader("🔍 About the Knowledge Base")

    st.write(
        "IntraMind uses a Retrieval-Augmented Generation (RAG) system "
        "to search relevant university documents before generating an answer."
    )

    st.info(
        "The knowledge base is built from the university documents "
        "currently loaded into the system."
    )
    if st.button("🔄 Update Knowledge Base"):

       with st.spinner("Updating knowledge base..."):

         ingest_documents()

       st.success("Knowledge base updated successfully!")

    from pathlib import Path

    docs_path = Path(__file__).parent / "docs"

    markdown_documents = list(
        docs_path.glob("*.md")
    )

    pdf_documents = list(
        docs_path.glob("*.pdf")
    )

    documents = markdown_documents + pdf_documents

st.divider()

st.subheader("📊 Knowledge Base Overview")

total_documents = len(documents)
total_chunks = collection.count()

markdown_count = len(markdown_documents)
pdf_count = len(pdf_documents)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Documents Available",
        total_documents
    )

with col2:

    st.metric(
        "Total Chunks",
        total_chunks
    )

with col3:

    st.metric(
        "Document Types",
        2
    )

if documents:

    st.success(
        f"IntraMind currently has access to {total_documents} "
        "documents in its knowledge base."
    )

    st.subheader("📄 Document Types")

    type_col1, type_col2 = st.columns(2)

    with type_col1:

        st.write(
            f"📄 Markdown documents: {markdown_count}"
        )

    with type_col2:

        st.write(
            f"📕 PDF documents: {pdf_count}"
        )

    st.subheader("📚 Documents in the Knowledge Base")

    for document in documents:

        st.write(
            f"• {document.name}"
        )

else:

    st.warning(
        "No documents are currently available in the knowledge base."
    )
    