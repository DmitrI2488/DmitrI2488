from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def get_events(request):
    access_key = '336a82f42c718236a4ef1487e85dd5ef9f2854ec'
    headers = {'Authorization': f'Bearer {access_key}'}
    url = 'https://api.timepad.ru/v1/events.json'
    params = {'category_ids': '457'}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        events = response.json()
        return Response(events)
    else:
        return Response({'error': 'Failed to fetch events'}, status=response.status_code)
