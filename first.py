import streamlit as st

#Header of the application
st.header("Students Record Management")

#Title of teh application
st.title("Student Management System")
st.header("By Sarika Devarajan")

#Subheader of the application
st.subheader("Manage student records with Create, Read, Update, and Delete operations")

#horizontal line
st.markdown("--------------------------------------------------------")

#text information
st.text("This application allows you to manage student records using a simple interface. You can create new records, read existing ones, update them, or delete them as needed.")

#Write method to display additional information
st.write("Hello Streamlit")
st.write(123)
st.write("**Features of the Application:**")
st.markdown("*- Create new student records*")
st.markdown("*- Read existing student records*")
st.markdown("*- Update student records*")
st.markdown("*- Delete student records*")
st.write("<h3 style='color:blue;'>Get Started Now!</h3>",unsafe_allow_html=True)

st.divider()

#caption method to add caption
st.caption("This is a simple student management system")

#CODE method to display code snippet
st.code("""
def add(a,b):
    return a+b
""",language="python")
st.divider()


st.latex(r'''
a^2 + b^2 = c^2
''')

#Divider method to sperate sections
st.divider()

#button method to add a button
if st.button("Click Me"):
    st.write("Button Clicked!")
    st.success("Success! You clicked the button.")
    st.balloons()
else:
    st.write("Button not clicked yet.")
    st.error("Error! Please click the button.")
st.divider()
   
#Text input method to take user input
name=st.text_input("Enter your name:")
if name==" ":
    st.warning("Name cannot be empty.")
elif not name.isalpha():
    st.warning("Please enter a valid name containing only letters.")
else:
    st.write(f"Hello, {name}!")
st.divider()

feedback=st.text_area("Enter your feedback:")
st.write("Your feedback:",feedback)

#Checkbox method to add checkbox
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing!")     
    
#Radio button method to add radio buttons
gender=st.radio("Select your gender:",("Male","Female","Other"))
st.write("You selected:",gender)
st.divider()

#Selectbox method to add dropdown
country=st.selectbox("Select your country:",["USA","Canada","UK","Australia","  Other"])
st.write("You selected:",country)   
st.divider()

#multiselect method to add multiselect dropdown
hobbies=st.multiselect("Select your hobbies:",["Reading","Traveling","Cooking","Sports","Music"])
st.write("You selected:",hobbies)
st.divider()

#Slider method to add slider
age=st.slider("Select your age:",0,100,25)
st.write("Your age is:",age)   
st.divider()

#File uploader method to upload files
uploaded_file=st.file_uploader("Upload a file:")
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("File name:",uploaded_file.name)        
st.divider()
 
    
#Form method to add form
with st.form("my_form"):
    st.write("Inside the form")
    name=st.text_input("Name")
    age=st.number_input("Age",0,100)
    submitted=st.form_submit_button("Submit")
    if submitted:
        st.write("<h4 style='color:Green;'>Get Started Now!</h4>",unsafe_allow_html=True)
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
st.divider()

        
with st.form("Login"):
    st.write("Fill the credentials to login")
    user=st.text_input("Username")
    age=st.text_input("Password",type="password")
    submitted=st.form_submit_button("Login")
    if submitted:
        st.success("Login Successful!")
        st.write(f"Welcome: {user}")
st.divider()

#Columns method to add columns
col1,col2,col3=st.columns(3)
with col1:
    st.header("Student Name")
    st.text("Sarika")
with col2:
    st.header("Roll Number")
    st.text("24")
with col3:
    st.header("Age")
    st.text("20") 

st.divider()

#Container method to add container
container = st.container()
container.write("This is inside the container")
container.button("Click Here")
st.divider()

#Table method to add table
data={
    'Name':['Sarika','Siri','Bharath'],
    'ID':[24,12,25],
    'Department':['DS','CS','IT']
}
st.table(data)
st.divider()

#sidebar 
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")
st.divider()

@st.cache_data
def load_data():
    return[1,2,3,4]
data=load_data
st.write("Cached data:",data)
