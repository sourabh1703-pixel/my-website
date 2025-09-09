import streamlit as st
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Susthira AI - SAP Consulting & GenAI Automation",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling with improved text visibility
def load_css():
    css = """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin-bottom: 3rem;
        color: white;
        text-align: center;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        line-height: 1.2;
        color: white;
    }

    .hero-subtitle {
        font-size: 1.4rem;
        font-weight: 400;
        margin-bottom: 2rem;
        opacity: 0.9;
        color: white;
    }

    .cta-button {
        background: #ff6b6b;
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        margin: 0.5rem;
    }

    .cta-button:hover {
        background: #ff5252;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);
        color: white;
    }

    /* Service Cards - FIXED TEXT VISIBILITY */
    .service-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
        color: #333;
    }

    .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }

    .service-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #333 !important;
        margin-bottom: 1rem;
    }

    .service-description {
        color: #666 !important;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        font-size: 1rem;
    }

    .service-features {
        list-style: none;
        padding: 0;
        color: #555 !important;
    }

    .service-features li {
        padding: 0.5rem 0;
        position: relative;
        padding-left: 1.5rem;
        color: #555 !important;
        font-size: 0.95rem;
    }

    .service-features li:before {
        content: "✓";
        position: absolute;
        left: 0;
        color: #4CAF50 !important;
        font-weight: bold;
    }

    /* Stats Section */
    .stats-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin: 3rem 0;
        color: white;
    }

    .stat-item {
        text-align: center;
        padding: 1rem;
    }

    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        display: block;
        color: white;
    }

    .stat-label {
        font-size: 1.1rem;
        opacity: 0.9;
        color: white;
    }

    /* Technology Section */
    .tech-badge {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white !important;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        margin: 0.25rem;
        font-weight: 500;
        display: inline-block;
        font-size: 0.9rem;
    }

    /* Contact Section - IMPROVED VISIBILITY */
    .contact-section h3 {
        background: #f8f9fa;
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-top: 3rem;
 	color: #333 !important;
    	font-weight: 600;
    }

    .contact-form {
        background: pink;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }

    .contact-form h4 {
        color: #333 !important;
	font-weight: 600;
    }

    .contact-form p {
        color: #666 !important;
    }

    /* Navigation */
    .nav-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 1rem 2rem;
        border-radius: 50px;
        margin-bottom: 2rem;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }

    .nav-item {
        display: inline-block;
        margin: 0 1rem;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        text-decoration: none;
        color: #333 !important;
        font-weight: 500;
        transition: all 0.3s ease;
    }

    .nav-item:hover {
        background: #667eea;
        color: white !important;
    }

    /* Fix for all white background containers */
    .white-container {
        background: white;
        color: #333 !important;
    }

    .white-container h1, 
    .white-container h2, 
    .white-container h3, 
    .white-container h4, 
    .white-container h5, 
    .white-container h6 {
        color: #333 !important;
    }

    .white-container p {
        color: #666 !important;
    }

    .white-container li {
        color: #555 !important;
    }

    /* About section text fixes */
    .service-card h3 {
        color: #667eea !important;
    }

    .service-card h4 {
        color: #667eea !important;
    }

    .service-card strong {
        color: #333 !important;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }

        .hero-subtitle {
            font-size: 1.2rem;
        }

        .service-card {
            margin-bottom: 1rem;
            padding: 1.5rem;
        }

        .nav-container {
            text-align: center;
        }

        .nav-item {
            display: block;
            margin: 0.5rem 0;
        }
    }

    /* Streamlit specific fixes */
    .stMarkdown {
        color: inherit;
    }

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
    """
    st.markdown(css, unsafe_allow_html=True)

def render_hero_section():
    """Render the hero section"""
    hero_html = """
    <div class="hero-section">
        <h1 class="hero-title">Susthira AI </h1>
        <p class="hero-subtitle">Transform Your Business with Expert SAP Consulting & GenAI Automation in a Stable(Susthira) Way</p>
        <p style="font-size: 1.1rem; margin-bottom: 2rem; opacity: 0.9; color: white;">
            Specializing in SAP Basis, ABAP Development, and Functional Consulting with cutting-edge GenAI integration
        </p>
        <a href="#contact" class="cta-button">Get Free Consultation</a>
        <a href="#services" class="cta-button" style="background: transparent; border: 2px solid white; color: white;">Our Services</a>
    </div>
    """
    st.markdown(hero_html, unsafe_allow_html=True)

