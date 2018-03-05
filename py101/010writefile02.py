append_text='\nThis is appended file.'  # 为这行文字提前空行 "\n"
my_file=open('my file.txt','w')   # 'a'=append 以增加内容的形式打开
my_file.write(append_text)
my_file.close()