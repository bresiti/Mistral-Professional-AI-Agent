import streamlit as st
import requests
import json

# Page configuration
st.set_page_config(
    page_title="Mistral AI Agent",
    page_icon="🤖",
    layout="centered"
)

OLLAMA_HOST = "http://192.168.1.253:11434"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "processing" not in st.session_state:
    st.session_state.processing = False

# Header
st.title("🤖 Mistral Professional AI Agent")
st.markdown("---")

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.container():
            st.markdown(f"**You:** {message['content']}")
    else:
        with st.container():
            st.markdown(f"**Agent:** {message['content']}")
    st.markdown("---")

# Processing indicator
if st.session_state.processing:
    with st.container():
        st.info("🔄 Agent is processing your request...")

# Chat input
if prompt := st.chat_input("Enter your message:"):
    if prompt.strip():
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt.strip()})
        st.session_state.processing = True
        st.rerun()

# Process request
if st.session_state.processing and st.session_state.messages:
    last_message = st.session_state.messages[-1]
    
    if last_message["role"] == "user":
        try:
            with st.spinner("Analyzing request..."):
                response = requests.post(
                    f"{OLLAMA_HOST}/api/generate",
                    json={
                        "model": "mistral",
                        "prompt": f"""You are a professional AI agent. Provide clear, concise, and helpful responses.

User: {last_message['content']}

Agent:""",
                        "stream": False,
                        "options": {
                            "temperature": 0.7,
                            "top_p": 0.9,
                            "num_predict": 500
                        }
                    },
                    timeout=120
                )
                
            if response.status_code == 200:
                result = response.json()
                agent_response = result.get("response", "I apologize, but I encountered an issue processing your request.")
                
                # Ensure professional formatting
                if not agent_response.strip():
                    agent_response = "Thank you for your message. How may I assist you further?"
                    
            else:
                agent_response = f"⚠️ Service temporarily unavailable. Please ensure Ollama is running with the Mistral model loaded. (Error: {response.status_code})"
                
        except requests.exceptions.ConnectionError:
            agent_response = "🔌 Connection error: Unable to reach AI service. Please verify Ollama is running on the specified host and port."
        except requests.exceptions.Timeout:
            agent_response = "⏱️ Request timeout: The service is taking longer than expected to respond. Please try again."
        except Exception as e:
            agent_response = f"❌ Unexpected error: {str(e)}. Please check your configuration."
        
        # Add agent response
        st.session_state.messages.append({"role": "assistant", "content": agent_response})
        st.session_state.processing = False
        st.rerun()

# Sidebar info
with st.sidebar:
    st.header("System Status")
    
    # Test connection
    if st.button("Check Connection"):
        try:
            test_response = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=5)
            if test_response.status_code == 200:
                st.success("✅ Connected to Ollama")
            else:
                st.error("❌ Connection failed")
        except:
            st.error("❌ Cannot reach Ollama")
    
    st.markdown("---")
    st.header("Agent Capabilities")
    st.write("• Professional communication")
    st.write("• Problem analysis")
    st.write("• Information processing")
    st.write("• Real-time responses")
    
    st.markdown("---")
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.session_state.processing = False
        st.rerun()

# Footer
st.markdown("---")
st.caption("Mistral Professional AI Agent | Secure Connection | Real-time Processing")