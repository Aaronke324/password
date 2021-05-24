password = 'a123456'
i = 3
while i > 0:
	answer = input('請輸入你的密碼:')
	if answer == password:
		print('登入成功。')
		break
	else:
		i = i - 1
		print('密碼錯誤!還有',i ,'次機會')


