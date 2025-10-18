"""UI utilities for session management."""

import streamlit as st


def load_session_messages(session_id):
    """Load messages for a specific session."""
    if 'session_messages' not in st.session_state:
        st.session_state.session_messages = {}
    
    if session_id not in st.session_state.session_messages:
        st.session_state.session_messages[session_id] = []
    
    return st.session_state.session_messages[session_id]


def save_message_to_session(session_id, role, content):
    """Save a message to the current session only when conversation is complete."""
    if 'session_messages' not in st.session_state:
        st.session_state.session_messages = {}
    
    if session_id not in st.session_state.session_messages:
        st.session_state.session_messages[session_id] = []
    
    # Only save assistant messages (which means conversation is complete)
    # User messages are already saved before processing
    if role == "assistant":
        st.session_state.session_messages[session_id].append({
            "role": role,
            "content": content
        })
    elif role == "user":
        # Save user message immediately
        st.session_state.session_messages[session_id].append({
            "role": role,
            "content": content
        })


def initialize_service():
    """Initialize the Digital Twin Service."""
    if 'digital_twin_service' not in st.session_state:
        with st.spinner("Initializing..."):
            from ..core.service import DigitalTwinService
            st.session_state.digital_twin_service = DigitalTwinService()
    return st.session_state.digital_twin_service