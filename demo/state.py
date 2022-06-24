import streamlit as st

def init():
    """Initialize State."""
    if "index" not in st.session_state:
        st.session_state["index"] = 1

@st.cache(
    allow_output_mutation=True,
    suppress_st_warning=True,
    show_spinner=False,
)

def load_video(files):
    """Load video.

    Returns:
        TODO
    """
    return files.getvalue()
    with MemoryFS() as fs:
        for file in files:
            with fs.open(file.name, "wb") as io:
                io.write(file.getvalue())
        try:
            documents = Document.from_dir(".", fs=fs)
            st.write(f"Loaded {len(documents)} documents")
        except FileNotFoundError:
            documents = []
            st.write("No documents found")
        return documents