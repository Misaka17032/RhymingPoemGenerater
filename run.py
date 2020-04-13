import json
import pypinyin 
def yayun(s1, s2):
	if s1 in ['qi', 'ti', 'yi', 'pi', 'di', 'ji', 'li', 'bi', 'ni', 'mi', 'xi', 'ri', 'si', 'zi', 'ci', 'shi', 'zhi', 'chi'] and s2 in ['qi', 'ti', 'yi', 'pi', 'di', 'ji', 'li', 'bi', 'ni', 'mi', 'xi', 'ri', 'si', 'zi', 'ci', 'shi', 'zhi', 'chi']:
		if s1 in ['qi', 'ti', 'yi', 'pi', 'di', 'ji', 'li', 'bi', 'ni', 'mi', 'xi'] and s2 in ['qi', 'ti', 'yi', 'pi', 'di', 'ji', 'li', 'bi', 'ni', 'mi', 'xi']:
			return True
		if s1 in ['ri', 'si', 'zi', 'ci', 'shi', 'zhi', 'chi'] and s2 in ['ri', 'si', 'zi', 'ci', 'shi', 'zhi', 'chi']:
			return True
		return False
	if s1 in ['wu', 'ru', 'tu', 'pu', 'su', 'du', 'fu', 'gu', 'hu', 'ku', 'lu', 'zu', 'cu', 'bu', 'nu', 'mu', 'zhu', 'chu', 'shu', 'qu', 'yu', 'ju', 'xu'] and s2 in ['wu', 'ru', 'tu', 'pu', 'su', 'du', 'fu', 'gu', 'hu', 'ku', 'lu', 'zu', 'cu', 'bu', 'nu', 'mu', 'zhu', 'chu', 'shu', 'qu', 'yu', 'ju', 'xu']:
		if s1 in ['qu', 'yu', 'ju', 'xu'] and s2 in ['qu', 'yu', 'ju', 'xu']:
			return True
		if s1 in ['wu', 'ru', 'tu', 'pu', 'su', 'du', 'fu', 'gu', 'hu', 'ku', 'lu', 'zu', 'cu', 'bu', 'nu', 'mu', 'zhu', 'chu', 'shu'] and s2 in ['wu', 'ru', 'tu', 'pu', 'su', 'du', 'fu', 'gu', 'hu', 'ku', 'lu', 'zu', 'cu', 'bu', 'nu', 'mu', 'zhu', 'chu', 'shu']:
			return True
		return False
	if s1 in ["yun", "yuan", "me"] or s2 in ["yun", "yuan", "me"]:
		if s1 == s2:
			return True
		else:
			return False
	if s1 == "yan":
		s1 = "yian"
	if s2 == "yan":
		s2 = "yian"
	if s1 == "ye":
		s1 = "yie"
	if s2 == "ye":
		s2 = "yie"
	if s1 == "feng":
		s1 = "fong"
	if s2 == "feng":
		s2 = "fong"
	if s1 == "meng":
		s1 = "mong"
	if s2 == "meng":
		s2 = "mong"
	y = ["a", "o", "e", "i", "u"]
	e = ["ai", "ei", "ao", "ou", "an", "en", "ia", "ie", "in", "ue", "un", "ui", "iu"]
	s = ["ong", "ang", "eng", "uan", "ian"]
	if s1[-3:] == s2[-3:] and s1[-3:] in s:
		return True
	if s1[-2:] == s2[-2:] and s1[-2:] in e and s1[-3:] not in s and s2[-3:] not in s:
		return True
	if s1[-1:] == s2[-1:] and s1[-1:] in y and s1[-2:] not in e and s2[-2:] not in e:
		return True
	return False
def tongdiao(s1, s2):
	a = ["āīēōūǖ", "áíéóúǘ", "ǎǐěǒǔǚ", "àìèòùǜ"]
	for i in s1:
		if i not in "qwertyuiopasdfghjklzxcvbnm":
			ss1 = i
			break
		ss1 = "a"
	for i in s2:
		if i not in "qwertyuiopasdfghjklzxcvbnm":
			ss2 = i
			break
		ss2 = "a"
	for i in a:
		if ss1 in i and ss2 in i:
			return True
		if ss1 == ss2:
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
		last_pinyin = pypinyin.lazy_pinyin(m[-1])[0]
		last_char = [m[-1]]
		for i in range(1, len(target)):
			for j in poet:
				if j[0] == target[i] and yayun(last_pinyin, pypinyin.lazy_pinyin(j[-1])[0]) and j not in ans and j[-1] not in last_char and not tongdiao(pypinyin.pinyin(ans[-1][-1])[0][0], pypinyin.pinyin(j[-1]))[0][0]:
					ans.append(j)
					last_char.append(j[-1])
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
can = True
wrong_char = ""
if input("要开启多重结果检索吗？（默认为关闭，开启有可能会影响检索速度）:(y/n)") == "y":
	multi = True
if input("检索时包含宋词吗？（默认为关闭，开启会影响检索速度）:(y/n)") == "y":
	ci = True
if input("生成五言诗或七言诗（默认为五言）:（5/7）") == "7":
	fos = 7
target = input("输入要生成的语句：")
fin = open("data" + str(fos) + ".txt", "r")
t = fin.read()
fin.close()
for i in target:
	if i not in t:
		can = False
		wrong_char = i
		break
if can:
	poet = read(fos, ci)
	print("数据读取完毕")
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
else:
	print("没有找到以" + wrong_char + "字开头的诗句")