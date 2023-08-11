from django.shortcuts import render
from django.http import HttpResponse
from .utils.predict import recommend

def index(request):
    return render(request, 'index.html')

def recommendation_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        # Process the user input using the recommendation model
        recommendations = recommend(user_input)

        # Convert the DataFrame into a list of dictionaries
        recommendations_list = recommendations.to_dict(orient='records')

        # Pass the recommendations as a context variable to the template
        context = {'recommendations': recommendations_list}
        request.session['recommendations'] = recommendations_list
        return render(request, 'recommendations.html', context)
    elif request.method == 'GET':
        if 'recommendations' in request.session:
            recommendations_list = request.session.pop('recommendations')
            context = {'recommendations': recommendations_list}
            return render(request, 'recommendations.html', context)
    
    return HttpResponse("Method not allowed")