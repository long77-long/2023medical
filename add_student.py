import sqlite3

# 连接到SQLite数据库（如果不存在则创建）
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# 创建students表（如果不存在）
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    student_id TEXT NOT NULL UNIQUE
)
''')

# 插入学生信息
student_name = '龙琪琪'
student_id = '20231201009'

try:
    cursor.execute(
        "INSERT INTO students (name, student_id) VALUES (?, ?)",
        (student_name, student_id)
    )
    conn.commit()
    print(f"成功添加学生信息: {student_name} - {student_id}")
    
    # 验证数据是否已添加
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    result = cursor.fetchone()
    if result:
        print(f"数据库中已存在该学生信息: {result[1]} - {result[2]}")
    
except sqlite3.IntegrityError:
    print(f"学生ID {student_id} 已存在于数据库中")
finally:
    # 关闭连接
    conn.close()