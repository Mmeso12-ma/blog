import requests
import streamlit as st

base_url = "http://localhost:8000"

def generate_image(name: str) -> str:
    response = requests.post(f"{base_url}/hello", json={"name": name})
    return response.json()

def main():
    st.title("Making a Blog with Bae")
    prompt = st.text_input("Enter a nice name", placeholder="Mmesoma")
    if st.button("Send Request"):
        with st.spinner("Sending request..."):
            result = generate_image(prompt.title())
            st.success(result["message"])

if __name__ == "__main__":
    main()