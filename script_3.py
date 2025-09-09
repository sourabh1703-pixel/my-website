# Now let's also update the Services and About pages with the same text visibility fixes

# Update Services.py
services_code = '''import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Services - SAPMaster Solutions",
    page_icon="⚙️",
    layout="wide"
)

# Custom CSS with improved text visibility
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .services-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .service-detail-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .service-detail-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }
    
    .service-detail-card h3, .service-detail-card h4 {
        color: #667eea !important;
    }
    
    .service-detail-card p {
        color: #666 !important;
    }
    
    .service-detail-card strong {
        color: #333 !important;
    }
    
    .service-detail-card ul li {
        color: #555 !important;
    }
    
    .pricing-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white !important;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .pricing-card h3 {
        color: white !important;
    }
    
    .pricing-card p {
        color: white !important;
    }
    
    .pricing-card div {
        color: white !important;
    }
    
    .pricing-card ul {
        color: white !important;
    }
    
    .pricing-card li {
        color: white !important;
        opacity: 0.9;
    }
    
    .process-step {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        border-left: 4px solid #4CAF50;
    }
    
    .process-step h4 {
        color: #333 !important;
    }
    
    .process-step p {
        color: #666 !important;
    }
    
    .process-step strong {
        color: #667eea !important;
    }
    
    .process-step ul li {
        color: #666 !important;
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
    
    .feature-list {
        list-style: none;
        padding: 0;
    }
    
    .feature-list li {
        padding: 0.5rem 0;
        position: relative;
        padding-left: 1.5rem;
        color: #555 !important;
    }
    
    .feature-list li:before {
        content: "✓";
        position: absolute;
        left: 0;
        color: #4CAF50 !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def render_services_header():
    """Render services page header"""
    header_html = """
    <div class="services-header">
        <h1 style="color: white;">Our Services</h1>
        <p style="font-size: 1.3rem; opacity: 0.9; margin-bottom: 1rem; color: white;">
            Comprehensive SAP Consulting & GenAI Automation Solutions
        </p>
        <p style="font-size: 1.1rem; opacity: 0.8; color: white;">
            From traditional SAP consulting to cutting-edge AI integration - we deliver end-to-end solutions
        </p>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

def render_sap_basis_services():
    """Render SAP Basis services details"""
    st.markdown("## 🔧 SAP Basis Administration Services")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        basis_html = """
        <div class="service-detail-card">
            <h3 style="color: #667eea !important; margin-bottom: 1.5rem;">Complete SAP Basis Lifecycle Management</h3>
            <p style="font-size: 1.1rem; color: #666 !important; line-height: 1.7; margin-bottom: 2rem;">
                Our SAP Basis experts provide comprehensive system administration services to ensure your SAP landscape 
                runs optimally, securely, and efficiently. From initial setup to ongoing maintenance, we handle all 
                technical aspects of your SAP environment.
            </p>
            
            <h4 style="color: #667eea !important; margin-bottom: 1rem;">Core Services Include:</h4>
            <ul class="feature-list">
                <li style="color: #555 !important;"><strong style="color: #333 !important;">System Installation & Configuration:</strong> Complete SAP system setup with best practices</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Performance Monitoring & Tuning:</strong> Proactive monitoring with automated alerts</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Security Implementation:</strong> User management, authorization concepts, and compliance</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Backup & Recovery:</strong> Comprehensive disaster recovery planning and implementation</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">System Upgrades:</strong> Zero-downtime upgrades and patches</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Transport Management:</strong> Streamlined change management processes</li>
            </ul>
        </div>
        """
        st.markdown(basis_html, unsafe_allow_html=True)
    
    with col2:
        basis_details_html = """
        <div class="service-detail-card">
            <h4 style="color: #667eea !important;">Technologies We Support</h4>
            <div style="margin: 1rem 0;">
                <span class="tech-badge">SAP NetWeaver</span>
                <span class="tech-badge">SAP HANA</span>
                <span class="tech-badge">SAP S/4HANA</span>
                <span class="tech-badge">SAP BW</span>
                <span class="tech-badge">Linux</span>
                <span class="tech-badge">Windows</span>
                <span class="tech-badge">Oracle</span>
                <span class="tech-badge">SQL Server</span>
            </div>
            
            <h4 style="color: #667eea !important; margin-top: 2rem;">Key Benefits</h4>
            <ul class="feature-list">
                <li style="color: #555 !important;">99.9% system uptime guarantee</li>
                <li style="color: #555 !important;">30% reduction in maintenance costs</li>
                <li style="color: #555 !important;">Automated monitoring and alerting</li>
                <li style="color: #555 !important;">24/7 expert support</li>
                <li style="color: #555 !important;">Compliance with security standards</li>
                <li style="color: #555 !important;">Proactive performance optimization</li>
            </ul>
        </div>
        """
        st.markdown(basis_details_html, unsafe_allow_html=True)

def render_abap_services():
    """Render ABAP development services"""
    st.markdown("## 💻 SAP ABAP Development Services")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        abap_html = """
        <div class="service-detail-card">
            <h3 style="color: #667eea !important; margin-bottom: 1.5rem;">Custom ABAP Development & Optimization</h3>
            <p style="font-size: 1.1rem; color: #666 !important; line-height: 1.7; margin-bottom: 2rem;">
                Our certified ABAP developers create high-performance, scalable solutions tailored to your business needs. 
                From simple reports to complex enterprise applications, we deliver clean, maintainable code that follows 
                SAP best practices and modern development standards.
            </p>
            
            <h4 style="color: #667eea !important; margin-bottom: 1rem;">Development Services:</h4>
            <ul class="feature-list">
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Custom Reports & Forms:</strong> Classical and ALV reports, Adobe Forms, Smart Forms</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Interface Development:</strong> RFC, IDoc, web services, API integrations</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Enhancement & Modifications:</strong> User exits, customer exits, enhancement framework</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Object-Oriented Programming:</strong> Classes, methods, inheritance, polymorphism</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Web Development:</strong> Web Dynpro ABAP, BSP, REST services</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Performance Optimization:</strong> Code review, SQL optimization, memory management</li>
            </ul>
        </div>
        """
        st.markdown(abap_html, unsafe_allow_html=True)
    
    with col2:
        abap_details_html = """
        <div class="service-detail-card">
            <h4 style="color: #667eea !important;">ABAP Expertise Areas</h4>
            <div style="margin: 1rem 0;">
                <span class="tech-badge">ABAP Objects</span>
                <span class="tech-badge">Web Dynpro</span>
                <span class="tech-badge">ALV</span>
                <span class="tech-badge">IDoc</span>
                <span class="tech-badge">RFC</span>
                <span class="tech-badge">BAPI</span>
                <span class="tech-badge">Workflow</span>
                <span class="tech-badge">Smart Forms</span>
                <span class="tech-badge">Adobe Forms</span>
                <span class="tech-badge">CDS Views</span>
                <span class="tech-badge">REST/OData</span>
            </div>
            
            <h4 style="color: #667eea !important; margin-top: 2rem;">Performance Metrics</h4>
            <ul class="feature-list">
                <li style="color: #555 !important;">75% faster code execution</li>
                <li style="color: #555 !important;">50% reduction in development time</li>
                <li style="color: #555 !important;">95% code quality score</li>
                <li style="color: #555 !important;">Zero critical bugs in production</li>
                <li style="color: #555 !important;">Comprehensive documentation</li>
                <li style="color: #555 !important;">Knowledge transfer included</li>
            </ul>
        </div>
        """
        st.markdown(abap_details_html, unsafe_allow_html=True)

def render_functional_services():
    """Render functional consulting services"""
    st.markdown("## 📊 SAP Functional Consulting Services")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        functional_html = """
        <div class="service-detail-card">
            <h3 style="color: #667eea !important; margin-bottom: 1.5rem;">End-to-End Functional Implementation</h3>
            <p style="font-size: 1.1rem; color: #666 !important; line-height: 1.7; margin-bottom: 2rem;">
                Our functional consultants bring deep business process knowledge and extensive SAP module expertise 
                to optimize your operations. We analyze your requirements, design efficient processes, and implement 
                solutions that drive business value and operational excellence.
            </p>
            
            <h4 style="color: #667eea !important; margin-bottom: 1rem;">Functional Areas:</h4>
            <ul class="feature-list">
                <li style="color: #555 !important;"><strong style="color: #333 !important;">SAP FI/CO:</strong> Financial accounting, controlling, asset management, profitability analysis</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">SAP MM:</strong> Materials management, procurement, inventory management, vendor management</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">SAP SD:</strong> Sales and distribution, pricing, billing, credit management</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">SAP PP:</strong> Production planning, manufacturing execution, capacity planning</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">SAP HR/HCM:</strong> Human resources, payroll, time management, organizational management</li>
            </ul>
        </div>
        """
        st.markdown(functional_html, unsafe_allow_html=True)
    
    with col2:
        functional_details_html = """
        <div class="service-detail-card">
            <h4 style="color: #667eea !important;">SAP Modules</h4>
            <div style="margin: 1rem 0;">
                <span class="tech-badge">SAP FI</span>
                <span class="tech-badge">SAP CO</span>
                <span class="tech-badge">SAP MM</span>
                <span class="tech-badge">SAP SD</span>
                <span class="tech-badge">SAP PP</span>
                <span class="tech-badge">SAP HR</span>
                <span class="tech-badge">SAP QM</span>
                <span class="tech-badge">SAP PM</span>
                <span class="tech-badge">SAP WM</span>
                <span class="tech-badge">SAP BW</span>
            </div>
            
            <h4 style="color: #667eea !important; margin-top: 2rem;">Implementation Approach</h4>
            <ul class="feature-list">
                <li style="color: #555 !important;">Business process analysis</li>
                <li style="color: #555 !important;">Gap analysis and blueprinting</li>
                <li style="color: #555 !important;">System configuration</li>
                <li style="color: #555 !important;">Integration testing</li>
                <li style="color: #555 !important;">User training and support</li>
                <li style="color: #555 !important;">Go-live assistance</li>
            </ul>
        </div>
        """
        st.markdown(functional_details_html, unsafe_allow_html=True)

def render_genai_services():
    """Render GenAI automation services"""
    st.markdown("## 🤖 GenAI Automation Solutions")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        genai_html = """
        <div class="service-detail-card">
            <h3 style="color: #667eea !important; margin-bottom: 1.5rem;">Intelligent SAP Automation with GenAI</h3>
            <p style="font-size: 1.1rem; color: #666 !important; line-height: 1.7; margin-bottom: 2rem;">
                Transform your SAP operations with our cutting-edge GenAI automation solutions. We integrate advanced 
                AI capabilities directly into your SAP environment to automate complex processes, enhance decision-making, 
                and unlock new levels of operational efficiency.
            </p>
            
            <h4 style="color: #667eea !important; margin-bottom: 1rem;">AI-Powered Solutions:</h4>
            <ul class="feature-list">
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Intelligent Document Processing:</strong> AI-powered OCR and data extraction from invoices, POs, contracts</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Natural Language Query Interface:</strong> Ask questions about SAP data in plain language</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Automated Report Generation:</strong> AI-generated insights and executive dashboards</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Predictive Analytics:</strong> Demand forecasting, maintenance predictions, risk analysis</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Process Automation:</strong> Intelligent workflows and approval routing</li>
                <li style="color: #555 !important;"><strong style="color: #333 !important;">Anomaly Detection:</strong> Real-time monitoring and automatic issue identification</li>
            </ul>
        </div>
        """
        st.markdown(genai_html, unsafe_allow_html=True)
    
    with col2:
        genai_details_html = """
        <div class="service-detail-card">
            <h4 style="color: #667eea !important;">AI Technologies</h4>
            <div style="margin: 1rem 0;">
                <span class="tech-badge">OpenAI GPT</span>
                <span class="tech-badge">Azure OpenAI</span>
                <span class="tech-badge">Claude</span>
                <span class="tech-badge">TensorFlow</span>
                <span class="tech-badge">PyTorch</span>
                <span class="tech-badge">FastAPI</span>
                <span class="tech-badge">Streamlit</span>
                <span class="tech-badge">Vector DBs</span>
            </div>
            
            <h4 style="color: #667eea !important; margin-top: 2rem;">ROI Metrics</h4>
            <ul class="feature-list">
                <li style="color: #555 !important;">80% reduction in manual processing</li>
                <li style="color: #555 !important;">95% accuracy in data extraction</li>
                <li style="color: #555 !important;">60% faster decision-making</li>
                <li style="color: #555 !important;">40% improvement in efficiency</li>
                <li style="color: #555 !important;">$500K+ annual cost savings</li>
                <li style="color: #555 !important;">24/7 intelligent monitoring</li>
            </ul>
        </div>
        """
        st.markdown(genai_details_html, unsafe_allow_html=True)

def render_pricing_packages():
    """Render pricing packages"""
    st.markdown("## 💰 Service Packages & Pricing")
    
    col1, col2, col3 = st.columns(3)
    
    packages = [
        {
            "name": "Starter Package",
            "price": "$25K - $75K",
            "duration": "2-4 months",
            "description": "Perfect for small to medium implementations",
            "features": [
                "Single module implementation",
                "Basic ABAP development",
                "Standard reporting",
                "User training (up to 20 users)",
                "3 months post-go-live support",
                "Email & phone support"
            ],
            "color": "#4CAF50"
        },
        {
            "name": "Professional Package", 
            "price": "$75K - $200K",
            "duration": "4-8 months",
            "description": "Comprehensive solution for enterprise needs",
            "features": [
                "Multi-module implementation",
                "Custom ABAP development",
                "Advanced reporting & analytics",
                "Integration with external systems",
                "GenAI automation (basic)",
                "User training (up to 100 users)",
                "6 months post-go-live support",
                "24/7 support hotline"
            ],
            "color": "#2196F3"
        },
        {
            "name": "Enterprise Package",
            "price": "$200K+",
            "duration": "8+ months", 
            "description": "Full-scale transformation with AI integration",
            "features": [
                "Complete SAP landscape",
                "Extensive custom development",
                "Advanced GenAI integration",
                "Predictive analytics & ML",
                "Custom AI model development",
                "Unlimited user training",
                "12 months post-go-live support",
                "Dedicated support team"
            ],
            "color": "#9C27B0"
        }
    ]
    
    for i, package in enumerate(packages):
        with [col1, col2, col3][i]:
            package_html = f"""
            <div class="pricing-card" style="background: linear-gradient(135deg, {package['color']} 0%, {package['color']}aa 100%);">
                <h3 style="margin-bottom: 1rem; color: white !important;">{package['name']}</h3>
                <div style="font-size: 2rem; font-weight: bold; margin-bottom: 0.5rem; color: white !important;">{package['price']}</div>
                <div style="opacity: 0.9; margin-bottom: 1.5rem; color: white !important;">{package['duration']}</div>
                <p style="opacity: 0.9; margin-bottom: 2rem; color: white !important;">{package['description']}</p>
                <ul style="text-align: left; list-style: none; padding: 0;">
                    {''.join([f'<li style="padding: 0.3rem 0; opacity: 0.9; color: white !important;">✓ {feature}</li>' for feature in package['features']])}
                </ul>
            </div>
            """
            st.markdown(package_html, unsafe_allow_html=True)

def main():
    """Main services page function"""
    render_services_header()
    render_sap_basis_services()
    render_abap_services()
    render_functional_services()
    render_genai_services()
    render_pricing_packages()
    
    # Call-to-action
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white; margin-top: 2rem;">
        <h3 style="color: white !important;">Ready to Get Started?</h3>
        <p style="font-size: 1.1rem; margin-bottom: 1.5rem; color: white !important;">
            Contact us today for a free consultation and custom quote for your SAP project.
        </p>
        <p style="font-size: 1rem; color: white !important;">
            📧 <strong style="color: white !important;">info@sapmaster-solutions.com</strong> | 📱 <strong style="color: white !important;">+1 (555) 123-4567</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
'''

# Save updated Services.py
with open('pages/Services.py', 'w', encoding='utf-8') as f:
    f.write(services_code)

print("✅ Updated pages/Services.py with improved text visibility")