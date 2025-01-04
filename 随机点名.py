import tkinter as tk
import tkinter.ttk as ttk
import random
import json
import logging
from tkinter import filedialog


# 设置日志格式，方便排查问题
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data():
    """从本地文件加载点名相关数据"""
    try:
        with open('roll_call_data.json', 'r') as file:
            data = json.load(file)
            return data.get('alreadyCalled', []), data.get('currentIndex', -1), data.get('selectedStudentColor', 'black'), data.get('students', [])
    except FileNotFoundError:
        return [], -1, 'black', []


def save_data(already_called, current_index, selected_student_color, students):
    """保存点名相关数据到本地文件"""
    data = {
        'alreadyCalled': already_called,
        'currentIndex': current_index,
        'selectedStudentColor': selected_student_color,
        'students': students
    }
    with open('roll_call_data.json', 'w') as file:
        json.dump(data, file)


def start_rolling():
    """开始滚动点名的过程"""
    global rolling, button_enabled
    if len(students) == 0:
        tk.messagebox.showinfo("提示", "没有导入名单，请先导入名单。")
        return
    rolling = True
    button_enabled = False
    roll_names()
    root.after(1000, stop_rolling)


def stop_rolling():
    """停止滚动点名，确定被点名学生"""
    global rolling, button_enabled
    rolling = False  # 确保正确将rolling设为False，停止滚动点名逻辑
    call_student()
    button_enabled = True


def roll_names():
    """持续滚动显示随机学生名字（模拟滚动效果）"""
    global rolling
    if rolling:
        random_name = random.choice(students)
        print_student_label.config(text=random_name)
        root.after(50, roll_names)
        logging.debug(f"当前正在滚动点名，显示名字: {random_name}")  # 记录点名滚动时的信息，方便排查问题


def call_student():
    """确定最终被点名的学生，更新相关状态并保存数据"""
    global already_called, current_index
    if len(already_called) < len(students):
        candidate = None
        while candidate is None or candidate in already_called:
            candidate = random.choice(students)
        print_student_label.config(text=f"被点名的同学是：{candidate}")
        selected_student_label.config(text=candidate)
        already_called.append(candidate)
        current_index += 1
    else:
        print_student_label.config(text="所有人已抽完，开始新一轮。")
        already_called = []
        current_index = -1
    save_data(already_called, current_index, selected_student_color, students)


def change_color(new_color):
    """改变被点名学生显示文字的颜色，并保存颜色设置"""
    global selected_student_color
    selected_student_color = new_color
    # 通过样式来更新显示被点名学生文字的颜色
    style.configure('SelectedStudent.TLabel', foreground=new_color)
    save_data(already_called, current_index, selected_student_color, students)


def upload_file():
    """上传学生名单文件"""
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            global students
            students = [line.strip() for line in content.splitlines() if line.strip()]
        save_data(already_called, current_index, selected_student_color, students)


def clear_students():
    """清除学生名单及相关点名状态数据"""
    global students, already_called, current_index
    students = []
    already_called = []
    current_index = -1
    save_data(already_called, current_index, selected_student_color, students)


# 加载初始数据
already_called, current_index, selected_student_color, students = load_data()

root = tk.Tk()
root.title("随机点名")
# 设置窗口为全屏模式
root.attributes('-fullscreen', True)

# 设置主题样式，获取更美观的外观
style = ttk.Style()
style.theme_use('clam')

# 自定义显示被点名学生标签的样式
style.configure('SelectedStudent.TLabel',
                font=("Helvetica", 100, "bold"),
                foreground=selected_student_color)

# 获取屏幕宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 主框架，用于整体布局
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# 显示被点名学生的标签，应用自定义样式
selected_student_label = ttk.Label(main_frame, style='SelectedStudent.TLabel', text="")
selected_student_label.pack(pady=(50, 20), padx=20, fill=tk.BOTH, expand=True)

# 提示标签
print_student_label = ttk.Label(main_frame, font=("Helvetica", 24, "normal"), text="被点名的同学是：")
print_student_label.pack(pady=(0, 10), padx=20, fill=tk.BOTH, expand=True)

# 按钮框架，用于放置三个按钮，统一布局
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=(0, 30), padx=20, fill=tk.BOTH, expand=True)

# 点名按钮
call_button = ttk.Button(button_frame, text="点名", command=start_rolling, style='TButton')
call_button.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

# 上传名单按钮
upload_button = ttk.Button(button_frame, text="上传名单", command=upload_file, style='TButton')
upload_button.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

# 清除名单按钮
clear_button = ttk.Button(button_frame, text="清除名单", command=clear_students, style='TButton')
clear_button.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

# 颜色选择容器
color_select_container = ttk.Frame(main_frame)
color_select_container.pack(pady=(0, 50), padx=20, fill=tk.BOTH, expand=True)

# 配置颜色选择按钮样式，设置合适大小（通过padding等方式间接控制外观大小）
style.configure('Color.TButton',
                borderwidth=0,
                relief='flat',
                background='#FFFFFF',  # 初始背景色设为白色，方便显示颜色效果
                foreground='black',
                focuscolor='',
                bordercolor='',
                lightcolor='#E0E0E0',  # 鼠标悬停变浅灰色的颜色设置
                darkcolor='#FFFFFF',
                padding=(5, 2)  # 通过padding来间接调整按钮大小，可根据实际需求调整数值
                )

# 颜色选择按钮（示例几个颜色，可按需扩展）
colors = ["red", "blue", "purple", "black"]
for color in colors:
    color_select = ttk.Button(color_select_container, text='',
                              command=lambda c=color: change_color(c), style='Color.TButton')
    color_select.pack(side=tk.LEFT, padx=5)

# 配置按钮样式，统一外观，设置颜色、圆角等效果
style.configure('TButton',
                font=("Helvetica", 20, "normal"),
                padding=(10, 5),
                borderwidth=0,
                relief='flat',
                background='#6699ff',
                foreground='white',
                focuscolor='',
                bordercolor='',
                lightcolor='#33ccff',  # 鼠标悬停变浅蓝的颜色设置
                darkcolor='#6699ff',
                )


# 控制点名滚动的状态变量
rolling = False
button_enabled = True

root.mainloop()