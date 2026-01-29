import streamlit as st
import sqlite3
conn=sqlite3.connect("students.db",check_same_thread=False)
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,department TEXT)")
conn.commit()
def create_student(name,age,dept):
    cursor.execute("INSERT INTO students(name,age,department) VALUES(?,?,?)",(name,age,dept))
    conn.commit()
def read_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()
def update_student(id,name,age,dept):
    cursor.execute("UPDATE students SET name=?,age=?,department=? WHERE id=?",(name,age,dept,id))
    conn.commit()
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=?",(id,))
    conn.commit()
menu=["Create","Read","Update","Delete"]
choice=st.sidebar.selectbox("Menu",menu)
if choice=="Create":
    name=st.text_input("Name")
    age=st.number_input("Age")
    dept=st.text_input("Department")
    if st.button("Add"):
        create_student(name,age,dept)
elif choice=="Read":
    st.table(read_students())
elif choice=="Update":
    data=read_students()
    ids=[row[0] for row in data]
    sid=st.selectbox("ID",ids)
    student=[row for row in data if row[0]==sid][0]
    name=st.text_input("Name",student[1])
    age=st.number_input("Age",min_value=1,step=1,value=student[2])
    dept=st.text_input("Department",student[3])
    if st.button("Update"):
        update_student(sid,name,age,dept)
elif choice=="Delete":
    ids=[row[0] for row in read_students()]
    sid=st.selectbox("ID",ids)
    if st.button("Delete"):
        delete_student(sid)