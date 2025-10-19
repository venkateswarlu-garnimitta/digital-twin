"""
Styles for Digital Twin Application
"""

def get_custom_css():
    return """
    <style>
    /* THEME VARIABLES */
    :root {
        --bg: #f7f7fb;
        --surface: #ffffff;
        --muted-surface: #fafafa;
        --text: #1f2937;
        --muted-text: #6b7280;
        --primary: #10a37f;
        --primary-600: #0d8f6d;
        --border: #e5e7eb;
        --ring: rgba(16, 163, 127, 0.15);
        --shadow: 0 4px 16px rgba(17, 24, 39, 0.06);
        --shadow-soft: 0 2px 10px rgba(17, 24, 39, 0.05);
        --radius: 12px;
        --radius-lg: 16px;
        --radius-xl: 20px;
    }
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* Main Container */
    .main {
        background-color: var(--bg);
        padding: 0;
    }
    
    /* Sidebar Styles */
    [data-testid="stSidebar"] {
        background-color: var(--surface);
        border-right: 1px solid var(--border);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background-color: #ffffff;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* FIXED TOP HEADER */
    .app-topbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 56px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: var(--surface);
        border-bottom: 1px solid var(--border);
        box-shadow: var(--shadow-soft);
        z-index: 1000;
        padding: 0 20px;
    }
    .app-topbar .brand {
        display: flex;
        align-items: center;
        gap: 10px;
        font-weight: 600;
        color: var(--text);
        letter-spacing: 0.2px;
    }
    .app-topbar .brand .logo {
        width: 28px;
        height: 28px;
        border-radius: 8px;
        display: grid;
        place-items: center;
        background: linear-gradient(135deg, rgba(16,163,127,0.15), rgba(16,163,127,0.05));
        border: 1px solid var(--border);
        color: var(--primary);
        font-size: 16px;
    }
    .app-topbar .meta {
        color: var(--muted-text);
        font-size: 12px;
    }
    
    /* Sidebar Title */
    .sidebar-title {
        font-size: 18px;
        font-weight: 600;
        color: var(--text);
        padding: 16px 16px 8px 16px;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Sidebar Buttons */
    [data-testid="stSidebar"] .stButton > button {
        background-color: transparent;
        color: var(--text);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 8px 12px;
        font-size: 14px;
        font-weight: 500;
        text-align: left;
        transition: transform 0.15s ease, border-color 0.2s, background-color 0.2s;
        width: 100%;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: var(--muted-surface);
        border-color: var(--primary);
        transform: translateY(-1px);
    }
    
    [data-testid="stSidebar"] .stButton > button:active {
        background-color: #ececec;
    }
    
    /* Sidebar Text Input (Search) */
    [data-testid="stSidebar"] .stTextInput > div > div > input {
        background-color: #f7f7f8;
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 10px 14px;
        font-size: 14px;
        color: var(--text);
    }
    
    [data-testid="stSidebar"] .stTextInput > div > div > input:focus {
        border-color: #10a37f;
        background-color: #ffffff;
    }
    
    /* Dropdown Styles */
    .stSelectbox {
        margin: 8px 8px;
    }
    
    .stSelectbox > div > div {
        background-color: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        font-size: 14px;
        color: var(--text);
    }
    
    /* Chat History Section */
    .chat-history-title {
        font-size: 12px;
        font-weight: 700;
        color: var(--muted-text);
        text-transform: uppercase;
        padding: 16px 16px 8px 16px;
        letter-spacing: 0.5px;
    }
    
    .chat-history-item {
        padding: 12px 16px;
        margin: 4px 8px;
        border-radius: 8px;
        cursor: pointer;
        color: #202123;
        font-size: 14px;
        transition: background-color 0.2s;
    }
    
    .chat-history-item:hover {
        background-color: #f7f7f8;
    }
    
    /* Chat Container */
    .chat-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 16px 20px 0 20px;
    }

    /* Cards */
    .card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow);
    }
    .chat-card {
        padding: 16px 16px 0 16px;
    }
    .search-card { padding: 24px; }
    
    /* Center Container for New Chat */
    .center-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        min-height: 20vh;
        padding: 20px;
        padding-top: 15vh;
    }
    
    .welcome-title {
        font-size: 32px;
        font-weight: 700;
        color: var(--text);
        margin-top: 80px;
        margin-bottom: 8px;
        text-align: center;
    }
    .welcome-subtitle { color: var(--muted-text); font-size: 16px; }
    


    /* Chat Message Styles */
    .chat-row { display: flex; gap: 10px; margin-bottom: 14px; align-items: flex-end; }
    .chat-row-user { justify-content: flex-end; }
    .chat-row-assistant { justify-content: flex-start; }

    .chat-avatar {
        flex: 0 0 32px;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        background: linear-gradient(135deg, rgba(16,163,127,0.15), rgba(16,163,127,0.03));
        color: var(--primary);
        border: 1px solid var(--border);
        font-size: 16px;
    }

    .chat-message {
        padding: 14px 16px;
        border-radius: 18px;
        max-width: 72%;
        word-wrap: break-word;
        box-shadow: var(--shadow-soft);
        animation: fadeInUp 240ms ease-out;
    }
    
    .chat-message.user {
        margin-left: auto;
        background: linear-gradient(160deg, rgba(16,163,127,0.15), rgba(16,163,127,0.06));
        border: 1px solid rgba(16,163,127,0.25);
        color: var(--text);
        backdrop-filter: saturate(1.2);
    }

    .chat-message.assistant {
        background-color: var(--surface);
        border: 1px solid var(--border);
        margin-right: auto;
        color: var(--text);
    }
    
    .message-content {
        color: var(--text);
        font-size: 15px;
        line-height: 1.6;
        white-space: pre-wrap;
        word-break: break-word;
    }

    .message-meta { margin-top: 6px; font-size: 11px; color: var(--muted-text); }
    
    /* Enhanced markdown formatting for assistant responses */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: var(--text);
        font-weight: 600;
        margin-top: 1.2em;
        margin-bottom: 0.6em;
    }
    
    .stMarkdown h1 {
        font-size: 24px;
        border-bottom: 2px solid #e5e5e5;
        padding-bottom: 13px;
    }
    
    .stMarkdown h2 {
        font-size: 20px;
    }
    
    .stMarkdown h3 {
        font-size: 18px;
    }
    
    .stMarkdown ul, .stMarkdown ol {
        padding-left: 24px;
        margin-top: 8px;
        margin-bottom: 8px;
    }
    
    .stMarkdown li {
        margin-bottom: 6px;
        line-height: 1.6;
    }
    
    .stMarkdown p {
        margin-bottom: 12px;
        line-height: 1.6;
    }
    
    .stMarkdown strong {
        font-weight: 600;
        color: #202123;
    }
    
    .stMarkdown code {
        background-color: #f1f3f4;
        padding: 2px 6px;
        border-radius: 4px;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        color: #d73a49;
    }
    
    .stMarkdown a {
        color: var(--primary);
        text-decoration: none;
        font-weight: 500;
    }
    
    .stMarkdown a:hover {
        text-decoration: underline;
    }
    
    /* CRITICAL: Fixed Chat Input Container */
    [data-testid="stChatInputContainer"] {
        position: fixed !important;
        bottom: 0 !important;
        left: 0 !important;
        right: 0 !important;
        background-color: var(--surface) !important;
        border-top: 1px solid var(--border) !important;
        padding: 16px 0 !important;
        z-index: 999 !important;
        box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05) !important;
        width: 100% !important;
    }
    
    /* Center the input within fixed container - consistent width */
    [data-testid="stChatInputContainer"] > div {
        max-width: 900px !important;
        width: 900px !important;
        margin: 0 auto !important;
        padding: 0 20px !important;
    }
    
    /* Chat Input Styling */
    .stChatInput {
        background-color: transparent !important;
    }
    
    .stChatInput > div {
        background-color: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-lg) !important;
        padding: 4px !important;
        box-shadow: var(--shadow-soft) !important;
    }
    
    .stChatInput textarea {
        background-color: var(--surface) !important;
        border: none !important;
        padding: 12px 16px !important;
        font-size: 15px !important;
        color: var(--text) !important;
        min-height: 24px !important;
        max-height: 200px !important;
    }
    
    .stChatInput textarea:focus {
        outline: none !important;
        box-shadow: none !important;
    }
    
    .stChatInput > div:focus-within {
        border-color: var(--primary) !important;
        box-shadow: 0 2px 12px var(--ring) !important;
    }
    
    /* Text Input Styling (for other inputs) */
    .stTextInput > div > div > input {
        background-color: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 12px 16px;
        font-size: 15px;
        color: var(--text);
        box-shadow: var(--shadow-soft);
        transition: all 0.2s;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--primary);
        box-shadow: 0 2px 12px var(--ring);
        outline: none;
    }
    
    /* Main Button Styles */
    .main .stButton > button {
        background-color: var(--primary);
        color: #ffffff;
        border: none;
        border-radius: var(--radius);
        padding: 10px 20px;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    
    .main .stButton > button:hover { background-color: var(--primary-600); }
    
    /* Scrollbar Styles */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #ffffff;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #d1d5db;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #9ca3af;
    }
    
    /* Remove/Adjust Streamlit padding */
    .block-container {
        padding-top: 5.5rem; /* room for fixed header */
        padding-bottom: 120px !important; /* Space for fixed input */
    }
    
    /* Divider */
    .sidebar-divider { border-top: 1px solid var(--border); margin: 16px 0; }
    
    /* Search Modal Input Styling - Match chat input exactly */
    [data-testid="stVerticalBlock"] > div:has(input[placeholder="Type to search your chat history..."]) .stTextInput {
        background-color: transparent !important;
    }
    
    [data-testid="stVerticalBlock"] > div:has(input[placeholder="Type to search your chat history..."]) .stTextInput > div {
        background-color: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-lg) !important;
        padding: 4px !important;
        box-shadow: var(--shadow-soft) !important;
    }
    
    [data-testid="stVerticalBlock"] > div:has(input[placeholder="Type to search your chat history..."]) .stTextInput > div > div > input {
        background-color: var(--surface) !important;
        border: none !important;
        padding: 12px 16px !important;
        font-size: 15px !important;
        color: var(--text) !important;
        min-height: 24px !important;
        max-height: 200px !important;
        text-align: left !important;
    }
    
    [data-testid="stVerticalBlock"] > div:has(input[placeholder="Type to search your chat history..."]) .stTextInput > div > div > input:focus {
        outline: none !important;
        box-shadow: none !important;
    }
    
    [data-testid="stVerticalBlock"] > div:has(input[placeholder="Type to search your chat history..."]) .stTextInput > div:focus-within {
        border-color: var(--primary) !important;
        box-shadow: 0 2px 12px var(--ring) !important;
    }
    
    /* Left align placeholder text */
    [data-testid="stVerticalBlock"] > div:has(input[placeholder="Type to search your chat history..."]) .stTextInput > div > div > input::placeholder {
        text-align: left !important;
    }
    
    /* Chat history items hover effect */
    .chat-history-item:hover {
        background-color: var(--muted-surface) !important;
        transform: translateY(-1px) !important;
        box-shadow: var(--shadow) !important;
    }
    
    /* Back button styling - reduce padding and width */
    button[key="back"] {
        padding: 6px 12px !important;
        width: auto !important;
        min-width: auto !important;
        max-width: 120px !important;
    }
    
    /* Style chat history buttons to look like simple text */
    button[key^="search_chat_"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 8px 0 !important;
        margin: 2px 0 !important;
        text-align: left !important;
        color: var(--text) !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        width: auto !important;
        min-width: auto !important;
        max-width: none !important;
    }
    
    button[key^="search_chat_"]:hover { background-color: var(--muted-surface) !important; border-radius: 6px !important; }
    
    /* Style error messages to match search bar message */
    .stAlert {
        background-color: var(--muted-surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        color: var(--muted-text) !important;
        font-size: 12px !important;
        padding: 8px 12px !important;
        margin: 0 auto !important;
        width: fit-content !important;
    }
    
    /* Search Modal Close Button */
    button[kind="secondary"]:has-text("✕") {
        background-color: transparent !important;
        border: none !important;
        color: #8e8ea0 !important;
        font-size: 20px !important;
        padding: 4px 8px !important;
    }
    
    /* Style sidebar buttons - more specific targeting */
    [data-testid="stSidebar"] .stButton > button[kind="secondary"] {
        font-size: 14px !important;
        text-align: left !important;
        padding: 8px 16px !important;
        justify-content: flex-start !important;
        display: flex !important;
        align-items: center !important;
    }
    
    /* Target specific buttons by key */
    [data-testid="stSidebar"] button[key="new_chat_button_2024"] {
        font-size: 14px !important;
        text-align: left !important;
        padding: 8px 16px !important;
        justify-content: flex-start !important;
    }
    
    [data-testid="stSidebar"] button[key="search_btn"] {
        font-size: 14px !important;
        text-align: left !important;
        padding: 8px 16px !important;
        justify-content: flex-start !important;
    }

    /* SEARCH RESULT CARDS */
    .search-result-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 12px 14px;
        margin-bottom: 10px;
        transition: transform 0.15s ease, box-shadow 0.2s ease;
        box-shadow: var(--shadow-soft);
    }
    .search-result-card:hover { transform: translateY(-1px); box-shadow: var(--shadow); }

    /* ANIMATIONS */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(4px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* RESPONSIVE */
    @media (max-width: 992px) {
        [data-testid="stChatInputContainer"] > div { max-width: 720px !important; width: 100% !important; }
        .chat-container { max-width: 720px; }
        .chat-message { max-width: 78%; }
    }
    @media (max-width: 768px) {
        .app-topbar { height: 52px; }
        .block-container { padding-top: 4.5rem; }
        [data-testid="stChatInputContainer"] > div { max-width: 100% !important; padding: 0 12px !important; }
        .chat-container { padding: 12px; }
        .chat-message { max-width: 86%; }
    }
    
    </style>
    """


    # Note: Dark theme helper removed per revert request.
