## bmi calc
normal_range = '''NORMAL RANGE IS 18.5 to 24.9'''
W = float(input('w(Kg)? '))

H = float(input('h(m)? '))

BMI = W/H**2
print(normal_range)
print('your weight is %.2f Kg and your hight is %.2f m and your BMI is: %.2f'  %(W,H,BMI))
wmin = 18.5*H**2
wmax = 24.9*H**2
print('your weight must be between %.2f-%.2f' %(wmin, wmax))

# this is a new comment