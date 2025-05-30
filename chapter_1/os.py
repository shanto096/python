# os module kivabe kaj kore 
import os

# 1. বর্তমান ডিরেক্টরি দেখানো
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# # 2. নতুন ফোল্ডার তৈরি করা
folder_name = "my_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")

# # 3. নতুন ফোল্ডারে একটি ফাইল তৈরি করা
file_path = os.path.join(folder_name, "my_file.txt")
with open(file_path, "w") as f:
    f.write("Hello from Python os module!\n")
    print(f"File 'my_file.txt' created inside '{folder_name}'.")

# 4. ডিরেক্টরির সব ফাইল ও ফোল্ডার দেখানো
print("Files and folders in current directory:")
print(os.listdir())

# # 5. ফাইল ও ফোল্ডার মুছে ফেলা
os.remove(file_path)
print(f"File '{file_path}' deleted.")

os.rmdir(folder_name)
print(f"Folder '{folder_name}' deleted.")
