

b = set()       # এটা হলো empty set ✅Set এ duplicate item থাকে না। .add(), .remove(), .update() ইত্যাদি method দিয়ে set manage করা যায়।


# 🧺 Python Set: All Methods & Examples

s= {1,2,3,3,4,5}
s.add(10)
print(s)
s.remove(3)
print(s)
s.discard(10)  #নির্দিষ্ট item মুছে ফেলে (না থাকলে error দেয় না)
print(s)
s.pop()# যেকোনো একটি item randomly মুছে ফেলে
print(s)
s2=s.copy()
print(s2)
s.update([7,8])
print(s)




a = {1, 2, 3,4}
b = {3, 4, 5}

# দুই সেট মিলিয়ে নতুন সেট দেয়
print(a.union(b))


# দুই সেট মিলিয়ে নতুন সেট দেয়
print(a.intersection(b))

# শুধু a তে আছে, b তে নেই এমন item
print(a.difference(b))