# Finally, update About.py with the same text visibility fixes

about_code = '''import streamlit as st

# Page configuration
st.set_page_config(
    page_title="About Us - SAPMaster Solutions",
    page_icon="🏢",
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
    
    .about-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .team-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        text-align: center;
        border-top: 4px solid #667eea;
    }
    
    .team-card h3, .team-card h4, .team-card h5 {
        color: #667eea !important;
    }
    
    .team-card p {
        color: #666 !important;
    }
    
    .value-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white !important;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    .value-card h3 {
        color: white !important;
    }
    
    .value-card p, .value-card ul, .value-card li {
        color: white !important;
    }
    
    .cert-badge {
        background: #667eea;
        color: white !important;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        margin: 0.25rem;
        font-size: 0.9rem;
        display: inline-block;
    }
    
    .timeline-item {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 3px 15px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
    }
    
    .timeline-item strong {
        color: #667eea !important;
    }
    
    .timeline-item p, .timeline-item {
        color: #666 !important;
    }
    
    /* General text fixes for white backgrounds */
    .white-bg-container {
        background: white;
    }
    
    .white-bg-container h1, .white-bg-container h2, .white-bg-container h3, .white-bg-container h4 {
        color: #333 !important;
    }
    
    .white-bg-container p {
        color: #666 !important;
    }
    
    .white-bg-container li {
        color: #555 !important;
    }
    
    .white-bg-container strong {
        color: #333 !important;
    }
</style>
""", unsafe_allow_html=True)

def render_about_header():
    """Render about page header"""
    header_html = """
    <div class="about-header">
        <h1 style="color: white;">About SAPMaster Solutions</h1>
        <p style="font-size: 1.3rem; opacity: 0.9; margin-bottom: 1rem; color: white;">
            Pioneering the Future of SAP Consulting with GenAI Innovation
        </p>
        <p style="font-size: 1.1rem; opacity: 0.8; color: white;">
            Over 10 years of excellence in SAP consulting, now enhanced with cutting-edge AI automation
        </p>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

def render_company_story():
    """Render company story and mission"""
    st.markdown("## 🚀 Our Story")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        story_html = """
        <div style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1); margin-bottom: 2rem;" class="white-bg-container">
            <h3 style="color: #667eea !important;">The Journey Begins</h3>
            <p style="color: #666 !important;">
                Founded in 2014 by a team of passionate SAP consultants, <strong style="color: #333 !important;">SAPMaster Solutions</strong> began with a simple yet powerful vision: 
                to bridge the gap between traditional SAP consulting and modern technological innovation. What started as a small 
                consulting firm specializing in SAP Basis and ABAP development has evolved into a leading provider of intelligent 
                SAP solutions powered by Generative AI.
            </p>
            
            <h3 style="color: #667eea !important;">Innovation at Our Core</h3>
            <p style="color: #666 !important;">
                Our founders recognized early on that the future of enterprise software lay not just in implementation and maintenance, 
                but in intelligent automation and AI-driven insights. This foresight led us to invest heavily in AI research and 
                development, making us one of the first SAP consulting firms to successfully integrate GenAI capabilities into 
                traditional SAP workflows.
            </p>
            
            <h3 style="color: #667eea !important;">Today's Excellence</h3>
            <p style="color: #666 !important;">
                Today, we serve Fortune 500 companies across multiple industries, delivering solutions that combine deep SAP expertise 
                with cutting-edge AI automation. Our unique approach has helped clients achieve an average of 40% improvement in 
                operational efficiency while reducing costs by up to 60%.
            </p>
        </div>
        """
        st.markdown(story_html, unsafe_allow_html=True)
    
    with col2:
        timeline_html = """
        <div style="background: #f8f9fa; padding: 2rem; border-radius: 15px; margin-top: 1rem;">
            <h4 style="color: #667eea !important; text-align: center;">Key Milestones</h4>
            <div class="timeline-item">
                <strong style="color: #667eea !important;">2014</strong><br>
                <span style="color: #666 !important;">Company founded with focus on SAP Basis consulting</span>
            </div>
            <div class="timeline-item">
                <strong style="color: #667eea !important;">2017</strong><br>
                <span style="color: #666 !important;">Expanded to ABAP development and functional consulting</span>
            </div>
            <div class="timeline-item">
                <strong style="color: #667eea !important;">2020</strong><br>
                <span style="color: #666 !important;">Pioneered AI integration in SAP environments</span>
            </div>
            <div class="timeline-item">
                <strong style="color: #667eea !important;">2023</strong><br>
                <span style="color: #666 !important;">Launched GenAI automation solutions</span>
            </div>
            <div class="timeline-item">
                <strong style="color: #667eea !important;">2024</strong><br>
                <span style="color: #666 !important;">150+ successful projects delivered</span>
            </div>
        </div>
        """
        st.markdown(timeline_html, unsafe_allow_html=True)

def render_mission_values():
    """Render mission, vision, and values"""
    st.markdown("## 🎯 Mission, Vision & Values")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mission_html = """
        <div class="value-card">
            <h3 style="color: white !important;">🎯 Our Mission</h3>
            <p style="color: white !important;">To empower businesses with intelligent SAP solutions that drive digital transformation, 
            optimize operations, and create sustainable competitive advantages through the seamless 
            integration of traditional consulting expertise and cutting-edge AI technology.</p>
        </div>
        """
        st.markdown(mission_html, unsafe_allow_html=True)
    
    with col2:
        vision_html = """
        <div class="value-card">
            <h3 style="color: white !important;">🔮 Our Vision</h3>
            <p style="color: white !important;">To be the global leader in AI-powered SAP consulting, setting industry standards for 
            innovation and excellence while helping organizations worldwide achieve their digital 
            transformation goals through intelligent automation.</p>
        </div>
        """
        st.markdown(vision_html, unsafe_allow_html=True)
    
    with col3:
        values_html = """
        <div class="value-card">
            <h3 style="color: white !important;">💎 Our Values</h3>
            <ul style="text-align: left; margin-top: 1rem; color: white !important;">
                <li style="color: white !important;"><strong style="color: white !important;">Innovation:</strong> Pioneering new solutions</li>
                <li style="color: white !important;"><strong style="color: white !important;">Excellence:</strong> Delivering superior quality</li>
                <li style="color: white !important;"><strong style="color: white !important;">Integrity:</strong> Honest and transparent practices</li>
                <li style="color: white !important;"><strong style="color: white !important;">Collaboration:</strong> Partnership approach</li>
                <li style="color: white !important;"><strong style="color: white !important;">Growth:</strong> Continuous learning and improvement</li>
            </ul>
        </div>
        """
        st.markdown(values_html, unsafe_allow_html=True)

def render_team_section():
    """Render team section"""
    st.markdown("## 👥 Meet Our Leadership Team")
    
    col1, col2, col3 = st.columns(3)
    
    team_members = [
        {
            "name": "Dr. Rajesh Kumar",
            "role": "Founder & CEO",
            "bio": "15+ years in SAP consulting with PhD in Computer Science. Visionary leader who pioneered our AI integration initiatives.",
            "expertise": ["Strategic Leadership", "SAP Architecture", "AI Strategy", "Digital Transformation"],
            "certifications": ["SAP Certified Solution Architect", "AWS Solutions Architect", "Google Cloud AI"]
        },
        {
            "name": "Maria Rodriguez",
            "role": "CTO & Co-Founder",
            "bio": "SAP technical expert with 12+ years experience. Leading our GenAI development and innovation lab.",
            "expertise": ["SAP Basis", "ABAP Development", "GenAI Integration", "Cloud Architecture"],
            "certifications": ["SAP Certified Technology Consultant", "Microsoft Azure AI Engineer", "SAP BTP Developer"]
        },
        {
            "name": "James Chen",
            "role": "VP of Consulting",
            "bio": "Former SAP executive with extensive functional consulting experience across multiple industries.",
            "expertise": ["SAP Functional", "Business Process", "Change Management", "Client Relations"],
            "certifications": ["SAP Certified Application Associate", "PMP", "ITIL Expert"]
        }
    ]
    
    for i, member in enumerate(team_members):
        with [col1, col2, col3][i]:
            team_card_html = f"""
            <div class="team-card">
                <div style="width: 100px; height: 100px; border-radius: 50%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                     margin: 0 auto 1rem; display: flex; align-items: center; justify-content: center; color: white; font-size: 2rem;">
                    {member['name'].split()[0][0]}{member['name'].split()[1][0]}
                </div>
                <h3 style="color: #333 !important; margin-bottom: 0.5rem;">{member['name']}</h3>
                <h4 style="color: #667eea !important; margin-bottom: 1rem;">{member['role']}</h4>
                <p style="color: #666 !important; margin-bottom: 1.5rem; line-height: 1.6;">{member['bio']}</p>
                <h5 style="color: #333 !important; margin-bottom: 0.5rem;">Expertise:</h5>
                <div style="margin-bottom: 1rem;">
                    {''.join([f'<span class="cert-badge" style="background: #4CAF50; color: white !important;">{exp}</span>' for exp in member['expertise']])}
                </div>
                <h5 style="color: #333 !important; margin-bottom: 0.5rem;">Certifications:</h5>
                <div>
                    {''.join([f'<span class="cert-badge">{cert}</span>' for cert in member['certifications']])}
                </div>
            </div>
            """
            st.markdown(team_card_html, unsafe_allow_html=True)

def render_expertise_section():
    """Render our expertise and capabilities"""
    st.markdown("## 🛠️ Our Expertise & Capabilities")
    
    tab1, tab2, tab3 = st.tabs(["🔧 Technical Skills", "🏢 Industry Experience", "🎓 Certifications"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            tech_html = """
            <div style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1);" class="white-bg-container">
                <h3 style="color: #667eea !important;">SAP Technical Expertise</h3>
                <ul>
                    <li style="color: #555 !important;"><strong style="color: #333 !important;">SAP Basis Administration:</strong> Complete system landscape management</li>
                    <li style="color: #555 !important;"><strong style="color: #333 !important;">ABAP Development:</strong> Custom development and optimization</li>
                    <li style="color: #555 !important;"><strong style="color: #333 !important;">SAP HANA:</strong> Database administration and optimization</li>
                    <li style="color: #555 !important;"><strong style="color: #333 !important;">SAP BTP:</strong> Cloud platform development and integration</li>
                    <li style="color: #555 !important;"><strong style="color: #333 !important;">S/4HANA:</strong> Migration and implementation expertise</li>
                </ul>
                
                <h3 style="color: #667eea !important;">GenAI & Modern Technologies</h3>
                <ul>
                    <li style="color: #555 !important;"><strong style="color: #333 !important;">Machine Learning:</strong> Custom AI model development</li>
                    <li style="color: #555 !important;"><strong style="color: #333 !important;">Natural Language Processing:</strong> Document processing and chatbots</li>
                    <li style="color: #555 !important;"><strong style="color: #333 !important;">Cloud Platforms:</strong> AWS, Azure, Google Cloud</li>
                    <li style="color: #555 !important;"><strong style="color: #333 !important;">DevOps:</strong> CI/CD, containerization, automation</li>
                    <li style="color: #555 !important;"><strong style="color: #333 !important;">APIs & Integration:</strong> RESTful services, middleware</li>
                </ul>
            </div>
            """
            st.markdown(tech_html, unsafe_allow_html=True)
        
        with col2:
            tech_stack_html = """
            <div style="background: #f8f9fa; padding: 2rem; border-radius: 15px;">
                <h4 style="color: #667eea !important; text-align: center; margin-bottom: 1.5rem;">Technology Stack</h4>
                <div style="text-align: center;">
                    <span class="cert-badge">SAP ERP</span>
                    <span class="cert-badge">SAP S/4HANA</span>
                    <span class="cert-badge">SAP BTP</span>
                    <span class="cert-badge">SAP HANA</span>
                    <span class="cert-badge">ABAP</span>
                    <span class="cert-badge">Python</span>
                    <span class="cert-badge">OpenAI</span>
                    <span class="cert-badge">TensorFlow</span>
                    <span class="cert-badge">PyTorch</span>
                    <span class="cert-badge">Streamlit</span>
                    <span class="cert-badge">FastAPI</span>
                    <span class="cert-badge">Docker</span>
                    <span class="cert-badge">Kubernetes</span>
                    <span class="cert-badge">AWS</span>
                    <span class="cert-badge">Azure</span>
                    <span class="cert-badge">Google Cloud</span>
                </div>
            </div>
            """
            st.markdown(tech_stack_html, unsafe_allow_html=True)
    
    with tab2:
        col1, col2, col3 = st.columns(3)
        
        industries = [
            {
                "name": "Manufacturing",
                "icon": "🏭",
                "projects": 45,
                "specialties": ["Production Planning", "Quality Management", "Supply Chain", "Industry 4.0"]
            },
            {
                "name": "Financial Services",
                "icon": "🏦", 
                "projects": 38,
                "specialties": ["Core Banking", "Risk Management", "Compliance", "Digital Banking"]
            },
            {
                "name": "Healthcare",
                "icon": "🏥",
                "projects": 25,
                "specialties": ["Patient Management", "Medical Records", "Compliance", "Analytics"]
            }
        ]
        
        for i, industry in enumerate(industries):
            with [col1, col2, col3][i]:
                industry_html = f"""
                <div style="background: white; padding: 1.5rem; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1); text-align: center;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">{industry['icon']}</div>
                    <h3 style="color: #667eea !important;">{industry['name']}</h3>
                    <p style="color: #666 !important; margin-bottom: 1rem;"><strong style="color: #333 !important;">{industry['projects']} projects completed</strong></p>
                    <h5 style="color: #333 !important;">Specialties:</h5>
                    <div>
                        {''.join([f'<span class="cert-badge" style="background: #4CAF50; margin: 0.2rem; font-size: 0.8rem;">{spec}</span>' for spec in industry['specialties']])}
                    </div>
                </div>
                """
                st.markdown(industry_html, unsafe_allow_html=True)
    
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            cert_html = """
            <div style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1);" class="white-bg-container">
                <h3 style="color: #667eea !important;">SAP Certifications</h3>
                <ul>
                    <li style="color: #555 !important;">SAP Certified Technology Consultant - SAP Basis</li>
                    <li style="color: #555 !important;">SAP Certified Development Specialist - ABAP for SAP HANA</li>
                    <li style="color: #555 !important;">SAP Certified Application Associate - SAP S/4HANA</li>
                    <li style="color: #555 !important;">SAP Certified Solution Architect - SAP BTP</li>
                    <li style="color: #555 !important;">SAP Certified Technology Associate - SAP HANA 2.0</li>
                </ul>
            </div>
            """
            st.markdown(cert_html, unsafe_allow_html=True)
        
        with col2:
            ai_cert_html = """
            <div style="background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.1);" class="white-bg-container">
                <h3 style="color: #667eea !important;">AI & Cloud Certifications</h3>
                <ul>
                    <li style="color: #555 !important;">Microsoft Azure AI Engineer Associate</li>
                    <li style="color: #555 !important;">AWS Certified Machine Learning - Specialty</li>
                    <li style="color: #555 !important;">Google Cloud Professional Machine Learning Engineer</li>
                    <li style="color: #555 !important;">TensorFlow Developer Certificate</li>
                    <li style="color: #555 !important;">OpenAI API Specialist</li>
                </ul>
            </div>
            """
            st.markdown(ai_cert_html, unsafe_allow_html=True)

def main():
    """Main about page function"""
    render_about_header()
    render_company_story()
    render_mission_values()
    render_team_section()
    render_expertise_section()
    
    # Call-to-action
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white; margin-top: 2rem;">
        <h3 style="color: white !important;">Ready to Start Your SAP Transformation Journey?</h3>
        <p style="font-size: 1.1rem; margin-bottom: 1.5rem; color: white !important;">
            Partner with SAPMaster Solutions for innovative SAP consulting and GenAI automation that delivers real results.
        </p>
        <p style="font-size: 1rem; color: white !important;">
            📧 <strong style="color: white !important;">info@sapmaster-solutions.com</strong> | 📱 <strong style="color: white !important;">+1 (555) 123-4567</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
'''

# Save updated About.py
with open('pages/About.py', 'w', encoding='utf-8') as f:
    f.write(about_code)

print("✅ Updated pages/About.py with improved text visibility")
print("\n🎨 Text Visibility Issues Fixed:")
print("   ✓ All white background cards now have dark text (#333, #666, #555)")
print("   ✓ Added !important declarations to override default Streamlit styling")
print("   ✓ Improved contrast ratios for better readability")
print("   ✓ Fixed header colors and strong text visibility")
print("   ✓ Enhanced list item and paragraph text contrast")
print("   ✓ Updated all gradient cards to maintain white text on colored backgrounds")
print("\n🚀 Ready to test! Run: streamlit run app.py")
print("📍 Navigate between pages using the sidebar to see the improvements")