import streamlit as st
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

def main():
    """Main portfolio page"""
    render_portfolio_header()

    # Navigation tabs
    tab1, tab2, tab3 = st.tabs(["📈 Case Studies", "📊 Metrics", "💬 Testimonials"])

    with tab1:
        render_case_studies()

    with tab2:
        render_metrics_dashboard()

    with tab3:
        render_testimonials()

if __name__ == "__main__":
    main()
