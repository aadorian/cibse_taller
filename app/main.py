import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport

# Define a function to generate the data profiling report
def generate_report(data):
    profile = ProfileReport(data, title='Data Profiling Report', explorative=True)
    return profile

# Define the Streamlit app
def main():
    # Set the app title
    st.title('Data Profiling App')

    # Allow users to upload a file
    uploaded_file = st.file_uploader('Upload a CSV file', type='csv')

    if uploaded_file is not None:
        # Load the data file
        data = pd.read_csv(uploaded_file, sep=';')

        # Generate the data profiling report
        report = generate_report(data)

        # Display the report as an HTML file
        st.write(report.to_html(), unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()
