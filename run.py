import json
from pypinyin import lazy_pinyin
def yayun(s1, s2):
	y = ["a", "o", "e", "i", "u"]
	e = ["ai", "ei", "ao", "ou", "an", "en", "ia", "ie", "in", "ue", "un", "ui", "iu"]
	s = ["ong", "ang", "eng", "uai", "uan", "ian", "iao"]
	if s1[-3:] == s2[-3:] and s1[-3:] in s:
		return True
	if s1[-2:] == s2[-2:] and s1[-2:] in e and s1[-3:] not in s and s2[-3:] not in s:
		return True
	if s1[-1:] == s2[-1:] and s1[-1:] in y and s1[-2:] not in e and s2[-2:] not in e:
		return True
	return False
def read(fos,ci):
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
	if ci:
		for i in range(0, 255):
			fin = open("./poet/poet.song." + str(i * 1000) + ".json","r")
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
	return poet
def jiansuo(poet, f, target, multi):
	result = []
	matched = False
	for m in f:
		ans = [m]
		last_pinyin = lazy_pinyin(m[len(m) - 1])[0]
		last_char = [m[len(m) - 1]]
		for i in range(1, len(target)):
			for j in poet:
				if j[0] == target[i] and yayun(last_pinyin, lazy_pinyin(j[len(j) - 1])[0]) and j not in ans and j[len(j) - 1] not in last_char:
					ans.append(j)
					last_char.append(j[len(j) - 1])
					break
		if len(ans) == len(target):
			matched = True
			result.append(ans)
			if multi == False:
				break
	return result, matched
poet = []
f = []
result = []
matched = False
multi = False
ci = False
fos = 5
if input("要开启多重结果检索吗？（默认为关闭，开启有可能会影响检索速度）:(y/n)") == "y":
	multi = True
if input("检索时包含宋词吗？（默认为关闭，开启会影响检索速度）:(y/n)") == "y":
	ci = True
if input("生成五言诗或七言诗（默认为五言）:（5/7）") == "7":
	fos = 7
poet = read(fos, ci)
print("数据读取完毕")
target = input("输入要生成的语句：")
for i in poet:
	if i[0] == target[0]:
		f.append(i)
		matched = True
if matched:
	result, matched = jiansuo(poet, f, target, multi)
	if matched:
		print("生成结果：")
		for i in result[0]:
			print(i)
		if len(result) > 1:
			if input("还有" + str(len(result) - 1) + "个结果，要查看吗？(y/n)") == "y":
				if len(result) > 10:
					for i in range(1, min(len(result), int(input("结果较多，请输入你想要显示的数量：")))):
						for j in result[i]:
							print(j)
						print("")
				else:
					for i in range(1, len(result)):
						for j in result[i]:
							print(j)
						print("")
	else:
		print("没有找到符合" + target + "的诗句组合")
else:
	print("没有找到以" + target[0] + "字开头的诗句")