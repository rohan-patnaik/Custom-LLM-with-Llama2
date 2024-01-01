import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,no_words,article_style):

    ### LLama2 model
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
        Write an article for {article_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["article_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(article_style=article_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Write Articles",
                    page_icon='📰',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Write Articles 📰")

input_text=st.text_input("Enter the topic for chosen article")

## creating two more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    article_style=st.selectbox('Generate article for',('Common Users','Data Scientist','PhD students'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,article_style))