def delete_student():
    student_id = entry_id.get()
    cursor.execute('SELECT * FROM DB_student WHERE db_student_id=?', (student_id,))
    delete = cursor.fetchall()
    cursor.execute('DELETE FROM DB_student WHERE db_student_id=?', (student_id,))
    print('Following row is deleted', delete)
    conn.commit()

button_remove = tk.Button(root, text='Remove', command=delete_student)
button_remove.pack(pady=25)
