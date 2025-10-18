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
    if 'app_started' not in st.session_state:
        st.session_state.app_started = False
    if 'current_session_id' not in st.session_state:
        st.session_state.current_session_id = None
    if 'selected_industry' not in st.session_state:
        st.session_state.selected_industry = None
    if 'selected_company_key' not in st.session_state:
        st.session_state.selected_company_key = None
    if 'session_messages' not in st.session_state:
        st.session_state.session_messages = {}
    if 'show_chat' not in st.session_state:
        st.session_state.show_chat = False
    
    # Show welcome screen if app not started
    if not st.session_state.app_started:
        st.markdown("""
        <div class="home-container">
            <div class="home-title">Welcome to Digital Twin</div>
            <div class="home-subtitle">Experience AI-powered customer service with intelligent digital representatives</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h3>🚀 AWS-Powered Digital Twin</h3>
            <p>Experience the future of customer service with AI-powered digital representatives</p>
            
            <div class="aws-services">
                <h4>Powered by AWS Services</h4>
                <p>• <strong>AWS Bedrock Knowledge Base</strong> - Advanced AI knowledge retrieval</p>
                <p>• <strong>Strands Agents</strong> - Intelligent conversation management</p>
                <p>• <strong>Claude-3-Sonnet</strong> - State-of-the-art language model</p>
                <p>• <strong>Real-time Processing</strong> - Instant responses and insights</p>
            </div>
            
            <p><strong>Ready to get started?</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Get Started Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Get Started", type="primary", use_container_width=True):
                st.session_state.app_started = True
                st.rerun()
        
        return
    
    # Main app interface
    # Sidebar
    with st.sidebar:
        st.markdown("# Digital Twin")
        
        # AWS Services Banner
        st.markdown("""
        <div class="aws-services-banner">
            <h4>🚀 Powered by AWS</h4>
            <p>Bedrock • Knowledge Base • Strands Agents</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Current Selection Info
        if st.session_state.selected_industry and st.session_state.selected_company_key:
            companies = service.get_available_companies()
            current_company = next(
                (c for c in companies if c['key'] == st.session_state.selected_company_key),
                None
            )
            
            if current_company:
                st.markdown(f"""
                <div class="sidebar-info">
                    <h4>Current Selection</h4>
                    <p><strong>Industry:</strong> {st.session_state.selected_industry}</p>
                    <p><strong>Company:</strong> {current_company['name']}</p>
                    <p><strong>Description:</strong> {current_company['description']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # New Chat button (only show when in chat)
        if st.session_state.show_chat:
            if st.button("New Chat", type="primary", use_container_width=True):
                # Create new session with current company
                session_result = service.create_new_session(
                    st.session_state.selected_company_key
                )
                if session_result['success']:
                    st.session_state.current_session_id = session_result['session_id']
                    st.session_state.session_messages[st.session_state.current_session_id] = []
                    st.rerun()
        
        # Back to selection button
        if st.session_state.show_chat:
            if st.button("← Back to Selection", use_container_width=True):
                st.session_state.show_chat = False
                st.session_state.current_session_id = None
                st.session_state.session_messages = {}
                st.rerun()
        
        st.divider()
        
        # Industry Selection
        st.markdown("### Industry")
        industries = service.get_industries()
        industry_icons = {
            'IT': '💻',
            'E-commerce': '🛒'
        }
        
        industry_options = [f"{industry_icons.get(ind, '🏢')} {ind}" for ind in industries]
        
        # Set default based on current selection or first option
        default_industry_index = 0
        if st.session_state.selected_industry:
            try:
                default_industry_index = industry_options.index(f"{industry_icons.get(st.session_state.selected_industry, '🏢')} {st.session_state.selected_industry}")
            except ValueError:
                default_industry_index = 0
        
        selected_industry_display = st.selectbox(
            "Select Industry:",
            options=industry_options,
            index=default_industry_index,
            label_visibility="collapsed"
        )
        
        # Extract industry name from display
        selected_industry = selected_industry_display.split(' ', 1)[1] if ' ' in selected_industry_display else selected_industry_display
        
        # Handle industry change - continue same session
        if selected_industry != st.session_state.selected_industry:
            st.session_state.selected_industry = selected_industry
            st.rerun()
        
        # Company Selection
        st.markdown("### Company")
        companies = service.get_companies_by_industry(st.session_state.selected_industry)
        company_options = [f"{c['name']}" for c in companies]
        
        # Set default based on current selection or first option
        default_company_index = 0
        if st.session_state.selected_company_key:
            try:
                current_company_name = next((c['name'] for c in companies if c['key'] == st.session_state.selected_company_key), None)
                if current_company_name:
                    default_company_index = company_options.index(current_company_name)
            except ValueError:
                default_company_index = 0
        
        selected_company = st.selectbox(
            "Select Company:",
            options=company_options,
            index=default_company_index,
            label_visibility="collapsed"
        )
        
        # Find company key
        selected_company_key = next((c['key'] for c in companies if c['name'] == selected_company), None)
        
        # Handle company change - continue same session
        if selected_company_key != st.session_state.selected_company_key:
            st.session_state.selected_company_key = selected_company_key
            st.rerun()
        
        st.divider()
        
        # Chat History (only show when we have sessions)
        if st.session_state.selected_company_key:
            st.markdown("### Recent Chats")
            sessions_result = service.list_user_sessions(limit=10)
            
            if sessions_result['success'] and sessions_result['sessions']:
                # Filter sessions for current company
                company_sessions = []
                seen_titles = set()
                
                for session in sessions_result['sessions']:
                    if session['company_key'] == st.session_state.selected_company_key:
                        # Avoid duplicate titles by adding timestamp
                        session_title = session['session_title']
                        if session_title in seen_titles:
                            session_title = f"{session_title} ({session['created_at_formatted']})"
                        seen_titles.add(session['session_title'])
                        
                        company_sessions.append({
                            'session': session,
                            'display_title': session_title
                        })
                
                if company_sessions:
                    for item in company_sessions[:5]:  # Show max 5 sessions
                        session = item['session']
                        display_title = item['display_title']
                        
                        col1, col2 = st.columns([4, 1])
                        
                        with col1:
                            if st.button(
                                display_title[:25] + "..." if len(display_title) > 25 else display_title,
                                key=f"session_btn_{session['session_id']}",
                                help=f"{session['company_name']} • {session['created_at_formatted']}",
                                use_container_width=True
                            ):
                                # Switch to this session and prepopulate
                                switch_result = service.switch_to_session(session['session_id'])
                                if switch_result['success']:
                                    st.session_state.current_session_id = session['session_id']
                                    # Load existing messages for this session
                                    if st.session_state.current_session_id not in st.session_state.session_messages:
                                        st.session_state.session_messages[st.session_state.current_session_id] = []
                                    st.session_state.show_chat = True
                                    st.rerun()
                        
                        with col2:
                            if st.button("×", key=f"delete_btn_{session['session_id']}", help="Delete chat", type="secondary"):
                                delete_result = service.delete_session(session['session_id'])
                                if delete_result['success']:
                                    if session['session_id'] in st.session_state.session_messages:
                                        del st.session_state.session_messages[session['session_id']]
                                    
                                    if st.session_state.current_session_id == session['session_id']:
                                        st.session_state.current_session_id = None
                                        st.session_state.session_messages = {}
                                        st.session_state.show_chat = False
                                    st.rerun()
                else:
                    st.markdown("*No recent chats*")
            else:
                st.markdown("*No recent chats*")
    
    # Main content area
    # Show selection interface when both industry and company are selected
    if st.session_state.selected_industry and st.session_state.selected_company_key and not st.session_state.show_chat:
        # Get company info
        companies = service.get_available_companies()
        current_company = next(
            (c for c in companies if c['key'] == st.session_state.selected_company_key),
            None
        )
        
        if current_company:
            # Simple selection header
            st.markdown(f"### 🚀 Ready to chat with {current_company['name']}")
            st.markdown(f"**{current_company['description']}** • {current_company['industry']} Industry")
            
            # Start Chat Button
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("Start Chat", type="primary", use_container_width=True):
                    # Create new session
                    session_result = service.create_new_session(st.session_state.selected_company_key)
                    if session_result['success']:
                        st.session_state.current_session_id = session_result['session_id']
                        st.session_state.session_messages[st.session_state.current_session_id] = []
                        st.session_state.show_chat = True
                        st.rerun()
    
    # Show chat interface when chat is active
    elif st.session_state.show_chat and st.session_state.selected_company_key and st.session_state.current_session_id:
        # Get company info
        companies = service.get_available_companies()
        current_company = next(
            (c for c in companies if c['key'] == st.session_state.selected_company_key),
            None
        )
        
        if current_company:
            # Simple chat header
            st.markdown(f"### 💬 Chat with {current_company['name']}")
            
            # Chat messages
            messages = load_session_messages(st.session_state.current_session_id)
            
            st.markdown('<div class="chat-container">', unsafe_allow_html=True)
            
            # Display all messages in the current session
            for message in messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Chat input
            if prompt := st.chat_input(f"Ask about {current_company['name']}..."):
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
                            
                            # Save assistant message to history
                            save_message_to_session(st.session_state.current_session_id, "assistant", assistant_response)
                        else:
                            error_msg = response.get('error', 'An error occurred')
                            st.error(error_msg)
                    
                    except Exception as e:
                        loading_placeholder.empty()
                        error_msg = "Sorry, something went wrong. Please try again."
                        st.error(error_msg)
    
    # Show selection prompt when industry/company not both selected
    elif not st.session_state.selected_industry or not st.session_state.selected_company_key:
        st.markdown("""
        <div class="info-card">
            <h3>Select Industry & Company</h3>
            <p>Choose your industry and company from the sidebar to start chatting</p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()