import webbrowser
import streamlit as st
import streamlit_shadcn_ui as ui


st.set_page_config(page_icon="🧬", #set the page favicon
                   layout="wide", #centered or wide
                   page_title="Durga Venu Kumar Mutyala", #tab name
                
                   )
# Set meta data
st.markdown(
    """
    <head>
        <title>Durga Venu Kumar Mutyala</title>
        <meta name="description" content="This is my portfolio. My name is Durga Venu Kumar Mutyala, an aspirig Gen AI Engineer.">
        <meta name="keywords" content="streamlit, python, Generative ai, Durga Venu Kumar Mutyala, Veddy AI, Firenation">
    </head>
    """,
    unsafe_allow_html=True
)


st.title("Durga Venu Kumar Mutyala", anchor=False)
st.subheader("🔥 Aspriring Generative AI Engineer", anchor=False)

#NAVIGATION
about, e1, skills, e2, projects, e3, publications, e4, contact, e5= st.tabs(["About","|", "Skills", "|","Projects","|", "Publications","|", "Get in Touch", "|"])



# About Section
with about:
    # About Me section
    st.toast("Welcome, To my Portfolio", icon="✅")
    about, empty = st.columns([3,1])
    with about:
        st.subheader("👋 Hey there, Venu Kumar here!", anchor=False)
        st.subheader("I'm a tech-savvy 🤖 chameleon always leveling up my skills. When I'm not crushing it in AI and coding, you can find me exploring the latest gadgets 🤖 or getting lost in a good book 📚.", anchor=False)
        ui.tabs(options=['Feel free to Navigate and Contact Me'], default_value='Feel free to Navigate and Contact Me', key=None)
    # Resume

    # Read the PDF file
    # Read the PDF file
    with open("Durga Venu Kumar Mutyala AI.pdf", "rb") as file:
        pdf_contents = file.read()

    # Create the download button
    st.button(on_click="https://www.linkedin.com/in/venukumarmd",label="Linkedin")
    st.download_button("Get My Resume", pdf_contents, file_name="Durga Venu Kumar Mutyala.pdf", mime="application/pdf")

# Skills Section
with skills:
    st.subheader("Explore My Abilities", anchor=False)
    cols = st.columns(3)
    with cols[0]:
        ui.metric_card(title="Programming", content="Python, Java", description="", key=1)
        ui.metric_card(title="Libraries", content="Pandas, Numpy", description="", key="4")
   
    with cols[1]:
        ui.metric_card(title="Frameworks", content="Flask, Django, Streamlit", description="", key=2)
        ui.metric_card(title="LLM I use", content="Gemini, Groq, Open AI ", description="", key="card3")
   
        
    with cols[2]:
        ui.metric_card(title="Databases", content="SQL, SQLite3", description="", key=3)

        ui.metric_card(title="Gen AI Frameworks", content="LangChain, Crew AI", description="", key=6)
   

