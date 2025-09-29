import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("explore the insight of titanic data")

df=sns.load_dataset('titanic')
st.dataframe(df)

#gender filter
gender = st.sidebar.multiselect("gender",
                               options=df['sex'].unique(),
                               default=df['sex'].unique())
          

#class filter
class_filter = st.sidebar.multiselect("class",
                                      options=df['class'].unique(),
                                      default=df['class'].unique())

#age filter
min_age, max_age = st.sidebar.slider("age",
                              min_value=int(df['age'].min()),
                              max_value=int(df['age'].max()),
                              value=(int(df['age'].min()),int(df['age'].max())))

filtered_df = df[
     (df['sex'].isin(gender))&
     (df['class'].isin(class_filter))&
     (df['age']>=min_age)&
     (df['age']<=max_age)
]
st.dataframe(filtered_df)




#total survived by class
fig = px.bar(df, x='class', y='survived',
             title = 'total survived by class',
             labels = {'class':'class', 'survived':'total survived'},
             color = 'survived', template='plotly_dark'
)
st.plotly_chart(fig)
st.markdown("data insight of titanic")

#age distribution
fig = px.histogram(df, x='age',
                    title='age distribution',
                    labels={'age':'age'},
                    color_discrete_sequence=['#F39C12'],
                    template='plotly_dark'
)
st.plotly_chart(fig)

#pie chart for class distribution
fig = px.pie(df, names='class',
             title='class distribution',
             color_discrete_sequence=px.colors.sequential.RdBu,
             template='plotly_dark'
)
st.plotly_chart(fig)


