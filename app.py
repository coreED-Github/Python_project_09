from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "saira.jpg"

PAGE_TITLE = "Digital CV | Saira"
PAGE_ICON = ":wave:"
NAME = "Saira"
DESCRIPTION = "School Principal | Math Teacher | E-Commerce Developer | Programer | Freelancer"
EMAIL = "sairanasir853@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/saira-nasir-935bb1230?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
    "GitHub": "https://github.com/coreED-Github",
    "Facebook":"https://www.facebook.com/share/1ALRVFEn2n/",

}
PROJECTS = {
    "🏆E-Commerce Marketplace with Sanity CMS & Next.js": "https://marketplace-home-store-ecommerce-website.vercel.app/",
    "🏆E-Commerce website with Sanity CMS & Next.js": "https://e-commerce-website-practise.vercel.app/",
    "🏆E-Commerce website with Next.js & tailwind CSS": "https://chocolate-cake-shop.vercel.app/",
    "🏆My Portfolio with Tailwind Css & Next.js": "https://my-portolio-project.vercel.app/",
    "🏆API Integration country info Website with Nextjs and API's": "classassignment-15-country.vercel.app",
    "🏆 Resume builder using HTML and CSS":"https://resume-builder-005.vercel.app/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


st.sidebar.title("Saira Nasir Portfolio")
nav_selection = st.sidebar.radio("Go to", ["Home", "Education", "Skills", "Experience", "Projects", "Contact"])

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


if nav_selection == "Home":
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
            # mime="application/pdf"
            
        )
        st.write("📫", EMAIL)

    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

if nav_selection == "Education":
    st.subheader("Education")
    st.write("---")
    st.write(
        """
- 🎓 *Bechelor Of Commercr* - Karachi University
- 📍 Location: Karachi, Pakistan
- 🗓 Duration: 2021 - 2024
"""
    )


if nav_selection == "Skills":
    st.subheader("Technical Skills")
    st.write("---")
    st.write(
        """
- 👩‍💻 *Programming*: Python, SQL, JavaScript , TypeScript , Next.js, React, HTML, CSS
- 📊 *Data Science*: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- ☁ *CMS & APIs*: Sanity CMS, EasyPost, Shippo, AliExpress APIs
- 🎨 *Frontend*: TailwindCSS, Responsive Design
- 🧪 *Testing*: Cypress, UAT, Lighthouse Audits
"""
    )

if nav_selection == "Experience":
    st.subheader("Experience")
    st.write("---")
    st.write("🚧 School Principal | Math Teacher")
    st.write("2018 - Present")
    st.write("- Teaching Data Science & mentoring students in real-world projects.")

    st.write('\n')
    st.write("🚧 Freelance Developer | E-Commerce Projects")
    st.write("2024 - Present")
    st.write(
        """
- Built and deployed marketplace platforms using Next.js & Sanity CMS.
- Integrated dynamic shipment tracking APIs and performed UAT for clients.
"""
    )

if nav_selection == "Projects":
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

if nav_selection == "Contact":
    st.subheader("Get in Touch")
    st.write("---")
    st.write(f"📫 Email: {EMAIL}")
    st.write("phone: 03492908035")
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
    st.write("Feel free to reach out for collaborations, mentorship, or freelance work!")

st.markdown("""
<hr style='border:1px solid #ccc'/>
<div style='text-align:center; color:gray; font-size: small;'>
    Built with ❤ by Saira | © 2025
</div>
""", unsafe_allow_html=True)
print("Resume size:" , resume_file.stat().st_size)