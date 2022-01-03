import pyinputplus as pyip
price=0
bread=pyip.inputMenu(['Wheat','White','Sourdough'],numbered=True)
if bread=='Wheat':
    price+=30
elif bread=='White':
    price+=30
else:
    price+=50
protein=pyip.inputMenu(['Chicken','Turkey','Ham','Tofu'],numbered=True)
if protein=='Chicken':
    price+=50
elif protein=='Turkey':
    price+=60
elif protein=='Ham':
    price+=60
else:
    price+=70
cheese=pyip.inputYesNo(prompt='Would you like Cheese: ')
if cheese=='yes':
    cheesemenu=pyip.inputMenu(['Cheddar','Swiss','Mozzarella'],numbered=True)
    if cheesemenu=='Cheddar':
        price+=20
    elif bread=='Swiss':
        price+=40
    else:
        price+=30
mayo=pyip.inputYesNo(prompt='Would you like Mayo: ')
if mayo=='yes':
    price=price+10
lettuce=pyip.inputYesNo(prompt='Would you like Lettuce: ')
if lettuce=='yes':
    price=price+10
mustard=pyip.inputYesNo(prompt='Would you like Mustard: ')
if mustard=='yes':
    price=price+10
tomato=pyip.inputYesNo(prompt='Would you like Tomato: ')
if tomato=='yes':
    price=price+10
number=pyip.inputInt(prompt='How many sandwiches?: ',min=1)
print("Total Price is",number*price)
