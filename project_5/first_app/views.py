from django.shortcuts import render

def home(request):

    data=meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "mealinfo":"The BeaverTail is a fried dough pastry that is sold in a variety of flavours. Most flavours of BeaverTails are topped with sweet condiments and confections, such as whipped cream, banana slices, crumbled Oreos, cinnamon sugar, and chocolate hazelnut"
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "mealinfo":"The BeaverTail is a fried dough pastry that is sold in a variety of flavours. Most flavours of BeaverTails are topped with sweet condiments and confections, such as whipped cream, banana slices, crumbled Oreos, cinnamon sugar, and chocolate hazelnut"
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "mealinfo":"The BeaverTail is a fried dough pastry that is sold in a variety of flavours. Most flavours of BeaverTails are topped with sweet condiments and confections, such as whipped cream, banana slices, crumbled Oreos, cinnamon sugar, and chocolate hazelnut"

        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "mealinfo":"The BeaverTail is a fried dough pastry that is sold in a variety of flavours. Most flavours of BeaverTails are topped with sweet condiments and confections, such as whipped cream, banana slices, crumbled Oreos, cinnamon sugar, and chocolate hazelnut"
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "mealinfo":"The BeaverTail is a fried dough pastry that is sold in a variety of flavours. Most flavours of BeaverTails are topped with sweet condiments and confections, such as whipped cream, banana slices, crumbled Oreos, cinnamon sugar, and chocolate hazelnut"
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "mealinfo":"The BeaverTail is a fried dough pastry that is sold in a variety of flavours. Most flavours of BeaverTails are topped with sweet condiments and confections, such as whipped cream, banana slices, crumbled Oreos, cinnamon sugar, and chocolate hazelnut"

        }
        ]


    return render(request,'index.html',{'data':data})


def about(request):
    return render(request,'index.html')

