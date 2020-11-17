# int, float, str, bool
#  and  or   not 
# bool:  True  False
'''legyen nő, a kor legyen > 15, ne legyen a hajszine lila, kék, rózsaszin'''
gender = 'nő'
age = 16
color = 'barna'

if gender == 'nő' and 15< age < 20 and ( color == 'barna' or color == 'szőke' or color == 'vörös'):
  print('Lajosnak tetszik')
else:
  print('Lajosnak nem tetszik') 