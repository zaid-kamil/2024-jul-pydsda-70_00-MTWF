import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    # In a real scenario, you'd load the actual Home Credit Default Risk dataset
    # For this example, we'll create a small mock dataset
    np.random.seed(0)
    data = pd.DataFrame({
        'SK_ID_CURR': range(1000),
        'TARGET': np.random.choice([0, 1], size=1000, p=[0.92, 0.08]),
        'DAYS_BIRTH': np.random.randint(-25000, -7000, 1000),
        'AMT_INCOME_TOTAL': np.random.lognormal(10, 1, 1000),
        'AMT_CREDIT': np.random.lognormal(11, 0.5, 1000),
        'DAYS_EMPLOYED': np.random.randint(-15000, 0, 1000),
    })
    return data

def main():
    st.title('Home Credit Default Risk - Exploratory Data Analysis')

    data = load_data()

    st.sidebar.header('Choose Analysis')
    analysis = st.sidebar.selectbox(
        'Select Analysis',
        ['Data Overview', 'Target Distribution', 'Age Analysis', 'Income vs Credit', 'Employment Analysis']
    )

    if analysis == 'Data Overview':
        st.header('Data Overview')
        st.write(data.head())
        st.write(data.describe())

    elif analysis == 'Target Distribution':
        st.header('Target Distribution')
        fig, ax = plt.subplots()
        data['TARGET'].value_counts(normalize=True).plot(kind='bar', ax=ax)
        ax.set_title('Distribution of Target Variable')
        ax.set_ylabel('Proportion')
        st.pyplot(fig)

    elif analysis == 'Age Analysis':
        st.header('Age Analysis')
        data['AGE_YEARS'] = -data['DAYS_BIRTH'] / 365
        fig, ax = plt.subplots()
        sns.histplot(data=data, x='AGE_YEARS', hue='TARGET', multiple='stack', ax=ax)
        ax.set_title('Age Distribution by Target')
        st.pyplot(fig)

    elif analysis == 'Income vs Credit':
        st.header('Income vs Credit Analysis')
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x='AMT_INCOME_TOTAL', y='AMT_CREDIT', hue='TARGET', ax=ax)
        ax.set_title('Income vs Credit Amount')
        ax.set_xlabel('Income')
        ax.set_ylabel('Credit Amount')
        st.pyplot(fig)

    elif analysis == 'Employment Analysis':
        st.header('Employment Analysis')
        data['YEARS_EMPLOYED'] = -data['DAYS_EMPLOYED'] / 365
        fig, ax = plt.subplots()
        sns.boxplot(data=data, x='TARGET', y='YEARS_EMPLOYED', ax=ax)
        ax.set_title('Years Employed by Target')
        ax.set_xlabel('Target')
        ax.set_ylabel('Years Employed')
        st.pyplot(fig)

if __name__ == "__main__":
    main()