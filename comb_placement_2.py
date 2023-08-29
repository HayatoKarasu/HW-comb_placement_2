from matplotlib import pyplot as plt

plt.text(0.01, 0.9, '1) У нас 2 яблока и 3 груши.', fontsize=15)
plt.text(0.01, 0.8, 'Сколько комбинаций раздачи на 5 дней?', fontsize=15)
form = r"$A = \frac{5!}{2!*3!} = \frac{5*4*3!}{2!*3!} = 5*2 = 10$"
plt.text(0.01, 0.7, form, fontsize=15)
plt.text(0.01, 0.5, '2) У нас 9 вагонов и 4 человека.', fontsize=15)
plt.text(0.01, 0.4, 'Сколько комбинаций без повторений:', fontsize=15)
form = r"$A_4^9 = \frac{9!}{(9-4)!} = \frac{9!}{5!} = \frac{9*8*7*6*5!}{5!} = 3024$"
plt.text(0.01, 0.3, form, fontsize=15)
plt.text(0.01, 0.2, 'Сколько комбинаций c повторениями:', fontsize=15)
form = r"$Ā_4^9 = 9^4 = 6561$"
plt.text(0.01, 0.1, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, '3) У нас 5 символов из которых 10 значный', fontsize=15)
plt.text(0.01, 0.8, 'пароль. Сколько комбинаций если цифры ', fontsize=15)
plt.text(0.01, 0.7, 'могут повторяться:', fontsize=15)
form = r"$Ā_5^{10} = 5^10 = 9 765 625$"
plt.text(0.01, 0.6, form, fontsize=15)
plt.text(0.01, 0.5, 'Если бы хакер из первой контрольной', fontsize=15)
plt.text(0.01, 0.4, 'решил бы подобрать пароль:', fontsize=15)
form = r"$9765625/60(с/м)\approx 162760(мин)/60(м/ч)\approx$"
plt.text(0.01, 0.3, form, fontsize=15)
form = r"$\approx 2712(час)/24(ч/сут) \approx 113(дней)/30(д/м) \approx$"
plt.text(0.01, 0.2, form, fontsize=15)
form = r"$\approx 3 (месяца)_ 23 (дня)$"
plt.text(0.01, 0.1, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()