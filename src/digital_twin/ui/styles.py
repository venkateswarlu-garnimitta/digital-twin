"""CSS styles for Digital Twin application."""

PROFESSIONAL_STYLES = """
<style>
/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main container */
.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    max-width: 1400px;
}

/* Sidebar styling */
.css-1d391kg {
    background-color: #ffffff;
    border-right: 1px solid #e1e5e9;
}

/* Chat messages */
.stChatMessage {
    margin-bottom: 1.5rem;
}

/* User messages */
.stChatMessage[data-testid="user"] {
    background-color: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 12px;
    padding: 16px 20px;
    margin-left: 15%;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

/* Assistant messages */
.stChatMessage[data-testid="assistant"] {
    background-color: #ffffff;
    border: 1px solid #e9ecef;
    border-radius: 12px;
    padding: 16px 20px;
    margin-right: 15%;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

/* Chat input at bottom */
.stChatInput {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 999;
    background: white;
    border-top: 1px solid #e9ecef;
    padding: 1rem;
}

/* Chat input styling */
.stChatInput > div {
    border-radius: 12px;
    border: 2px solid #e9ecef;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.stChatInput > div:focus-within {
    border-color: #007bff;
    box-shadow: 0 0 0 3px rgba(0,123,255,0.1);
}

/* Main content area - add bottom padding for fixed input */
.main .block-container {
    padding-bottom: 120px !important;
}

/* Buttons */
.stButton > button {
    border-radius: 8px;
    border: 1px solid #e9ecef;
    background-color: #ffffff;
    color: #495057;
    font-weight: 500;
    transition: all 0.2s;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.stButton > button:hover {
    background-color: #f8f9fa;
    border-color: #007bff;
    color: #007bff;
    transform: translateY(-1px);
    box-shadow: 0 2px 6px rgba(0,0,0,0.15);
}

/* Primary button */
.stButton > button[kind="primary"] {
    background-color: #007bff;
    border-color: #007bff;
    color: #ffffff;
    font-weight: 600;
}

.stButton > button[kind="primary"]:hover {
    background-color: #0056b3;
    border-color: #0056b3;
    color: #ffffff;
}

/* Secondary button */
.stButton > button[kind="secondary"] {
    background-color: #6c757d;
    border-color: #6c757d;
    color: #ffffff;
}

.stButton > button[kind="secondary"]:hover {
    background-color: #545b62;
    border-color: #545b62;
    color: #ffffff;
}

/* Selectbox */
.stSelectbox > div > div {
    border-radius: 8px;
    border: 1px solid #e9ecef;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    color: #212529;
    font-weight: 600;
}

.stMarkdown {
    color: #495057;
    line-height: 1.6;
}

/* Loading animation */
.loading-dots {
    display: inline-block;
}

.loading-dots::after {
    content: '';
    animation: dots 1.5s steps(4, end) infinite;
}

@keyframes dots {
    0%, 20% { content: ''; }
    40% { content: '.'; }
    60% { content: '..'; }
    80%, 100% { content: '...'; }
}

/* Status indicators */
.status-online {
    color: #28a745;
    font-weight: 600;
}

.status-ready {
    color: #6c757d;
    font-weight: 500;
}

/* Welcome message styling */
.welcome-container {
    text-align: center;
    padding: 3rem 1rem;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    border-radius: 12px;
    margin: 2rem 0;
}

.welcome-title {
    font-size: 2rem;
    font-weight: 700;
    color: #212529;
    margin-bottom: 1rem;
}

.welcome-subtitle {
    font-size: 1.1rem;
    color: #6c757d;
    margin-bottom: 2rem;
}
</style>
"""

def apply_styles():
    """Apply professional styles to the Streamlit app."""
    import streamlit as st
    st.markdown(PROFESSIONAL_STYLES, unsafe_allow_html=True)
