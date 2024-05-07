import uuid
import os
import posthog
import streamlit as st

from langchain.chat_models.ollama import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

try:
    posthog.api_key = os.environ["POSTHOG_API_KEY"]
    posthog.host = os.environ['POSTHOG_HOST']
except KeyError:
    raise ValueError("Please set POSTHOG_API_KEY and POSTHOG_HOST environment variables")



model_name = "llama3:latest"
llm = ChatOllama(temperature=0.0, model=model_name)
memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory, verbose=True)


def task(distinct_id, input, output, event="llm-task", timestamp=None, session_id=None, properties=None):
    props = properties if properties else {}
    props["$llm_input"] = input
    props["$llm_output"] = output

    if session_id:
        props["$session_id"] = session_id

    posthog.capture(
        distinct_id=distinct_id, event=event, properties=props, timestamp=timestamp, disable_geoip=False
    )


def predict(message):
    response = chain.invoke({"input": message})
    return response["response"]


st.title(f"Ollama model: {model_name}")

if "messages" not in st.session_state or "session_id" not in st.session_state:
    st.session_state.messages = []
    st.session_state.session_id = uuid.uuid4().hex
    st.session_state.user_id = uuid.uuid4().hex


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type here..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = predict(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    task(
        distinct_id=st.session_state.user_id,
        input=prompt,
        output=response,
        event="llm-task",
        session_id=st.session_state.session_id,
        properties={"model": model_name},
    )
