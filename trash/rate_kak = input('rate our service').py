rate_kak = int(input('rate our service'))


# rate = int(rate_kak)


if (rate_kak < 1):
    rate_kak = 1

if (rate_kak > 5):
    rate_kak = 5

# feedback = ''

if (rate_kak == 1):
    feedback = print('схуяли?')
elif (rate_kak == 2):
    feedback = print('нахуй ты 2 поставил')
elif (rate_kak == 3):
    feedback = print('я тебе тройку в ебало дам')
elif (rate_kak == 4):
    feedback = print('поставь 5 заебал')
else:
    feedback = input('why not 5?')
print(feedback)
