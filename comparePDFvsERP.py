import streamlit as st
import requests
import json
import time

page_title="GenAI Builder - Content Reconciliation"
title="Content reconciliation between PDF Contracts and ERP"
# SnapLogic RAG pipeline
URL = 'https://ec2-13-37-172-69.eu-west-3.compute.amazonaws.com:8081/api/1/rest/feed/run/task/ConnectFasterInc/Toni/Toni_GenAI_Contracts-Reconciliation/Content_Reconciliation_API'
BEARER_TOKEN ='vktUhPn5qtMfLr4DqfpZW1mS9cNiT0gM'
timeout = 90



def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)



st.set_page_config(page_title=page_title)
st.title(title)
time.sleep(1.0)
with st.chat_message("assistant"):
    st.markdown("Welcome! 👋")

time.sleep(1.0)
with st.chat_message("assistant"):
    st.markdown("Select the PDF Contract to check against the ERP")
    
time.sleep(0.5)
uploaded_file = st.file_uploader(' ')
if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    with st.chat_message("assistant"):
        st.markdown("Successful Upload !")
    time.sleep(0.5)
    with st.chat_message("assistant"):
        st.markdown("Click below to launch the content comparison!")    
    if st.button(":blue[Analyze!]"):
        with st.spinner("Comparing PDF and ERP ..."):
            headers = {
                'Authorization': f'Bearer {BEARER_TOKEN}',
                'Content-Type': 'application/octet-stream'
            }
            response = requests.post(
                url=URL,
                data=file_bytes,
                headers=headers,
                timeout=timeout,
                verify=False
            )
            result = response.json()[0]["result"]
            message = f"Comparison completed for the contract N˚ **{result['pdf']['referenceClient']}** for customer **{result['pdf']['nomClient']}**"
            with st.chat_message("assistant"):
                typewriter(text=message,speed=10)
            time.sleep(1.0)
            with st.chat_message("assistant"):
                typewriter(text="Here's the result:", speed=10)
            if result["status"] == "OK":
                time.sleep(1.0)
                typewriter(text=f"✅ {result['message']}", speed=10)            
                time.sleep(1.0)
                typewriter(text="The price revision formula is the following:", speed=10)            
                time.sleep(1.0)
                st.latex(f"{result['pdf']['revisionFormulaPDF']}")
                time.sleep(1.0)
            elif result["status"] == "NOK_WRONG_FORMULA":
                    time.sleep(1.0)
                    st.error(f"❌ {result['message']}")            
                    typewriter(text="The price revision formula extracted from the PDF Contract is the following:", speed=10)
                    st.latex(f"{result['pdf']['revisionFormulaPDF']}")
                    typewriter(text="The price revision formula extracted from the ERP is the following:", speed=10)
                    st.latex(f"{result['erp']['revisionFormulaERP']}")
            elif result["status"] == "NOK_DISABLED_FORMULA":
                    time.sleep(1.0)
                    st.error(f"❌ {result['message']}")            
                    typewriter(text="The price revision formula extracted from the PDF Contract is the following:", speed=10)
                    st.latex(f"{result['pdf']['revisionFormulaPDF']}")