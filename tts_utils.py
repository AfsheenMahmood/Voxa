# tts_utils.py

from gtts import gTTS
from io import BytesIO
import base64
import streamlit as st

def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp
import base64
import streamlit as st
import time

import base64
import streamlit as st
import time

def play_audio(audio_bytes):
    unique_id = str(time.time())  # Create a unique timestamp-based ID
    b64 = base64.b64encode(audio_bytes.read()).decode()
    audio_html = f"""
    <audio id="audio_{unique_id}" autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    <script>
        var audio = document.getElementById("audio_{unique_id}");
        if (audio) {{
            audio.play().catch(e => {{
                console.log("Playback error:", e);
            }});
        }}
    </script>
    """
    st.markdown(audio_html, unsafe_allow_html=True)