#Projects Section
with projects:
    st.subheader("Explore my Work",anchor=False)

    col = st.columns(3) # Divide the page into three columns

    with col[0]:
        st.subheader("FarmFlow AI", anchor=False)
        if st.button("See Here 1", key="button1"):
            webbrowser.open_new_tab("https://farmflow-ai.onrender.com/")
        with st.expander("Know More"):
            st.markdown("A Data Science Project that allows farmers to know what type of plants are suitable to grow in their field by taking some soil parameters")
            ui.badges(badge_list=[("Python", "destructive"), ("HTML", "destructive"), ("CSS", "destructive"), ("Kaggle-Dataset", "destructive")], class_name="flex gap-2", key="badges1")

        with col[1]:
            st.subheader("Veddy AI",anchor=False)
            if st.button("See Here 2", key="button2"):
                webbrowser.open_new_tab("https://firenationai-code.streamlit.app/")
            with st.expander("Know More"):
                st.markdown("Elevate your code with intelligent suggestions, real-time assistance, and the power of Google's Gemini API. Your seamless path to coding excellence.")
                ui.badges(badge_list=[("Python", "destructive"), ("HTML", "destructive"), ("Streamlit", "destructive"), ("Gemini Pro", "destructive")], class_name="flex gap-2", key="badges2")

        with col[2]:
            st.subheader("Resumer AI",anchor=False)
            if st.button("See Here 3", key="button3"):
                webbrowser.open_new_tab("https://resumer-ai.streamlit.app/")
            with st.expander("Know More"):
                st.markdown("Powerful tool that leverages the capabilities of Streamlit to help you create a standout resume and improve your job prospects.")
                ui.badges(badge_list=[("Python", "destructive"), ("Streamlit", "destructive"), ("Gemini AI", "destructive"), ("Gemini Vision", "destructive")], class_name="flex gap-2", key="badges3")
        
    pol = st.columns(3)

    with pol[0]:
        st.subheader("Swachh Jalam AI",anchor=False)
        if st.button("See Here 4"):
            webbrowser.open_new_tab("https://waterprediction.streamlit.app/")

        with st.expander("Know More"):
            st.markdown("An interactive tool designed to help to understand and predict the quality of groundwater in different locations, determining the suitability of water for drinking.")
            ui.badges(badge_list=[("Python", "destructive"), ("Streamlit", "destructive"), ("Machine Learning", "destructive"), ("Kaggle-Dataset", "destructive")], class_name="flex gap-2", key="badges4")

    with pol[1]:
        st.subheader("Student Management Portal",anchor=False)
        if st.button("See Here 5"):
            webbrowser.open_new_tab("https://ucststudentmanagement.streamlit.app/")
        with st.expander("Know More"):
            st.markdown("app serves as a basic tool for efficiently managing and maintaining student records within an educational institution offering a user-friendly interface and basic functionalities. ")
            ui.badges(badge_list=[("Python", "destructive"), ("Pandas", "destructive"), ("Streamlit", "destructive"), ("Drag & Drop", "destructive"), ("JSON", "destructive")], class_name="flex gap-2", key="badges5")

    with pol[2]:
        st.subheader("Green AI",anchor=False)
        if st.button("See Here 6"):
            webbrowser.open_new_tab("https://paddydiagnosis.streamlit.app/")

        with st.expander("Know More"):
            st.markdown("serves as a helpful resource for farmers by providing them with a user-friendly tool to diagnose disease-related problems in rice cultivation more effectively.")
            ui.badges(badge_list=[("Python", "destructive"), ("Machine Learning", "destructive"), ("Streamlit", "destructive"), ("Kaggle-Dataset", "destructive")], class_name="flex gap-2", key="badges6")

    mol = st.columns(3)
    with mol[0]:
        st.subheader("ChatPDF AI",anchor=False)
        if st.button("See Here 7"):
            webbrowser.open_new_tab("https://veddyai-pdf.streamlit.app/")

        with st.expander("Know More"):
            st.markdown("A useful tool for individuals that process and analyze data from PDF documents, particularly when it comes to extracting text content for further analysis or usage.")
            ui.badges(badge_list=[("Python", "destructive"), ("Gemini Pro", "destructive"), ("Streamlit", "destructive"), ("FAISS", "destructive"), ("PDF", "destructive")], class_name="flex gap-2", key="badges7")

    with mol[1]:
        st.subheader("Just Add",anchor=False)
        if st.button("See Here 8"):
            webbrowser.open_new_tab("https://pro1vk.web.app/")
        
        with st.expander("Know More"):
            st.markdown("A progressive Web App that allows users to add things like to-do and then just on a tap it stores in the database and and on click it removes them.")
            ui.badges(badge_list=[("HTML", "destructive"), ("CSS", "destructive"), ("Firebase", "destructive")], class_name="flex gap-2", key="badges8")


    with mol[2]:
        st.subheader("Pokemon Game",anchor=False)
        if st.button("See Here 9"):
            webbrowser.open_new_tab("https://cardgamer786.web.app/")
        with st.expander("Know More"):
            st.markdown("A Progressive Web App that allows users to play Pokemon Game just by generating and firing a character card and competing with friends.")
            ui.badges(badge_list=[("HTML", "destructive"), ("CSS", "destructive"), ("Pokemon API", "destructive"), ("Firebase", "destructive")], class_name="flex gap-2", key="badges9")

#publications
with publications:
    st.subheader("My Contributions", anchor=False)
    st.subheader("Flipkart-Scraper", anchor=False)
    col = st.columns([2,1])
    with col[0]:
        st.markdown("Flipkart Scraper is a Python library designed for extracting detailed product information from Flipkart. This library utilizes web scraping techniques to gather data such as title, price, rating, number of reviews, and description from a given Flipkart product URL.")
        st.code("pip install flipkart-scraper")
    with st.expander("Know More"):
        st.subheader("Sample implementation with Streamlit.", anchor=False)
        st.code("""
# Import necessary libraries
import streamlit as st
from thevk.flipkartscraper import FlipkartScraper

# Define the main function to display the Flipkart product information
def main():
    # Set the title of the Streamlit app
    st.title("Flipkart Product Scraper")

    # Define the URL of the Flipkart product you want to scrape
    url = "https://www.flipkart.com/some-product"

    # Initialize the FlipkartScraper with the provided URL
    scraper = FlipkartScraper(url)

    # Get the title of the product
    title = scraper.get_title()

    # Get the price of the product
    price = scraper.get_price()

    # Get the rating of the product
    rating = scraper.get_rating()

    # Get the number of reviews for the product
    num_reviews = scraper.get_num_reviews()

    # Get the description of the product
    description = scraper.get_description()

    # Display the scraped information using Streamlit
    st.write("Title:", title)
    st.write("Price:", price)
    st.write("Rating:", rating)
    st.write("Number of Reviews:", num_reviews)
    st.write("Description:", description)

# Run the Streamlit app
if __name__ == "__main__":
    main()

""")


    ui.tabs(options=["Dont't forget to play with the library"], default_value="Dont't forget to play with the library", key=None)
    if st.button("Check detailed Documentation here", key="button11"):
            webbrowser.open_new_tab("https://pypi.org/project/flipkart-scraper/")

with contact:

    st.subheader("Contact Me")

    st.write("Feel free to reach out to me via email or connect with me on social media.")

    st.write("📧 Email: [venukumarmd03@gmail.com](mailto:venukumarmd03@gmail.com)")

    st.write("Connect with me on social media:")
    st.markdown("➡️ LinkedIn: [https://www.linkedin.com/in/venukumarmd](https://www.linkedin.com/in/venukumarmd)")
    st.markdown("➡️ Instagram: [https://www.instagram.com/_the_vk.__/](https://www.instagram.com/_the_vk.__/)")
    st.markdown("➡️ GitHub: [https://github.com/mdvenukumar](https://github.com/mdvenukumar)")