# Create a Services page with detailed service information
services_code = '''import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Services - SAPMaster Solutions",
    page_icon="⚙️",
    layout="wide"
)

# Custom CSS
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
    
    .pricing-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .process-step {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        border-left: 4px solid #4CAF50;
    }
    
    .tech-badge {
        background: #667eea;
        color: white;
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
    }
    
    .feature-list li:before {
        content: "✓";
        position: absolute;
        left: 0;
        color: #4CAF50;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def render_services_header():
    """Render services page header"""
    header_html = """
    <div class="services-header">
        <h1>Our Services</h1>
        <p style="font-size: 1.3rem; opacity: 0.9; margin-bottom: 1rem;">
            Comprehensive SAP Consulting & GenAI Automation Solutions
        </p>
        <p style="font-size: 1.1rem; opacity: 0.8;">
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
            <h3 style="color: #667eea; margin-bottom: 1.5rem;">Complete SAP Basis Lifecycle Management</h3>
            <p style="font-size: 1.1rem; color: #666; line-height: 1.7; margin-bottom: 2rem;">
                Our SAP Basis experts provide comprehensive system administration services to ensure your SAP landscape 
                runs optimally, securely, and efficiently. From initial setup to ongoing maintenance, we handle all 
                technical aspects of your SAP environment.
            </p>
            
            <h4 style="color: #667eea; margin-bottom: 1rem;">Core Services Include:</h4>
            <ul class="feature-list">
                <li><strong>System Installation & Configuration:</strong> Complete SAP system setup with best practices</li>
                <li><strong>Performance Monitoring & Tuning:</strong> Proactive monitoring with automated alerts</li>
                <li><strong>Security Implementation:</strong> User management, authorization concepts, and compliance</li>
                <li><strong>Backup & Recovery:</strong> Comprehensive disaster recovery planning and implementation</li>
                <li><strong>System Upgrades:</strong> Zero-downtime upgrades and patches</li>
                <li><strong>Transport Management:</strong> Streamlined change management processes</li>
                <li><strong>Database Administration:</strong> HANA, Oracle, SQL Server optimization</li>
                <li><strong>High Availability Setup:</strong> Clustering and failover configuration</li>
            </ul>
        </div>
        """
        st.markdown(basis_html, unsafe_allow_html=True)
    
    with col2:
        basis_details_html = """
        <div class="service-detail-card">
            <h4 style="color: #667eea;">Technologies We Support</h4>
            <div style="margin: 1rem 0;">
                <span class="tech-badge">SAP NetWeaver</span>
                <span class="tech-badge">SAP HANA</span>
                <span class="tech-badge">SAP S/4HANA</span>
                <span class="tech-badge">SAP BW</span>
                <span class="tech-badge">SAP PI/PO</span>
                <span class="tech-badge">SAP Solution Manager</span>
                <span class="tech-badge">Linux</span>
                <span class="tech-badge">Windows</span>
                <span class="tech-badge">AIX</span>
                <span class="tech-badge">Oracle</span>
                <span class="tech-badge">SQL Server</span>
                <span class="tech-badge">DB2</span>
            </div>
            
            <h4 style="color: #667eea; margin-top: 2rem;">Key Benefits</h4>
            <ul class="feature-list">
                <li>99.9% system uptime guarantee</li>
                <li>30% reduction in maintenance costs</li>
                <li>Automated monitoring and alerting</li>
                <li>24/7 expert support</li>
                <li>Compliance with security standards</li>
                <li>Proactive performance optimization</li>
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
            <h3 style="color: #667eea; margin-bottom: 1.5rem;">Custom ABAP Development & Optimization</h3>
            <p style="font-size: 1.1rem; color: #666; line-height: 1.7; margin-bottom: 2rem;">
                Our certified ABAP developers create high-performance, scalable solutions tailored to your business needs. 
                From simple reports to complex enterprise applications, we deliver clean, maintainable code that follows 
                SAP best practices and modern development standards.
            </p>
            
            <h4 style="color: #667eea; margin-bottom: 1rem;">Development Services:</h4>
            <ul class="feature-list">
                <li><strong>Custom Reports & Forms:</strong> Classical and ALV reports, Adobe Forms, Smart Forms</li>
                <li><strong>Interface Development:</strong> RFC, IDoc, web services, API integrations</li>
                <li><strong>Enhancement & Modifications:</strong> User exits, customer exits, enhancement framework</li>
                <li><strong>Object-Oriented Programming:</strong> Classes, methods, inheritance, polymorphism</li>
                <li><strong>Web Development:</strong> Web Dynpro ABAP, BSP, REST services</li>
                <li><strong>Workflow Development:</strong> Business workflow automation and approval processes</li>
                <li><strong>Performance Optimization:</strong> Code review, SQL optimization, memory management</li>
                <li><strong>Migration & Conversion:</strong> Data migration tools and conversion programs</li>
            </ul>
        </div>
        """
        st.markdown(abap_html, unsafe_allow_html=True)
    
    with col2:
        abap_details_html = """
        <div class="service-detail-card">
            <h4 style="color: #667eea;">ABAP Expertise Areas</h4>
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
                <span class="tech-badge">AMDP</span>
                <span class="tech-badge">REST/OData</span>
            </div>
            
            <h4 style="color: #667eea; margin-top: 2rem;">Performance Metrics</h4>
            <ul class="feature-list">
                <li>75% faster code execution</li>
                <li>50% reduction in development time</li>
                <li>95% code quality score</li>
                <li>Zero critical bugs in production</li>
                <li>Comprehensive documentation</li>
                <li>Knowledge transfer included</li>
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
            <h3 style="color: #667eea; margin-bottom: 1.5rem;">End-to-End Functional Implementation</h3>
            <p style="font-size: 1.1rem; color: #666; line-height: 1.7; margin-bottom: 2rem;">
                Our functional consultants bring deep business process knowledge and extensive SAP module expertise 
                to optimize your operations. We analyze your requirements, design efficient processes, and implement 
                solutions that drive business value and operational excellence.
            </p>
            
            <h4 style="color: #667eea; margin-bottom: 1rem;">Functional Areas:</h4>
            <ul class="feature-list">
                <li><strong>SAP FI/CO:</strong> Financial accounting, controlling, asset management, profitability analysis</li>
                <li><strong>SAP MM:</strong> Materials management, procurement, inventory management, vendor management</li>
                <li><strong>SAP SD:</strong> Sales and distribution, pricing, billing, credit management</li>
                <li><strong>SAP PP:</strong> Production planning, manufacturing execution, capacity planning</li>
                <li><strong>SAP HR/HCM:</strong> Human resources, payroll, time management, organizational management</li>
                <li><strong>SAP QM:</strong> Quality management, inspections, certificates, audits</li>
                <li><strong>SAP PM:</strong> Plant maintenance, work orders, preventive maintenance</li>
                <li><strong>SAP WM/EWM:</strong> Warehouse management, extended warehouse management</li>
            </ul>
        </div>
        """
        st.markdown(functional_html, unsafe_allow_html=True)
    
    with col2:
        functional_details_html = """
        <div class="service-detail-card">
            <h4 style="color: #667eea;">SAP Modules</h4>
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
                <span class="tech-badge">SAP PS</span>
                <span class="tech-badge">SAP BW</span>
                <span class="tech-badge">SAP CRM</span>
            </div>
            
            <h4 style="color: #667eea; margin-top: 2rem;">Implementation Approach</h4>
            <ul class="feature-list">
                <li>Business process analysis</li>
                <li>Gap analysis and blueprinting</li>
                <li>System configuration</li>
                <li>Integration testing</li>
                <li>User training and support</li>
                <li>Go-live assistance</li>
                <li>Post-implementation optimization</li>
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
            <h3 style="color: #667eea; margin-bottom: 1.5rem;">Intelligent SAP Automation with GenAI</h3>
            <p style="font-size: 1.1rem; color: #666; line-height: 1.7; margin-bottom: 2rem;">
                Transform your SAP operations with our cutting-edge GenAI automation solutions. We integrate advanced 
                AI capabilities directly into your SAP environment to automate complex processes, enhance decision-making, 
                and unlock new levels of operational efficiency.
            </p>
            
            <h4 style="color: #667eea; margin-bottom: 1rem;">AI-Powered Solutions:</h4>
            <ul class="feature-list">
                <li><strong>Intelligent Document Processing:</strong> AI-powered OCR and data extraction from invoices, POs, contracts</li>
                <li><strong>Natural Language Query Interface:</strong> Ask questions about SAP data in plain language</li>
                <li><strong>Automated Report Generation:</strong> AI-generated insights and executive dashboards</li>
                <li><strong>Predictive Analytics:</strong> Demand forecasting, maintenance predictions, risk analysis</li>
                <li><strong>Process Automation:</strong> Intelligent workflows and approval routing</li>
                <li><strong>Anomaly Detection:</strong> Real-time monitoring and automatic issue identification</li>
                <li><strong>Chatbot Integration:</strong> AI assistants for user support and system interaction</li>
                <li><strong>Smart Recommendations:</strong> AI-driven suggestions for optimization and cost savings</li>
            </ul>
        </div>
        """
        st.markdown(genai_html, unsafe_allow_html=True)
    
    with col2:
        genai_details_html = """
        <div class="service-detail-card">
            <h4 style="color: #667eea;">AI Technologies</h4>
            <div style="margin: 1rem 0;">
                <span class="tech-badge">OpenAI GPT</span>
                <span class="tech-badge">Azure OpenAI</span>
                <span class="tech-badge">Claude</span>
                <span class="tech-badge">LangChain</span>
                <span class="tech-badge">TensorFlow</span>
                <span class="tech-badge">PyTorch</span>
                <span class="tech-badge">Hugging Face</span>
                <span class="tech-badge">spaCy</span>
                <span class="tech-badge">scikit-learn</span>
                <span class="tech-badge">FastAPI</span>
                <span class="tech-badge">Streamlit</span>
                <span class="tech-badge">Vector DBs</span>
            </div>
            
            <h4 style="color: #667eea; margin-top: 2rem;">ROI Metrics</h4>
            <ul class="feature-list">
                <li>80% reduction in manual processing</li>
                <li>95% accuracy in data extraction</li>
                <li>60% faster decision-making</li>
                <li>40% improvement in efficiency</li>
                <li>$500K+ annual cost savings</li>
                <li>24/7 intelligent monitoring</li>
            </ul>
        </div>
        """
        st.markdown(genai_details_html, unsafe_allow_html=True)

def render_implementation_process():
    """Render implementation process"""
    st.markdown("## 🔄 Our Implementation Process")
    
    process_steps = [
        {
            "step": "1",
            "title": "Discovery & Assessment",
            "description": "Comprehensive analysis of your current SAP landscape, business processes, and AI readiness",
            "duration": "2-4 weeks",
            "deliverables": ["Current state assessment", "Gap analysis", "AI opportunity identification", "Project roadmap"]
        },
        {
            "step": "2", 
            "title": "Solution Design",
            "description": "Detailed technical and functional design of the optimal solution architecture",
            "duration": "3-6 weeks",
            "deliverables": ["Solution blueprint", "Technical architecture", "Integration design", "AI model specifications"]
        },
        {
            "step": "3",
            "title": "Development & Configuration",
            "description": "Implementation of SAP configurations, custom development, and AI model integration",
            "duration": "8-16 weeks",
            "deliverables": ["Configured system", "Custom developments", "AI models", "Integration components"]
        },
        {
            "step": "4",
            "title": "Testing & Validation", 
            "description": "Comprehensive testing including unit, integration, performance, and user acceptance testing",
            "duration": "4-8 weeks",
            "deliverables": ["Test results", "Performance reports", "User training materials", "Go-live checklist"]
        },
        {
            "step": "5",
            "title": "Deployment & Go-Live",
            "description": "Careful deployment with minimal business disruption and comprehensive go-live support",
            "duration": "2-4 weeks", 
            "deliverables": ["Production deployment", "Go-live support", "Issue resolution", "Performance monitoring"]
        },
        {
            "step": "6",
            "title": "Support & Optimization",
            "description": "Ongoing support, monitoring, and continuous optimization for sustained success",
            "duration": "Ongoing",
            "deliverables": ["24/7 monitoring", "Regular optimization", "Performance reports", "Enhancement recommendations"]
        }
    ]
    
    col1, col2 = st.columns(2)
    
    for i, step in enumerate(process_steps):
        with col1 if i % 2 == 0 else col2:
            step_html = f"""
            <div class="process-step">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div style="width: 40px; height: 40px; border-radius: 50%; background: #4CAF50; color: white; 
                         display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 1rem;">
                        {step['step']}
                    </div>
                    <h4 style="color: #333; margin: 0;">{step['title']}</h4>
                </div>
                <p style="color: #666; margin-bottom: 1rem; line-height: 1.6;">{step['description']}</p>
                <div style="margin-bottom: 1rem;">
                    <strong style="color: #667eea;">Duration:</strong> {step['duration']}
                </div>
                <div>
                    <strong style="color: #667eea;">Key Deliverables:</strong>
                    <ul style="margin-top: 0.5rem; color: #666;">
                        {''.join([f'<li>{deliverable}</li>' for deliverable in step['deliverables']])}
                    </ul>
                </div>
            </div>
            """
            st.markdown(step_html, unsafe_allow_html=True)

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
                "Dedicated support team",
                "Ongoing optimization services"
            ],
            "color": "#9C27B0"
        }
    ]
    
    for i, package in enumerate(packages):
        with [col1, col2, col3][i]:
            package_html = f"""
            <div class="pricing-card" style="background: linear-gradient(135deg, {package['color']} 0%, {package['color']}aa 100%);">
                <h3 style="margin-bottom: 1rem;">{package['name']}</h3>
                <div style="font-size: 2rem; font-weight: bold; margin-bottom: 0.5rem;">{package['price']}</div>
                <div style="opacity: 0.9; margin-bottom: 1.5rem;">{package['duration']}</div>
                <p style="opacity: 0.9; margin-bottom: 2rem;">{package['description']}</p>
                <ul style="text-align: left; list-style: none; padding: 0;">
                    {''.join([f'<li style="padding: 0.3rem 0; opacity: 0.9;">✓ {feature}</li>' for feature in package['features']])}
                </ul>
            </div>
            """
            st.markdown(package_html, unsafe_allow_html=True)
    
    # Additional pricing information
    st.markdown("### 📝 Pricing Notes")
    st.markdown("""
    - **Flexible Pricing:** All packages can be customized based on your specific requirements
    - **Phased Approach:** Large projects can be broken into phases for better budget management
    - **ROI Guarantee:** We work with you to ensure measurable return on investment
    - **Maintenance Packages:** Optional ongoing support packages available starting at $5K/month
    - **Training Programs:** Additional training sessions available at $2K/day per trainer
    """)

def main():
    """Main services page function"""
    render_services_header()
    render_sap_basis_services()
    render_abap_services()
    render_functional_services()
    render_genai_services()
    render_implementation_process()
    render_pricing_packages()
    
    # Call-to-action
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white; margin-top: 2rem;">
        <h3>Ready to Get Started?</h3>
        <p style="font-size: 1.1rem; margin-bottom: 1.5rem;">
            Contact us today for a free consultation and custom quote for your SAP project.
        </p>
        <p style="font-size: 1rem;">
            📧 <strong>info@sapmaster-solutions.com</strong> | 📱 <strong>+1 (555) 123-4567</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
'''

# Save the services page
with open('pages/Services.py', 'w', encoding='utf-8') as f:
    f.write(services_code)

print("✅ Created pages/Services.py - Detailed Services page")