from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.core.exceptions import ValidationError

@api_view(['GET'])
def get_events(request):
    access_key = '336a82f42c718236a4ef1487e85dd5ef9f2854ec'
    headers = {'Authorization': f'Bearer {access_key}'}
    url = 'https://api.timepad.ru/v1/events.json'
    category_ids = request.GET.get('category_id')  # Получение параметра category_ids из запроса
    print(category_ids)
    if category_ids == None:
        category_ids = 525
    try:
        print(0)
        params = {'category_ids': category_ids}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            events = response.json()
            return Response(events)
        else:
            return Response({'error': 'Failed to fetch events'}, status=response.status_code)
    except ValidationError:
        return Response({'error': 'Invalid category_ids'}, status=400)

@api_view(['GET'])
def get_categories(request):
    access_key = '336a82f42c718236a4ef1487e85dd5ef9f2854ec'
    headers = {'Authorization': f'Bearer {access_key}'}
    url = 'https://api.timepad.ru/v1/dictionary/event_categories'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        events = response.json()
        return Response(events)
    else:
        return Response({'error': 'Failed to fetch categories'}, status=response.status_code)