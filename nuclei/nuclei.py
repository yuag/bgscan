import os
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import threading
from ttkbootstrap import Style

class NucleiScan:
    def __init__(self, root):
        self.root = root
        self.root.title("nuclei批量扫描工具")
        self.style = Style(theme='lumen')
        self.create_widgets()

    def create_widgets(self):
        # 创建标签和输入框
        urls_label = ttk.Label(self.root, text="导入网站:")
        self.urls_entry = ttk.Entry(self.root, width=40)
        self.urls_button = ttk.Button(self.root, text="选择文件", command=self.select_urls_file)

        templates_label = ttk.Label(self.root, text="导入POC:")
        self.templates_entry = ttk.Entry(self.root, width=40)
        self.templates_button = ttk.Button(self.root, text="选择目录", command=self.select_templates_directory)

        nuclei_label = ttk.Label(self.root, text="nuclei程序路径:")
        self.nuclei_entry = ttk.Entry(self.root, width=40)
        self.nuclei_button = ttk.Button(self.root, text="选择nuclei", command=self.select_nuclei_cutable)

        # 使用grid进行布局
        urls_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.urls_entry.grid(row=0, column=1, padx=5, pady=5)
        self.urls_button.grid(row=0, column=2, padx=5, pady=5)

        templates_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.templates_entry.grid(row=1, column=1, padx=5, pady=5)
        self.templates_button.grid(row=1, column=2, padx=5, pady=5)

        nuclei_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.nuclei_entry.grid(row=2, column=1, padx=5, pady=5)
        self.nuclei_button.grid(row=2, column=2, padx=5, pady=5)

        # 创建扫描按钮
        self.scan_button = ttk.Button(self.root, text="开始扫描", command=self.scan_button_clicked)
        self.scan_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        # 创建文本框显示输出
        self.output_text = tk.Text(self.root, wrap=tk.WORD, width=60, height=15)
        self.output_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def select_urls_file(self):
        urls_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if urls_file:
            self.urls_entry.delete(0, tk.END)
            self.urls_entry.insert(0, urls_file)

    def select_templates_directory(self):
        templates_directory = filedialog.askdirectory()
        if templates_directory:
            self.templates_entry.delete(0, tk.END)
            self.templates_entry.insert(0, templates_directory)

    def select_nuclei_cutable(self):
        nuclei_path = filedialog.askopenfilename()

        if nuclei_path:
            self.nuclei_entry.delete(0, tk.END)
            self.nuclei_entry.insert(0, nuclei_path)

    def run_nuclei_scan(self, urls_file, templates_directory, nuclei_cutable):
        nuclei_command = f"{nuclei_cutable} -l {urls_file} -t {templates_directory}"

        try:
            process = subprocess.Popen(nuclei_command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

            while process.poll() is None:
                line = process.stdout.readline()
                self.output_text.insert(tk.END, line)
                self.output_text.see(tk.END)

                # 将扫描结果写入文本文件
                with open('nuclei.txt', 'a') as result_file:
                    result_file.write(line)

                self.root.update_idletasks()

            # 捕获剩余的输出
            output, _ = process.communicate()
            self.output_text.insert(tk.END, output)
            self.output_text.see(tk.END)

            # 扫描结束后显示提醒
            self.show_scan_complete_message()

        except subprocess.CalledProcessError as e:
            error_message = f"Nuclei 命令执行出错，返回非零状态码: {e.returncode}\n错误输出: {e.output}"
            self.output_text.insert(tk.END, error_message)
            self.output_text.see(tk.END)

    def scan_button_clicked(self):
        urls_file = self.urls_entry.get()
        templates_directory = self.templates_entry.get()
        nuclei_cutable = self.nuclei_entry.get()

        if not os.path.exists(urls_file):
            self.output_text.insert(tk.END, f"错误: {urls_file} 文件不存在。\n")
            return
        if not os.path.exists(templates_directory):
            self.output_text.insert(tk.END, f"错误: {templates_directory} 目录不存在。\n")
            return
        if not os.path.exists(nuclei_cutable):
            self.output_text.insert(tk.END, f"错误: {nuclei_cutable} Nuclei程序不存在。\n")
            return

        self.output_text.delete(1.0, tk.END)
        self.scan_button.config(state="disabled")

        # 在后台运行扫描并在完成后启用扫描按钮
        def run_scan_in_thread():
            self.run_nuclei_scan(urls_file, templates_directory, nuclei_cutable)
            self.scan_button.config(state="normal")

        # 创建一个新线程来运行扫描
        scan_thread = threading.Thread(target=run_scan_in_thread)
        scan_thread.start()

        # 在后台运行扫描并在完成后启用扫描按钮
        def check_scan_thread():
            if scan_thread.is_alive():
                self.root.after(1000, check_scan_thread)
            else:
                self.scan_button.config(state="normal")

        self.root.after(1000, check_scan_thread)

    def show_scan_complete_message(self):
        messagebox.showinfo("扫描完成", "扫描已完成！")

if __name__ == "__main__":
    root = tk.Tk()
    app = NucleiScan(root)
    root.mainloop()
