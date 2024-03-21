from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from config.settings.base import OPEN_AI_API_KEY

class MealView(APIView):
    llm = OpenAI(openai_api_key = OPEN_AI_API_KEY, temperature = 0.9)
    prompt_template = PromptTemplate(
        template = 'Give me a Meal that could be created using the following ingredients: {ingredients}',
        input_variables = ['ingredients']
    )
    meal_chain = LLMChain(llm = llm, prompt = prompt_template)

    def get(self, request, format=None):
        user_ingredients = request.query_params['ingredients']
        meal_created = self.meal_chain.run(ingredients = user_ingredients)
        return Response({ 'meal': meal_created })