def render_navigation():
    """Render navigation menu"""
    nav_html = """
    <div class="nav-container">
        <a href="#home" class="nav-item">Home</a>
        <a href="#services" class="nav-item">Services</a>
        <a href="#genai" class="nav-item">GenAI Solutions</a>
        <a href="#about" class="nav-item">About</a>
        <a href="#contact" class="nav-item">Contact</a>
    </div>
    """
    st.markdown(nav_html, unsafe_allow_html=True)

def render_services_section():
    """Render services section"""
    st.markdown('<div id="services"></div>', unsafe_allow_html=True)
    st.markdown("## 🚀 Our Core Services")

    col1, col2, col3 = st.columns(3)

    with col1:
        service_html = """
        <div class="service-card white-container">
            <h3 class="service-title" style="color: #667eea !important;">🔧 SAP Basis Administration</h3>
            <p class="service-description" style="color: #666 !important;">
                Expert SAP Basis consulting to ensure your systems run smoothly, securely, and efficiently.
            </p>
            <ul class="service-features">
                <li style="color: #555 !important;">System Installation & Configuration</li>
                <li style="color: #555 !important;">Performance Monitoring & Tuning</li>
                <li style="color: #555 !important;">Security Implementation</li>
                <li style="color: #555 !important;">Backup & Recovery Solutions</li>
                <li style="color: #555 !important;">System Upgrades & Migrations</li>
                <li style="color: #555 !important;">Transport Management</li>
            </ul>
        </div>
        """
        st.markdown(service_html, unsafe_allow_html=True)

    with col2:
        service_html = """
        <div class="service-card white-container">
            <h3 class="service-title" style="color: #667eea !important;">💻 SAP ABAP Development</h3>
            <p class="service-description" style="color: #666 !important;">
                Custom ABAP development and optimization to meet your unique business requirements.
            </p>
            <ul class="service-features">
                <li style="color: #555 !important;">Custom Report Development</li>
                <li style="color: #555 !important;">Interface & Integration Programming</li>
                <li style="color: #555 !important;">Enhancement & Modification</li>
                <li style="color: #555 !important;">Performance Optimization</li>
                <li style="color: #555 !important;">Object-Oriented Programming</li>
                <li style="color: #555 !important;">Web Dynpro & UI5 Development</li>
            </ul>
        </div>
        """
        st.markdown(service_html, unsafe_allow_html=True)

    with col3:
        service_html = """
        <div class="service-card white-container">
            <h3 class="service-title" style="color: #667eea !important;">📊 SAP Functional Consulting</h3>
            <p class="service-description" style="color: #666 !important;">
                End-to-end functional consulting across various SAP modules to optimize your business processes.
            </p>
            <ul class="service-features">
                <li style="color: #555 !important;">SAP FI/CO Implementation</li>
                <li style="color: #555 !important;">SAP MM & SD Configuration</li>
                <li style="color: #555 !important;">Business Process Analysis</li>
                <li style="color: #555 !important;">User Training & Support</li>
                <li style="color: #555 !important;">System Integration</li>
                <li style="color: #555 !important;">Go-Live Support</li>
            </ul>
        </div>
        """
        st.markdown(service_html, unsafe_allow_html=True)

