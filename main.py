import streamlit as st
import os
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

# Initialize session state
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def extract_video_id(url):
    if 'youtu.be/' in url:
        return url.split('youtu.be/')[-1].split('?')[0]
    elif 'watch?v=' in url:
        return url.split('v=')[-1].split('&')[0]
    return None

def load_transcript(video_id):
    transcript_list = YouTubeTranscriptApi().list(video_id)
    transcript = transcript_list.find_transcript(['en'])
    transcript_data = transcript.fetch()
    return " ".join(chunk.text for chunk in transcript_data)

def create_vector_store(transcript):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])
    return FAISS.from_documents(chunks, embeddings)

def get_answer(question, vector_store):
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    docs = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that answers questions based on YouTube video transcripts. Use only the provided context to answer."),
        ("user", f"Context: {context}\n\nQuestion: {question}")
    ])
    
    chain = prompt | llm
    response = chain.invoke({})
    return response.content

client = ChatOpenAI(model = 'gpt-4o-mini')

def Translate(language_code, text):
    """
    language_code: source language code (hi, mr, ta, en, etc.)
    text: input text
    returns: English translation
    """

    if not text.strip():
        return ""

    if language_code == "en":
        return text

    prompt = f"""
    Translate the following text from language code '{language_code}' to English.
    Only return the translated text. No explanations.

    Text:
    {text}
    """

    response = client.invoke(prompt).content

    return response


def main():
    print("Yt chat pipeline initialised")

if __name__ == "__main__":
    main()