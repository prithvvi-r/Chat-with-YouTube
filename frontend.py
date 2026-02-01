import streamlit as st
from main import extract_video_id, load_transcript, create_vector_store, get_answer, Translate
# UI
st.title("🎥 Chat with YouTube")

# URL Input Section
url = st.text_input("Enter YouTube URL:", placeholder="https://youtu.be/... or https://www.youtube.com/watch?v=...")



languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Tamil": "ta"
}

selected_language = st.selectbox(
    "Choose a video language",
    options=list(languages.keys())
)

language_code = languages[selected_language]

st.write("Selected:", selected_language)
st.write("Language code:", language_code)

if st.button("Load Video"):
    if url:
        with st.spinner("Loading transcript..."):
            try:
                video_id = extract_video_id(url)
                transcript = load_transcript(video_id)
                if language_code is not 'en':
                    transcript = Translate(language_code,transcript)
                st.session_state.vector_store = create_vector_store(transcript)
                st.session_state.chat_history = []
                st.success("✅ Video loaded! You can now ask questions.")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a YouTube URL")

# Chat Section
if st.session_state.vector_store:
    st.divider()
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if question := st.chat_input("Ask a question about the video..."):
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)
        
        # Get and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = get_answer(question, st.session_state.vector_store)
                st.write(answer)
                st.session_state.chat_history.append({"role": "assistant", "content": answer})

