import os
from django.conf import settings
from django.shortcuts import render
from django.views import View
from datareader.models import Datas
import pandas as pd
import numpy as np
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import redirect


def main(request):
    data = Datas.objects.all()
    return render(request, 'base.html', {"data":data})

def upload(request):
    return render(request, 'upload.html')

def first(request):
    data = Datas.objects.all()
    return render(request, 'FIRST.html', {'data': data})
    

def post(request):
    file = request.FILES['file']

    # Save previous data to a file
    previous_data = Datas.objects.all()
    if previous_data.exists():
        previous_data_values = previous_data.values()
        df = pd.DataFrame.from_records(previous_data_values)
        # Create the filename using datetime as a pure number
        now = datetime.now()
        timestamp = now.strftime("%m-%d-%Y (%H-%M)")
        filename = f"previous_data {timestamp}.csv"
        previous_data_path = os.path.join(settings.MEDIA_ROOT, filename)
        df.to_csv(previous_data_path, index=False)

    # Process the new data
    data = pd.read_excel(file, header=2, usecols="A:E")
    data = data.fillna('')  # Replace NaN values with empty strings
    data = data.applymap(lambda x: '{:,.0f}'.format(x).replace('-', '') if pd.notnull(x) and isinstance(x, float) else x)
    new_data = []
    for _, row in data.iterrows():
        new_data.append(Datas(
            first_ratings=row['FIRST Rating Indicators'],
            expected_results=row['Expected \nResults'],
            points=row['Points'],
            status=row['Status'],
            notes=row['Notes'],
        ))
    Datas.objects.all().delete()
    Datas.objects.bulk_create(new_data)

    return redirect('main')