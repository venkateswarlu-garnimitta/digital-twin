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
    padding-bottom: 140px;
    max-width: 900px;
    margin: 0 auto;
}

/* Sidebar styling */
.css-1d391kg {
    background-color: #fafbfc;
    border-right: 1px solid #e8eaed;
}

/* Chat messages */
.stChatMessage {
    margin-bottom: 1.5rem;
    width: 100%;
    clear: both;
}

/* User messages - RIGHT SIDE like ChatGPT */
.stChatMessage[data-testid="user"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 18px 18px 4px 18px;
    padding: 12px 16px;
    margin-left: 30%;
    margin-right: 0;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.15);
    border: none;
    max-width: 70%;
    float: right;
    clear: both;
}

/* Assistant messages - LEFT SIDE like ChatGPT */
.stChatMessage[data-testid="assistant"] {
    background-color: #ffffff;
    border: 1px solid #e8eaed;
    border-radius: 18px 18px 18px 4px;
    padding: 12px 16px;
    margin-right: 30%;
    margin-left: 0;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    max-width: 70%;
    float: left;
    clear: both;
}

/* Chat input - fixed at bottom with proper sizing */
.stChatInput {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 999;
    background: white;
    border-top: 1px solid #e8eaed;
    padding: 16px 20px;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
}

/* Chat input styling - smaller and better aligned */
.stChatInput > div {
    border-radius: 24px;
    border: 1px solid #e8eaed;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    max-width: 800px;
    margin: 0 auto;
}

.stChatInput > div:focus-within {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

/* Buttons */
.stButton > button {
    border-radius: 8px;
    border: 1px solid #e8eaed;
    background-color: #ffffff;
    color: #5f6368;
    font-weight: 500;
    transition: all 0.2s ease;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.stButton > button:hover {
    background-color: #f8f9fa;
    border-color: #667eea;
    color: #667eea;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Primary button */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    color: #ffffff;
    font-weight: 600;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
    color: #ffffff;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

/* Secondary button */
.stButton > button[kind="secondary"] {
    background-color: #f1f3f4;
    border-color: #dadce0;
    color: #5f6368;
}

.stButton > button[kind="secondary"]:hover {
    background-color: #e8eaed;
    border-color: #dadce0;
    color: #3c4043;
}

/* Selectbox */
.stSelectbox > div > div {
    border-radius: 8px;
    border: 1px solid #e8eaed;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    background-color: #ffffff;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    color: #202124;
    font-weight: 600;
}

.stMarkdown {
    color: #3c4043;
    line-height: 1.6;
}

/* Loading animation */
.loading-dots {
    display: inline-block;
    color: #667eea;
    font-weight: 500;
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

/* AWS Services Banner */
.aws-services-banner {
    background: linear-gradient(135deg, #ff9900 0%, #ff6600 100%);
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
    margin-bottom: 1rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(255, 153, 0, 0.3);
}

.aws-services-banner h4 {
    color: white;
    margin: 0;
    font-size: 1rem;
    font-weight: 600;
}

.aws-services-banner p {
    color: white;
    margin: 4px 0 0 0;
    font-size: 0.85rem;
    opacity: 0.9;
}

/* Company cards styling */
.company-cards-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    padding: 2rem 0;
}

.company-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 1px solid #e8eaed;
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.company-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    border-color: #667eea;
}

.company-card h3 {
    color: #202124;
    font-size: 1.4rem;
    font-weight: 600;
    margin-bottom: 8px;
}

.company-card p {
    color: #5f6368;
    font-size: 0.95rem;
    margin-bottom: 16px;
    line-height: 1.5;
}

.company-card .company-icon {
    font-size: 2.5rem;
    margin-bottom: 16px;
    opacity: 0.8;
}

/* Home screen styling */
.home-container {
    text-align: center;
    padding: 2rem 1rem;
}

.home-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #202124;
    margin-bottom: 1rem;
}

.home-subtitle {
    font-size: 1.2rem;
    color: #5f6368;
    margin-bottom: 3rem;
    font-weight: 400;
}

/* Info card for selection */
.info-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    padding: 3rem 2rem;
    border-radius: 16px;
    margin: 2rem 0;
    border: 1px solid #e8eaed;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.info-card h3 {
    color: #202124;
    margin-bottom: 1.5rem;
    font-size: 1.8rem;
    font-weight: 700;
}

.info-card p {
    color: #5f6368;
    margin-bottom: 0.8rem;
    font-size: 1rem;
    line-height: 1.6;
}

.info-card .aws-services {
    background: linear-gradient(135deg, #ff9900 0%, #ff6600 100%);
    color: white;
    padding: 1rem;
    border-radius: 8px;
    margin: 1.5rem 0;
}

.info-card .aws-services h4 {
    color: white;
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
}

.info-card .aws-services p {
    color: white;
    margin: 0.3rem 0;
    font-size: 0.9rem;
    opacity: 0.9;
}

/* Get Started Button */
.get-started-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 16px 32px;
    border-radius: 12px;
    border: none;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    margin-top: 2rem;
}

.get-started-btn:hover {
    background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(102, 126, 234, 0.4);
}

/* Sidebar info styling */
.sidebar-info {
    background: linear-gradient(135deg, #f8f9fa 0%, #e8f0fe 100%);
    padding: 16px;
    border-radius: 8px;
    margin-bottom: 1rem;
    border: 1px solid #e8eaed;
}

.sidebar-info h4 {
    color: #202124;
    margin: 0 0 8px 0;
    font-size: 1rem;
}

.sidebar-info p {
    color: #5f6368;
    margin: 4px 0;
    font-size: 0.9rem;
}

/* Selection interface */
.selection-container {
    background: linear-gradient(135deg, #f8f9fa 0%, #e8f0fe 100%);
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1rem 0;
    border: 1px solid #e8eaed;
}

.selection-row {
    display: flex;
    gap: 20px;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
}

.selection-item {
    flex: 1;
    min-width: 200px;
}

/* Chat header styling */
.chat-header {
    background: linear-gradient(135deg, #f8f9fa 0%, #e8f0fe 100%);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 2rem;
    border: 1px solid #e8eaed;
}

.chat-header h2 {
    color: #202124;
    margin-bottom: 4px;
}

.chat-header p {
    color: #5f6368;
    margin: 0;
    font-size: 0.95rem;
}

/* Status panel improvements */
.status-panel {
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    padding: 16px;
    border-radius: 8px;
    border: 1px solid #e8eaed;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

/* Message count styling */
.message-count {
    color: #667eea;
    font-weight: 600;
    font-size: 1.2rem;
}

/* Session info styling */
.session-info {
    color: #5f6368;
    font-size: 0.85rem;
    font-style: italic;
    margin-top: 8px;
}

/* Sidebar improvements */
.css-1d391kg .stMarkdown h3 {
    color: #202124;
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

/* Remove empty space issues */
.stChatMessage > div {
    padding: 0;
    margin: 0;
}

/* Fix text alignment in messages */
.stChatMessage .stMarkdown {
    margin: 0;
    padding: 0;
}

/* Chat container improvements */
.chat-container {
    min-height: 400px;
    padding-bottom: 20px;
}

/* Industry icons */
.industry-icon {
    font-size: 1.2rem;
    margin-right: 6px;
}
</style>
"""

def apply_styles():
    """Apply professional styles to the Streamlit app."""
    import streamlit as st
    st.markdown(PROFESSIONAL_STYLES, unsafe_allow_html=True)