def render_genai_section():
    """Render GenAI automation section"""
    st.markdown('<div id="genai"></div>', unsafe_allow_html=True)
    st.markdown("## 🤖 GenAI-Powered Automation Solutions")

    col1, col2 = st.columns([2, 1])

    with col1:
        genai_html = """
        <div class="service-card white-container">
            <h3 class="service-title" style="color: #667eea !important;">🧠 Intelligent SAP Automation</h3>
            <p class="service-description" style="color: #666 !important;">
                Leverage the power of Generative AI to transform your SAP operations with intelligent automation, 
                predictive analytics, and enhanced decision-making capabilities.
            </p>
            <h4 style="color: #667eea !important; margin-top: 2rem;">Key GenAI Capabilities:</h4>
            <ul class="service-features">
                <li style="color: #555 !important;">AI-Powered Document Processing & Data Extraction</li>
                <li style="color: #555 !important;">Intelligent Process Automation & Workflow Optimization</li>
                <li style="color: #555 !important;">Natural Language Query Interface for SAP Data</li>
                <li style="color: #555 !important;">Predictive Maintenance & Performance Analytics</li>
                <li style="color: #555 !important;">Automated Report Generation & Insights</li>
                <li style="color: #555 !important;">Smart Error Detection & Resolution</li>
                <li style="color: #555 !important;">AI-Driven User Support & Chatbots</li>
                <li style="color: #555 !important;">Custom AI Model Development for SAP</li>
            </ul>
        </div>
        """
        st.markdown(genai_html, unsafe_allow_html=True)

    with col2:
        tech_html = """
        <div class="service-card white-container">
            <h3 class="service-title" style="color: #667eea !important;">🛠️ Technologies We Use</h3>
            <div style="margin-top: 1rem;">
                <span class="tech-badge">SAP BTP</span>
                <span class="tech-badge">SAP AI Core</span>
                <span class="tech-badge">OpenAI GPT</span>
                <span class="tech-badge">Azure AI</span>
                <span class="tech-badge">Python</span>
                <span class="tech-badge">TensorFlow</span>
                <span class="tech-badge">PyTorch</span>
                <span class="tech-badge">Streamlit</span>
                <span class="tech-badge">FastAPI</span>
                <span class="tech-badge">Docker</span>
                <span class="tech-badge">Kubernetes</span>
                <span class="tech-badge">SAP HANA</span>
            </div>
        </div>
        """
        st.markdown(tech_html, unsafe_allow_html=True)

def render_stats_section():
    """Render statistics section"""
    stats_html = """
    <div class="stats-container">
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="margin-bottom: 1rem; color: white;">Why Choose Susthira AI?</h2>
            <p style="font-size: 1.2rem; opacity: 0.9; color: white;">Proven track record of delivering exceptional SAP solutions</p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;">
            <div class="stat-item">
                <span class="stat-number">20+</span>
                <span class="stat-label">Projects Completed</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">10+</span>
                <span class="stat-label">Happy Clients</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">10+</span>
                <span class="stat-label">Years Experience</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">100%</span>
                <span class="stat-label">Success Rate</span>
            </div>
        </div>
    </div>
    """
    st.markdown(stats_html, unsafe_allow_html=True)

def render_about_section():
    """Render about section"""
    st.markdown('<div id="about"></div>', unsafe_allow_html=True)
    st.markdown("## 🏢 About Susthira AI")

    col1, col2 = st.columns([2, 1])

    with col1:
        about_html = """
        <div class="service-card white-container">
            <p style="font-size: 1.1rem; line-height: 1.8; color: #555 !important;">
                At <strong style="color: #333 !important;">Susthira AI</strong>, we are passionate about transforming businesses through 
                innovative SAP consulting and cutting-edge GenAI automation. With over a decade of experience 
                in the SAP ecosystem, our team of certified consultants specializes in delivering comprehensive 
                solutions that drive efficiency, reduce costs, and accelerate digital transformation.
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; color: #555 !important; margin-top: 1.5rem;">
                We combine deep SAP expertise with the latest advances in Generative AI to create intelligent, 
                automated solutions that not only solve today's challenges but anticipate tomorrow's opportunities. 
                From SAP Basis administration to complex ABAP development and functional consulting, we deliver 
                results that matter.
            </p>
            <h4 style="color: #667eea !important; margin-top: 2rem;">Our Expertise Includes:</h4>
            <ul class="service-features">
                <li style="color: #555 !important;">SAP S/4HANA Implementation & Migration</li>
                <li style="color: #555 !important;">SAP Cloud Platform (BTP) Solutions</li>
                <li style="color: #555 !important;">GenAI Integration & Custom AI Development</li>
                <li style="color: #555 !important;">Enterprise Architecture & System Integration</li>
                <li style="color: #555 !important;">Change Management & User Adoption</li>
            </ul>
        </div>
        """
        st.markdown(about_html, unsafe_allow_html=True)

    with col2:
        # Using Streamlit native approach to avoid HTML parsing issues
        st.markdown("### 🏆 Certifications & Partnerships")
        
        certifications = [
            "SAP Certified Technology Consultant",
            "SAP Certified Development Specialist",
            "SAP Certified Application Associate",
            "Microsoft Azure AI Engineer",
            "AWS Machine Learning Specialty",
            "Google Cloud AI/ML Professional"
        ]
        
        for cert in certifications:
            st.markdown(f"✅ {cert}")
        
        st.markdown("#### Industry Focus:")
        
        industries = [
            "Manufacturing & Automotive", 
            "Financial Services",
            "Healthcare & Life Sciences",
            "Retail & Consumer Goods",
            "Energy & Utilities"
        ]
        
        for industry in industries:
            st.markdown(f"✅ {industry}")


