def delete_student():
    student_id = entry_id.get()
    cursor.execute('SELECT * FROM DB_student WHERE db_student_id=?', (student_id,))
    delete = cursor.fetchall()
    cursor.execute('DELETE FROM DB_student WHERE db_student_id=?', (student_id,))
    print('Following row is deleted', delete)
    conn.commit()

button_delete = tk.Button(root, text='delete', command=delete_student)
button_delete.pack(pady=25)
