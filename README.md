# Mistral AI Agent - Streamlit Web Interface

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Ollama](https://img.shields.io/badge/Ollama-Latest-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A professional Streamlit web interface for interacting with Mistral AI models through Ollama.

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Configuration](#configuration)

</div>

## 📋 Overview

A clean, professional Streamlit-based web interface designed for seamless interaction with Mistral AI models via Ollama. This application provides a business-appropriate chat interface with real-time AI communication capabilities.

## ✨ Features

- **🤖 Professional Interface** - Clean, minimalist design suitable for business environments
- **⚡ Real-time Communication** - Instant responses from Mistral AI models
- **🔗 Connection Management** - Built-in Ollama connection testing and status monitoring
- **💬 Session Management** - Maintains conversation history during active sessions
- **🛡️ Robust Error Handling** - Comprehensive error handling with user-friendly messages
- **🎛️ Simple Configuration** - Easy setup and customization options

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running
- Mistral model available in Ollama

### Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
```bash
pip install streamlit requests

# Install Ollama (if not already installed)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the Mistral model
ollama pull mistral

# Start Ollama service
ollama serve

🎮 Usage
#Start the Streamlit application

source .venv/bin/activate 
streamlit run mistral_agent.py

#Access the web interface
http://localhost:8501

⚙️ Configuration

OLLAMA_HOST = "http://localhost:11434"  # Default Ollama port