def render_contact_section():
    """Render contact section"""
    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.markdown("## 📞 Get In Touch")

    contact_html = """
    <div class="contact-section">
        <div style="text-align: center; margin-bottom: 2rem;">
            <h3 style="color: #333 !important;">Ready to Transform Your SAP Environment?</h3>
            <p style="font-size: 1.1rem; color: #666 !important;">
                Let's discuss how our SAP consulting and GenAI automation solutions can drive your business forward.
            </p>
        </div>
    """
    st.markdown(contact_html, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        contact_form_html = """
        <div class="contact-form">
            <h4 style="text-align: center; margin-bottom: 1.5rem; color: #333 !important;">Request a Free Consultation</h4>
        """
        st.markdown(contact_form_html, unsafe_allow_html=True)

        # Contact form
        with st.form("contact_form"):
            name = st.text_input("Full Name *", placeholder="Enter your full name")
            email = st.text_input("Email Address *", placeholder="Enter your email address")
            company = st.text_input("Company Name", placeholder="Enter your company name")

            service_type = st.selectbox(
                "Service Interest *",
                ["Select a service...", "SAP Basis Administration", "SAP ABAP Development", 
                 "SAP Functional Consulting", "GenAI Automation Solutions", "Complete SAP Transformation", "Other"]
            )

            project_timeline = st.selectbox(
                "Project Timeline",
                ["Select timeline...", "Immediate (Within 1 month)", "Short-term (1-3 months)", 
                 "Medium-term (3-6 months)", "Long-term (6+ months)", "Just exploring options"]
            )

            message = st.text_area(
                "Project Details *", 
                placeholder="Please describe your project requirements, challenges, or questions...",
                height=100
            )

            col_submit1, col_submit2, col_submit3 = st.columns([1, 2, 1])
            with col_submit2:
                submitted = st.form_submit_button(
                    "Send Message", 
                    use_container_width=True,
                    type="primary"
                )

            if submitted:
                if name and email and service_type != "Select a service..." and message:
                    st.success("✅ Thank you! Your message has been sent. We'll get back to you within 24 hours.")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields marked with *")

        st.markdown("</div>", unsafe_allow_html=True)

    # Contact information
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        contact_info_html = """
        <div style="text-align: center; padding: 1rem;">
            <h4 style="color: #667eea !important;">📧 Email</h4>
            <p style="color: #555 !important;">susthira.ai.1@gmail.com</p>
            <p style="color: #555 !important;">support@SRK-solutions.com</p>
        </div>
        """
        st.markdown(contact_info_html, unsafe_allow_html=True)

    with col2:
        contact_info_html = """
        <div style="text-align: center; padding: 1rem;">
            <h4 style="color: #667eea !important;">📱 Phone</h4>
            <p style="color: #555 !important;">+91 (860) 245-9300</p>
            <p style="color: #555 !important;">+1 (555) 987-6543</p>
        </div>
        """
        st.markdown(contact_info_html, unsafe_allow_html=True)

    with col3:
        contact_info_html = """
        <div style="text-align: center; padding: 1rem;">
            <h4 style="color: #667eea !important;">🌐 Connect</h4>
            <p style="color: #555 !important;">LinkedIn | Twitter</p>
            <p style="color: #555 !important;">Schedule a Call</p>
        </div>
        """
        st.markdown(contact_info_html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

def render_footer():
    """Render footer"""
    footer_html = """
    <div style="background: #333; color: white; padding: 2rem; border-radius: 20px; margin-top: 3rem; text-align: center;">
        <h3 style="margin-bottom: 1rem; color: white;">Susthira AI</h3>
        <p style="opacity: 0.8; margin-bottom: 1rem; color: white;">Transforming Businesses Through Expert SAP Consulting & GenAI Innovation</p>
        <p style="opacity: 0.6; font-size: 0.9rem; color: white;">
            © 2025 Susthira AI. All rights reserved. | Privacy Policy | Terms of Service
        </p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

def main():
    """Main application function"""
    # Load custom CSS
    load_css()

    # Navigation
    render_navigation()

    # Hero Section
    render_hero_section()

    # Services Section
    render_services_section()

    # GenAI Section
    render_genai_section()

    # Stats Section
    render_stats_section()

    # About Section
    render_about_section()

    # Contact Section
    render_contact_section()

    # Footer
    render_footer()

if __name__ == "__main__":
    main()
