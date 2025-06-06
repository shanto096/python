import os  # OS module import করা হয়েছে যাতে ফাইল ও ফোল্ডার নিয়ে কাজ করা যায়

# ইউজারের কাছ থেকে ফোল্ডার নাম নেওয়া
folderName = input("📁 Folder name: ")

# যদি ফোল্ডার না থাকে, তাহলে বানিয়ে ফেলো
if not os.path.exists(folderName):
    os.makedirs(folderName)  # নতুন ফোল্ডার তৈরি
    print("✅ Folder created.")
else:
    print("📁 Folder already exists.")  # যদি আগে থেকেই থাকে

# ইউজারের কাছ থেকে ফাইল নাম নেওয়া
fileName = input("📄 File name (e.g. myfile.txt): ")

# ফোল্ডারের ভিতরে ফাইলের পূর্ণ path বানানো
file_path = os.path.join(folderName, fileName)

# যদি ফাইল আগে থেকেই থাকে, তাহলে জানাও
if os.path.exists(file_path):
    print("⚠️ File already exists.")
else:
    # না থাকলে নতুন ফাইল তৈরি করো (খালি)
    with open(file_path, 'w') as f:
        print("✅ File created.")

# ইউজারের কাছ থেকে লেখার জন্য কিছু text নেওয়া
text = input('📝 Write some text to save in file: ')

# ফাইলে লেখা হচ্ছে (আগের লেখা ওভাররাইট হবে)
with open(file_path, 'w') as f:
    f.write(text)
    print("✅ Text written to file.")

# ফাইলটি আবার খুলে সেই লেখা পড়ে দেখানো
with open(file_path, 'r') as f:
    p = f.read()
    print("📄 File content:\n" + p)
