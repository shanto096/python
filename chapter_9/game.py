import random  # random মডিউল ইমপোর্ট করা হয়েছে র‌্যান্ডম নাম্বার জেনারেট করার জন্য

# ১ থেকে ১০০ এর মধ্যে একটি র‌্যান্ডম স্কোর তৈরি করা হচ্ছে
randomscore = random.randint(1, 100)

# গেম ফাংশন ডিফাইন করা
def game():
    print('🎮 Game start')

    # আগের হাইস্কোর পড়ার জন্য ফাইল ওপেন করা হচ্ছে
    with open('score.txt') as f:  # ✅ ফাইল path এখানে ঠিক করতে হবে (folder তৈরি থাকতে হবে)
        hiscore = f.read()

        # যদি ফাইলে কিছু থাকে, সেটিকে integer তে কনভার্ট করো
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0  # যদি ফাইল খালি থাকে, তাহলে হাইস্কোর ০ ধরা হবে

    # র‌্যান্ডম স্কোর প্রিন্ট করা
    print(f'📊 Current score: {randomscore}')

    # যদি র‌্যান্ডম স্কোর > হাইস্কোর হয়, তাহলে নতুন হাইস্কোর লিখে দাও
    if randomscore > hiscore:
        with open('score.txt', 'w') as f:
            f.write(str(randomscore))
            print("🏆 New high score saved!")

    return randomscore  # স্কোর রিটার্ন করা

# ফাংশন কল করে গেম চালানো
game()
