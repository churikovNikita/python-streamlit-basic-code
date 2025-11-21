import streamlit as st
import datetime
name = st.text_input('Name')
comp_name = st.text_input('Company Name')



start_date = st.date_input('Starting date',datetime.date(2019,7,6),format="DD/MM/YYYY",)
end_date = st.date_input('Ending date',format="DD/MM/YYYY",)


str_start_date = str(start_date).split(sep="-")
str_end_date = str(end_date).split(sep="-")


btn_show = st.button('Show')


year_dif = int(str_end_date[0]) - int(str_start_date[0])
mounth_dif = int(str_end_date[1]) - int(str_start_date[1])
days_dif = int(str_end_date[2]) - int(str_start_date[2])


if btn_show:
    st.write(f'Years dif = {year_dif}. Mounth dif = {mounth_dif}. Days dif = {days_dif}')