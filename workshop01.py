try :
    def AS(sentence):
        words = sentence.split()
        total = len(words)
        unique = set(words)
        count = {word: words.count(word) for word in unique}
        repeated = {word: count for word, count in count.items() if count > 1}

        print(f"มีคำรวมทั้งหมด {total} คำ")
        print(f"มีคำที่ซ้ำกันรวม {len(repeated)} คำคือ {', '.join(repeated)}")

        for word, count in repeated.items():
            print(f"คำว่า {word} ซ้ำกัน {count} ครั้ง")
        print ("----------------------------------------")
except Exception :
    print('มีข้อพลาดเกิดขึ้น')
    print ("----------------------------------------")

print ("----------------------------------------")
user = input("ป้อนข้อความ: ")
print ("----------------------------------------")
AS(user)