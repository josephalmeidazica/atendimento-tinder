import streamlit as st

st.title('Suporte a denúncias :red[Tinder]')

st.text('Informe seus dados e clique em enviar para prosseguirmos com o atendimento.')

title = st.text_input('Nome completo')

phone = st.text_input('Telefone')

cpf = st.text_input('CPF')

st.button('Enviar')