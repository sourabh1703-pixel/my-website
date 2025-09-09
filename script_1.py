# Now let's also update the other pages to fix the same text visibility issues

# Update Portfolio.py
updated_portfolio_code = '''import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Portfolio - SAPMaster Solutions",
    page_icon="📊",
    layout="wide"
)

# Custom CSS with improved text visibility
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .portfolio-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .project-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border-left: 4px solid #667eea;
        color: #333 !important;
    }
    
    .project-card h3, .project-card h4 {
        color: #667eea !important;
    }
    
    .project-card p {
        color: #666 !important;
    }
    
    .project-card strong {
        color: #333 !important;
    }
    
    .project-card ul li {
        color: #555 !important;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white !important;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .metric-card h3 {
        color: white !important;
    }
    
    .metric-card p {
        color: white !important;
    }
    
    .tech-stack {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    .tech-stack strong {
        color: #333 !important;
    }
    
    .tech-badge {
        background: #667eea;
        color: white !important;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.8rem;
        display: inline-block;
    }
    
    /* Fix for all text elements */
    div[data-testid="stMarkdownContainer"] p {
        color: inherit !important;
    }
    
    div[data-testid="stMarkdownContainer"] li {
        color: inherit !important;
    }
    
    div[data-testid="stMarkdownContainer"] h1,
    div[data-testid="stMarkdownContainer"] h2,
    div[data-testid="stMarkdownContainer"] h3,
    div[data-testid="stMarkdownContainer"] h4 {
        color: inherit !important;
    }
</style>
""", unsafe_allow_html=True)

def render_portfolio_header():
    """Render portfolio header"""
    header_html = """
    <div class="portfolio-header">
        <h1 style="color: white;">Our Portfolio & Case Studies</h1>
        <p style="font-size: 1.2rem; opacity: 0.9; color: white;">
            Demonstrating real-world impact through innovative SAP solutions and GenAI automation
        </p>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

def render_case_studies():
    """Render case studies section"""
    st.markdown("## 📈 Featured Case Studies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        case_study_html = """
        <div class="project-card">
            <h3 style="color: #667eea !important;">🏭 Manufacturing Giant - SAP S/4HANA Migration</h3>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Client:</strong> Fortune 500 Manufacturing Company</p>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Challenge:</strong> Legacy ECC system causing performance bottlenecks and limiting scalability</p>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Solution:</strong> Complete S/4HANA migration with GenAI-powered data cleansing and custom ABAP optimization</p>
            <div class="tech-stack">
                <strong style="color: #333 !important;">Technologies:</strong><br>
                <span class="tech-badge">SAP S/4HANA</span>
                <span class="tech-badge">ABAP</span>
                <span class="tech-badge">SAP BTP</span>
                <span class="tech-badge">GenAI</span>
                <span class="tech-badge">Python</span>
            </div>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Results:</strong></p>
            <ul>
                <li style="color: #555 !important;">40% improvement in system performance</li>
                <li style="color: #555 !important;">60% reduction in monthly maintenance costs</li>
                <li style="color: #555 !important;">Real-time analytics and reporting capabilities</li>
                <li style="color: #555 !important;">$2M annual cost savings</li>
            </ul>
        </div>
        """
        st.markdown(case_study_html, unsafe_allow_html=True)
    
    with col2:
        case_study_html = """
        <div class="project-card">
            <h3 style="color: #667eea !important;">🏦 Financial Services - GenAI Document Processing</h3>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Client:</strong> Regional Banking Institution</p>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Challenge:</strong> Manual processing of loan documents causing delays and errors</p>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Solution:</strong> AI-powered document processing integrated with SAP systems for automated workflows</p>
            <div class="tech-stack">
                <strong style="color: #333 !important;">Technologies:</strong><br>
                <span class="tech-badge">OpenAI GPT</span>
                <span class="tech-badge">SAP BTP</span>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">OCR</span>
                <span class="tech-badge">Streamlit</span>
            </div>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Results:</strong></p>
            <ul>
                <li style="color: #555 !important;">85% reduction in document processing time</li>
                <li style="color: #555 !important;">95% accuracy in data extraction</li>
                <li style="color: #555 !important;">50% faster loan approval process</li>
                <li style="color: #555 !important;">$800K annual operational savings</li>
            </ul>
        </div>
        """
        st.markdown(case_study_html, unsafe_allow_html=True)

    # Additional case studies
    st.markdown("### 🔍 More Success Stories")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #667eea !important;">🚗 Automotive - ABAP Performance Optimization</h4>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Challenge:</strong> Custom ABAP programs causing system slowdowns</p>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Solution:</strong> Code optimization and performance tuning</p>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Result:</strong> 75% faster processing, $500K savings</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #667eea !important;">🏥 Healthcare - SAP Basis Upgrade</h4>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Challenge:</strong> Outdated system affecting patient care</p>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Solution:</strong> Zero-downtime upgrade with enhanced security</p>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Result:</strong> 99.9% uptime, improved compliance</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="project-card">
            <h4 style="color: #667eea !important;">🛒 Retail - AI-Powered Inventory</h4>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Challenge:</strong> Manual inventory management inefficiencies</p>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Solution:</strong> GenAI integration for demand forecasting</p>
            <p style="color: #666 !important;"><strong style="color: #333 !important;">Result:</strong> 30% reduction in stockouts</p>
        </div>
        """, unsafe_allow_html=True)

def render_metrics_dashboard():
    """Render key metrics and KPIs"""
    st.markdown("## 📊 Key Performance Indicators")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: white !important;">150+</h3>
            <p style="color: white !important;">Projects Delivered</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: white !important;">$15M+</h3>
            <p style="color: white !important;">Client Cost Savings</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: white !important;">99.7%</h3>
            <p style="color: white !important;">Project Success Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: white !important;">24/7</h3>
            <p style="color: white !important;">Support Available</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Sample data tables
    st.markdown("### 📈 Sample Project Performance Data")
    
    # Create sample data
    project_data = pd.DataFrame({
        'Project Name': ['ERP Migration Alpha', 'ABAP Optimization Beta', 'GenAI Integration Gamma', 'Basis Upgrade Delta'],
        'Industry': ['Manufacturing', 'Finance', 'Healthcare', 'Retail'],
        'Duration (months)': [12, 6, 8, 4],
        'Budget ($K)': [750, 200, 400, 150],
        'ROI (%)': [250, 180, 220, 160],
        'Status': ['Completed', 'Completed', 'In Progress', 'Completed']
    })
    
    st.dataframe(project_data, use_container_width=True)
    
    # Technology adoption metrics
    st.markdown("### 🛠️ Technology Adoption Rates")
    
    tech_data = pd.DataFrame({
        'Technology': ['SAP S/4HANA', 'SAP BTP', 'GenAI Integration', 'ABAP on HANA', 'Cloud Migration'],
        'Adoption Rate (%)': [85, 75, 60, 90, 70],
        'Client Satisfaction': [4.8, 4.6, 4.9, 4.7, 4.5],
        'Projects Count': [45, 38, 25, 52, 35]
    })
    
    st.dataframe(tech_data, use_container_width=True)

def render_genai_demo():
    """Render GenAI demonstration section"""
    st.markdown("## 🤖 GenAI Integration Showcase")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 💬 AI-Powered SAP Assistant (Interactive Demo)")
        
        # Sample conversation interface
        st.markdown("**Sample Interactions:**")
        
        conversation_examples = [
            {
                "user": "Show me the top 5 vendors by purchase volume this quarter",
                "ai": """I've analyzed your SAP MM data for Q3 2024. Here are the top 5 vendors:
                
1. **TechSupply Corp** - $2.4M (35% of total)
2. **GlobalParts Ltd** - $1.8M (26% of total) 
3. **Industrial Solutions** - $1.2M (17% of total)
4. **QualityMaterials Inc** - $0.9M (13% of total)
5. **FastDelivery Co** - $0.6M (9% of total)

Would you like me to generate a detailed report or identify spending patterns?"""
            },
            {
                "user": "Generate a performance report for our SAP system",
                "ai": """SAP System Performance Report - September 2024:

📈 **Key Metrics:**
- Average response time: 2.3s ✅ (Target: <3s)
- System availability: 99.7% ✅ (Target: >99.5%)
- Peak concurrent users: 247 ✅ (Capacity: 300)
- Failed transactions: 0.2% ✅ (Target: <1%)

🔍 **Recommendations:**
- Archive old data to improve query performance
- Schedule memory optimization during off-hours
- Monitor disk space (currently at 78%)"""
            }
        ]
        
        for i, conv in enumerate(conversation_examples):
            with st.expander(f"Example {i+1}: {conv['user'][:50]}..."):
                st.markdown(f"**User Query:** {conv['user']}")
                st.markdown(f"**AI Response:**")
                st.markdown(conv['ai'])
        
        # Interactive input
        st.markdown("### Try the Demo Interface:")
        user_query = st.text_input("Ask the AI Assistant:", 
                                 placeholder="e.g., Show me invoice processing delays...")
        
        if user_query:
            st.markdown(f"**Your Query:** {user_query}")
            st.info("🤖 **AI Response:** This is a demo interface. In production, this would connect to your SAP system and provide intelligent responses based on your actual data, using advanced GenAI models to understand context and deliver actionable insights.")
    
    with col2:
        demo_features = """
        <div class="project-card">
            <h3 style="color: #667eea !important;">🚀 AI Capabilities</h3>
            <ul>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Natural Language Processing:</strong> Ask questions in plain English</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Automated Reporting:</strong> Generate insights on demand</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Anomaly Detection:</strong> Identify unusual patterns</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Predictive Analytics:</strong> Forecast trends</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Smart Recommendations:</strong> AI-driven optimization</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Multi-language Support:</strong> Global communication</li>
            </ul>
            
            <h4 style="color: #667eea !important; margin-top: 1.5rem;">Integration Points:</h4>
            <span class="tech-badge">SAP ERP</span>
            <span class="tech-badge">SAP BW</span>
            <span class="tech-badge">SAP HANA</span>
            <span class="tech-badge">SAP BTP</span>
            <span class="tech-badge">External APIs</span>
            
            <h4 style="color: #667eea !important; margin-top: 1.5rem;">AI Models Used:</h4>
            <span class="tech-badge">GPT-4</span>
            <span class="tech-badge">Claude</span>
            <span class="tech-badge">Custom Models</span>
            <span class="tech-badge">Azure OpenAI</span>
        </div>
        """
        st.markdown(demo_features, unsafe_allow_html=True)

def render_testimonials():
    """Render client testimonials"""
    st.markdown("## 💬 Client Success Stories")
    
    col1, col2, col3 = st.columns(3)
    
    testimonials = [
        {
            "quote": "SAPMaster Solutions transformed our entire SAP landscape. Their GenAI integration reduced our manual processing time by 80% and the ROI was evident within 6 months.",
            "name": "Sarah Johnson",
            "title": "CTO, Manufacturing Excellence Corp",
            "rating": "⭐⭐⭐⭐⭐"
        },
        {
            "quote": "The ABAP optimization work was exceptional. Our system performance improved dramatically and the team's expertise in both traditional SAP and modern AI is unmatched.",
            "name": "Michael Chen",
            "title": "IT Director, Global Finance Solutions",
            "rating": "⭐⭐⭐⭐⭐"
        },
        {
            "quote": "Professional, knowledgeable, and innovative. They delivered our S/4HANA migration on time and under budget, with zero business disruption.",
            "name": "Emma Rodriguez",
            "title": "VP Operations, TechVenture Inc",
            "rating": "⭐⭐⭐⭐⭐"
        }
    ]
    
    for i, testimonial in enumerate(testimonials):
        with [col1, col2, col3][i]:
            testimonial_html = f"""
            <div class="project-card">
                <p style="font-style: italic; margin-bottom: 1rem; color: #666 !important;">
                    "{testimonial['quote']}"
                </p>
                <p style="color: #555 !important;">{testimonial['rating']}</p>
                <p style="color: #666 !important;"><strong style="color: #333 !important;">- {testimonial['name']}</strong><br>
                <small style="color: #999 !important;">{testimonial['title']}</small></p>
            </div>
            """
            st.markdown(testimonial_html, unsafe_allow_html=True)
    
    # Additional testimonials
    st.markdown("### 📝 More Client Feedback")
    
    additional_testimonials = [
        "The GenAI document processing solution has revolutionized our accounts payable process. We're processing invoices 5x faster with 99% accuracy. - David Kim, CFO",
        "Their SAP Basis expertise kept our critical systems running smoothly during a complex upgrade. Outstanding technical knowledge and communication. - Lisa Wang, Systems Manager",
        "The custom ABAP development exceeded our expectations. Clean code, excellent documentation, and ongoing support. Highly recommended! - Roberto Silva, Development Lead"
    ]
    
    for testimonial in additional_testimonials:
        st.markdown(f"💬 *{testimonial}*")
        st.markdown("---")

def main():
    """Main portfolio page"""
    render_portfolio_header()
    
    # Navigation tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Case Studies", "📊 Metrics & KPIs", "🤖 AI Showcase", "💬 Testimonials"])
    
    with tab1:
        render_case_studies()
    
    with tab2:
        render_metrics_dashboard()
    
    with tab3:
        render_genai_demo()
    
    with tab4:
        render_testimonials()
    
    # Call-to-action at the bottom
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white; margin-top: 2rem;">
        <h3 style="color: white !important;">Ready to Transform Your SAP Environment?</h3>
        <p style="font-size: 1.1rem; margin-bottom: 1.5rem; color: white !important;">
            Let's discuss how our proven SAP consulting and GenAI automation solutions can drive your business forward.
        </p>
        <p style="font-size: 1rem; color: white !important;">
            📧 Contact us at: <strong style="color: white !important;">info@sapmaster-solutions.com</strong> | 📱 Call: <strong style="color: white !important;">+1 (555) 123-4567</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
'''

# Save the updated portfolio page
with open('pages/Portfolio.py', 'w', encoding='utf-8') as f:
    f.write(updated_portfolio_code)

print("✅ Updated pages/Portfolio.py with improved text visibility")