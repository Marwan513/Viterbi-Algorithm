p_s_s = 0.8
p_s_r = 0.2
p_r_s = 0.4
p_r_r = 0.6

p_s = 0.6
p_r = 0.4

p_s_h = 0.8
p_s_g = 0.2
p_r_h = 0.4
p_r_g = 0.6

mood = ['G','G','H','H','H','H','G']
prob = []
weather = []

if mood[0] == 'H':
    prob.append((p_s*p_s_h , p_r*p_r_h))
else :
    prob.append((p_s*p_s_g , p_r*p_r_g))
    
if prob[0][0] > prob[0][1]:
    weather.append('Sunny')
else:
    weather.append('Rainy')

for i in range(1,len(mood)):
    yesterday_sunny , yesterday_rainy = prob[-1]
    if mood[i] == 'H':
        today_sunny = max(yesterday_sunny*p_s_s*p_s_h , yesterday_rainy*p_r_s*p_s_h)
        today_rainy = max(yesterday_sunny*p_s_r*p_r_h , yesterday_rainy*p_r_r*p_r_h)
        prob.append((today_sunny,today_rainy))

    else:
        today_sunny = max(yesterday_sunny*p_s_s*p_s_g , yesterday_rainy*p_r_s*p_s_g)
        today_rainy = max(yesterday_sunny*p_s_r*p_r_g , yesterday_rainy*p_r_r*p_r_g)
        prob.append((today_sunny,today_rainy))
    
    if prob[i][0] > prob[i][1]:
        weather.append('Sunny')
    else:
        weather.append('Rainy')

print('Weather sequence is:',weather)