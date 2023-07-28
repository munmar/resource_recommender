from django.shortcuts import render
from ..utils.recommendation import train_recommendation_model, get_top_n_recommendations

def recommend_courses(request):
    if request.method == 'POST':
        # Get user input from the form submission or text input field
        user_input = request.POST.get('user_input')

        # Train the recommendation model (you can call this function once during application initialization)
        similarity_scores = train_recommendation_model()

        # Get top N recommendations based on the user's input
        top_n_recommendations = get_top_n_recommendations(user_input, similarity_scores)

        # Pass the recommendations to the template for rendering
        context = {'recommendations': top_n_recommendations}
        return render(request, 'recommendations.html', context)

    return render(request, 'index.html')