import json
from pypinyin import lazy_pinyin
def yayun(s1, s2):
	y = ["a", "o", "e", "i", "u"]
	e = ["ai", "ei", "ao", "ou", "an", "en", "ia", "ie", "in", "ue", "un", "ui", "iu"]
	s = ["ong", "ang", "eng"]
	if s1[-3:] == s2[-3:] and s1[-3:] in s:
		return True
	if s1[-2:] == s2[-2:] and s1[-2:] in e:
		return True
	if s1[-1:] == s2[-1:] and s1[-1:] in y and s1[-2:] not in e and s2[-2:] not in e:
		return True
	return False
poet = []
f = []
last_pinyin = ""
matched = False
fos = int(input("生成五言诗或七言诗:（5/7）"))
for i in range(0, 58):
	fin = open("./poet/poet.tang." + str(i * 1000) + ".json","r")
	s = fin.read()
	temp = json.loads(s)
	for j in temp:
		for m in j["paragraphs"]:
			if len(m) == 12 and fos == 5:
				poet.append(m[0:5])
				poet.append(m[6:11])
			elif len(m) == 16 and fos == 7:
				poet.append(m[0:7])
				poet.append(m[8:15])
fin.close()
target = input("输入要生成的语句：")
for i in poet:
	if i[0] == target[0]:
		f.append(i)
		matched = True
if matched:
	matched = False
	for m in f:
		ans = [m]
		last_pinyin = lazy_pinyin(m[len(m) - 1])[0]
		for i in range(1, len(target)):
			for j in poet:
				if j[0] == target[i] and yayun(last_pinyin, lazy_pinyin(j[len(j) - 1])[0]):
					ans.append(j)
					break
		if len(ans) == len(target):
			matched = True
			print("生成结果：")
			for i in ans:
				print(i)
			break
	if not matched:
		print("没有找到符合" + target + "的诗句组合")
else:
	print("没有找到以" + target[0] + "字开头的诗句")