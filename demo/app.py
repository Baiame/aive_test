"""Streamlit App to process videos."""

import streamlit as st
import numpy as np
import cv2 as cv
import tempfile
from pathlib import Path

from demo import state
from src import HumanVideoDetection


def main():
    """Main Application."""
    st.set_page_config(page_title="Document Reading")
    state.init()

    uploaded_file = st.file_uploader("Upload file")

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            fp = Path(tmp_file.name)
            fp.write_bytes(uploaded_file.getvalue())


            hvd = HumanVideoDetection()



            tfile = tempfile.NamedTemporaryFile(delete=False) 
            tfile.write(f.read())


            vf = cv.VideoCapture(tfile.name)

            stframe = st.empty()


if __name__ == '__main__':
    main()