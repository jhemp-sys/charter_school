import os
from django.conf import settings
from django.shortcuts import render
from django.views import View
from datareader.models import First, BS, PL
import pandas as pd
import numpy as np
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import redirect


def main(request):
    first_data = First.objects.all()
    bs_data = BS.objects.all()
    pl_data = PL.objects.all()
    data = {
        "first": first_data,
        "bs":bs_data,
        "pl":pl_data
    }
    return render(request, 'base.html', {"data":data})

def upload(request):
    file_upload = request.FILES['file']

    first_post(file_upload, "FIRST")
    pl_post(file_upload,"PL")
    bs_post(file_upload, "BS")
    return redirect("main")

def first_post(file, sheetname):
    now = datetime.now()
    record_date = now.strftime("%m-%d-%Y")
    record_dir = os.path.join(settings.MEDIA_ROOT, f"Record-{record_date}")
    os.makedirs(record_dir, exist_ok=True)

    # Save previous data to a file
    previous_data = First.objects.all()
    if previous_data.exists():
        previous_data_values = previous_data.values()
        df = pd.DataFrame.from_records(previous_data_values)
        # Create the filename using datetime as a pure number
        timestamp = now.strftime("%m-%d-%Y (%H-%M)")
        filename = f"FIRST {timestamp}.csv"
        previous_data_path = os.path.join(record_dir, filename)
        df.to_csv(previous_data_path, index=False)

    # sheet_name = "FIRST"
    sheet_name = sheetname
    # Process the new data
    first_data = pd.read_excel(file,sheet_name=sheet_name , header=2, usecols="A:E")
    first_data = first_data.fillna('')  # Replace NaN values with empty strings
    first_data = first_data.applymap(lambda x: '{:,.0f}'.format(x).replace('-', '') if pd.notnull(x) and isinstance(x, float) else x)
    new_first_data = []
    for _, row in first_data.iterrows():
        new_first_data.append(First(
            first_ratings=row.iloc[0],
            expected_results=row.iloc[1],
            points=row.iloc[2],
            status=row.iloc[3],
            notes=row.iloc[4],
        ))
    First.objects.all().delete()
    First.objects.bulk_create(new_first_data)
    return 1

def pl_post(file, sheetname):
    now = datetime.now()
    record_date = now.strftime("%m-%d-%Y")
    record_dir = os.path.join(settings.MEDIA_ROOT, f"Record-{record_date}")
    os.makedirs(record_dir, exist_ok=True)
    
    previous_data = PL.objects.all()
    if previous_data.exists():
        previous_data_values = previous_data.values()
        df = pd.DataFrame.from_records(previous_data_values)
        # Create the filename using datetime as a pure number
        timestamp = now.strftime("%m-%d-%Y (%H-%M)")
        filename = f"PL {timestamp}.csv"
        previous_data_path = os.path.join(record_dir, filename)
        df.to_csv(previous_data_path, index=False)

    # sheet_name = "PL"
    sheet_name = sheetname
    # Process the new data
    pl_data = pd.read_excel(file,sheet_name=sheet_name , header=2, usecols="A:V")
    pl_data = pl_data.fillna('')  # Replace NaN values with empty strings
    pl_data = pl_data.applymap(lambda x: '{:,.0f}'.format(x).replace('-', '') if pd.notnull(x) and isinstance(x, float) else x)
    new_pl_data = []
    for _, row in pl_data.iterrows():
        new_pl_data.append(PL(
            numbers = row.iloc[0],
            titles = row.iloc[1],
            extra = row.iloc[2],
            ammended_budget = row.iloc[3],
            ytd_budget = row.iloc[4],
            september = row.iloc[6],
            october = row.iloc[7],
            november = row.iloc[8],
            december = row.iloc[9],
            january = row.iloc[10],
            february = row.iloc[11],
            march = row.iloc[12],
            april = row.iloc[13],
            may = row.iloc[14],
            june = row.iloc[15],
            july = row.iloc[16],
            august = row.iloc[17],
            year_to_date = row.iloc[19],
            variances = row.iloc[20],
            var = row.iloc[21]
        ))
    PL.objects.all().delete()
    PL.objects.bulk_create(new_pl_data)
    return 1

def bs_post(file, sheetname):
    now = datetime.now()
    record_date = now.strftime("%m-%d-%Y")
    record_dir = os.path.join(settings.MEDIA_ROOT, f"Record-{record_date}")
    os.makedirs(record_dir, exist_ok=True)

    previous_data = BS.objects.all()
    if previous_data.exists():
        previous_data_values = previous_data.values()
        df = pd.DataFrame.from_records(previous_data_values)
        # Create the filename using datetime as a pure number
        timestamp = now.strftime("%m-%d-%Y (%H-%M)")
        filename = f"Balance Sheet(BS) {timestamp}.csv"
        previous_data_path = os.path.join(record_dir, filename)
        df.to_csv(previous_data_path, index=False)

    # sheet_name = "BS"
    sheet_name = sheetname
    # Process the new data
    bs_data = pd.read_excel(file,sheet_name=sheet_name , header=2, usecols="D:U")
    bs_data = bs_data.fillna('')  # Replace NaN values with empty strings
    bs_data = bs_data.applymap(lambda x: '{:,.0f}'.format(x).replace('-', '') if pd.notnull(x) and isinstance(x, float) else x)
    new_bs_data = []
    for _, row in bs_data.iterrows():
        new_bs_data.append(BS(
            titles = row.iloc[0],
            extra = row.iloc[1],
            fye_year=row['FYE 2022'],
            september=row['September'],
            october=row['October'],
            november=row['November'],
            december=row['December'],
            january=row['January'],
            february=row['February'], 
            fytd_activity=row['FYTD \nActivity'],
            as_of_january=row['As of January'],
        ))
    BS.objects.all().delete()
    BS.objects.bulk_create(new_bs_data)
    return 1
