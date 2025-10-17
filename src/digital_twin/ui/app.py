"""Streamlit application for Digital Twin."""

import streamlit as st
from .utils import initialize_service, load_session_messages, save_message_to_session
from .styles import apply_styles


def main():
    """Main application."""
    st.set_page_config(
        page_title="Digital Twin",
        page_icon="",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply professional styles
    apply_styles()
    
    # Initialize service
    service = initialize_service()
    
    # Initialize session state
    if 'current_session_id' not in st.session_state:
        st.session_state.current_session_id = None
    if 'selected_company_key' not in st.session_state:
        st.session_state.selected_company_key = 'techcorp'
    if 'session_messages' not in st.session_state:
        st.session_state.session_messages = {}
    
    # Sidebar
    with st.sidebar:
        st.markdown("# Digital Twin")
        
        # New Chat button
        if st.button("New Chat", type="primary", use_container_width=True):
            # Create new session with current company
            session_result = service.create_new_session(
                st.session_state.selected_company_key
            )
            if session_result['success']:
                st.session_state.current_session_id = session_result['session_id']
                # Initialize empty messages for new session
                st.session_state.session_messages[st.session_state.current_session_id] = []
                st.rerun()
        
        st.divider()
        
        # Company Selection
        st.markdown("### Company")
        companies = service.get_available_companies()
        company_options = {f"{c['name']}": c['key'] for c in companies}
        
        # Get current company name
        current_company_name = next(
            (name for name, key in company_options.items() if key == st.session_state.selected_company_key),
            list(company_options.keys())[0]
        )
        
        selected_company = st.selectbox(
            "Select company:",
            options=list(company_options.keys()),
            index=list(company_options.keys()).index(current_company_name),
            label_visibility="collapsed"
        )
        
        selected_company_key = company_options[selected_company]
        
        # Handle company change
        if selected_company_key != st.session_state.selected_company_key:
            st.session_state.selected_company_key = selected_company_key
            
            # If no current session, create one
            if not st.session_state.current_session_id:
                session_result = service.create_new_session(selected_company_key)
                if session_result['success']:
                    st.session_state.current_session_id = session_result['session_id']
                    st.session_state.session_messages[st.session_state.current_session_id] = []
            else:
                # Continue with existing session but clear messages for new company context
                if st.session_state.current_session_id in st.session_state.session_messages:
                    st.session_state.session_messages[st.session_state.current_session_id] = []
        
        st.divider()
        
        # Chat History
        st.markdown("### Recent Chats")
        sessions_result = service.list_user_sessions(limit=10)
        
        if sessions_result['success'] and sessions_result['sessions']:
            for session in sessions_result['sessions']:
                # Create session item with proper styling
                col1, col2 = st.columns([5, 1])
                
                with col1:
                    session_title = f"{session['session_title'][:25]}{'...' if len(session['session_title']) > 25 else ''}"
                    if st.button(
                        session_title,
                        key=f"session_btn_{session['session_id']}",
                        help=f"{session['company_name']} • {session['created_at_formatted']}",
                        use_container_width=True
                    ):
                        # Switch to this session
                        switch_result = service.switch_to_session(session['session_id'])
                        if switch_result['success']:
                            st.session_state.current_session_id = session['session_id']
                            st.session_state.selected_company_key = session['company_key']
                            # Load messages for this session (they should already be loaded)
                            if st.session_state.current_session_id not in st.session_state.session_messages:
                                st.session_state.session_messages[st.session_state.current_session_id] = []
                            st.rerun()
                
                with col2:
                    if st.button("×", key=f"delete_btn_{session['session_id']}", help="Delete chat", type="secondary"):
                        delete_result = service.delete_session(session['session_id'])
                        if delete_result['success']:
                            # Remove from local session messages
                            if session['session_id'] in st.session_state.session_messages:
                                del st.session_state.session_messages[session['session_id']]
                            
                            if st.session_state.current_session_id == session['session_id']:
                                st.session_state.current_session_id = None
                                st.session_state.session_messages = {}
                            st.rerun()
        else:
            st.markdown("*No recent chats*")
    
    # Main chat interface
    col1, col2 = st.columns([6, 1])
    
    with col1:
        # Chat header with company info
        current_company_name = next(
            (c['name'] for c in companies if c['key'] == st.session_state.selected_company_key),
            'TechCorp'
        )
        current_company_desc = next(
            (c['description'] for c in companies if c['key'] == st.session_state.selected_company_key),
            'Technology company'
        )
        
        st.markdown(f"## {current_company_name}")
        st.markdown(f"*{current_company_desc}*")
        
        # Display chat messages for current session
        if st.session_state.current_session_id:
            messages = load_session_messages(st.session_state.current_session_id)
            
            # Display all messages in the current session
            for message in messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            # Chat input
            if prompt := st.chat_input(f"Ask about {current_company_name}..."):
                # Add user message to current session
                save_message_to_session(st.session_state.current_session_id, "user", prompt)
                
                with st.chat_message("user"):
                    st.markdown(prompt)
                
                # Generate response
                with st.chat_message("assistant"):
                    # Create loading placeholder
                    loading_placeholder = st.empty()
                    
                    try:
                        # Show loading animation
                        loading_placeholder.markdown('<span class="loading-dots">Thinking</span>', unsafe_allow_html=True)
                        
                        # Process query
                        response = service.process_query(
                            company_key=st.session_state.selected_company_key,
                            user_query=prompt,
                            session_id=st.session_state.current_session_id
                        )
                        
                        # Clear loading and show response
                        loading_placeholder.empty()
                        
                        if response.get('success') or 'response' in response:
                            assistant_response = response.get('response', response.get('error', 'No response'))
                            st.markdown(assistant_response)
                            # Save assistant message to current session
                            save_message_to_session(st.session_state.current_session_id, "assistant", assistant_response)
                        else:
                            error_msg = response.get('error', 'An error occurred')
                            st.error(error_msg)
                            save_message_to_session(st.session_state.current_session_id, "assistant", f"Error: {error_msg}")
                    
                    except Exception as e:
                        loading_placeholder.empty()
                        error_msg = "Sorry, something went wrong. Please try again."
                        st.error(error_msg)
                        save_message_to_session(st.session_state.current_session_id, "assistant", error_msg)
        else:
            # Welcome screen - no pre-populated queries
            st.markdown("""
            <div class="welcome-container">
                <div class="welcome-title">Welcome to Digital Twin</div>
                <div class="welcome-subtitle">Start a conversation with {}</div>
            </div>
            """.format(current_company_name), unsafe_allow_html=True)
    
    with col2:
        # Status panel
        if st.session_state.current_session_id:
            messages = load_session_messages(st.session_state.current_session_id)
            st.markdown("**Messages**")
            st.markdown(f"**{len(messages)}**")
            
            st.markdown("**Status**")
            st.markdown('<span class="status-online">● Online</span>', unsafe_allow_html=True)
            
            # Session info
            session_info = service.get_session_history(st.session_state.current_session_id)
            if session_info['success']:
                st.markdown("**Session**")
                st.markdown(f"*{session_info['session_title'][:20]}...*")
        else:
            st.markdown("**Status**")
            st.markdown('<span class="status-ready">● Ready</span>', unsafe_allow_html=True)
            
            st.markdown("**Next Step**")
            st.markdown("Start a new chat")


if __name__ == "__main__":
    main()