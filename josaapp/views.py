from django.shortcuts import render
from django.db.models import Count
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from josaapp.models import SeatAllotment
import matplotlib.pyplot as plt
import io
import base64
from io import BytesIO

def home(request):
    return render(request, 'home.html')
def next_page(request):
    return render(request, 'next_page.html')
def cloud(request):
    image_data = open('static/cloud.avif', 'rb').read()
    return HttpResponse(image_data, content_type='image/avif')
def logo(request):
    image_data = open('static/LOGO.jpg', 'rb').read()
    return HttpResponse(image_data, content_type='image/jpg')
def wall(request):
    image_data = open('static/wall.jpg', 'rb').read()
    return HttpResponse(image_data, content_type='image/jpg')
def wall_2(request):
    image_data = open('static/wall(2).jpg', 'rb').read()
    return HttpResponse(image_data, content_type='image/jpg')
def popular_branches(request):
    # Retrieve data from the database
    branches = SeatAllotment.objects.values('branch').annotate(total_count=Count('branch')).order_by('-total_count')

    context = {
        'branches': branches
    }
    return render(request, 'popular_branches.html', context)
def seat_allotment_list(request):
    seat_allotments = SeatAllotment.objects.all()
    # Process the data as needed
    serialized_data = serializers.serialize('json', seat_allotments)

    return JsonResponse(serialized_data, safe=False)

def cutoff_analysis(request):
    if request.method == 'POST':
        rank = int(request.POST.get('rank'))
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        year = int(request.POST.get('year'))
        round_number = int(request.POST.get('round_number'))

        cutoff_data = SeatAllotment.objects.filter(
            opening_rank__lte=rank,
            closing_rank__gte=rank,
            gender=gender,
            category=category,
            year=year,
            round_no=round_number
        ).order_by('branch')

        context = {
            'cutoff_data': cutoff_data
        }

        return render(request, 'cutoff_analysis.html', context)

    return render(request, 'cutoff_analysis.html')

def branch_analysis(request):
    if request.method == 'POST':
        branch = request.POST.get('branch')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        year = int(request.POST.get('year'))
        round_number = request.POST.get('round_number')
        

        br_data = SeatAllotment.objects.filter(
            gender=gender,
            category=category,
            year=year,
            round_no=round_number,
            branch=branch
        )

        context = {
            'br_data': br_data
        }

        return render(request, 'branch_analysis.html', context)

    return render(request, 'branch_analysis.html')

def insti_analysis(request):
    if request.method == 'POST':
        Institute_name = request.POST.get('insti')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        year = int(request.POST.get('year'))
        round_number = int(request.POST.get('round_number'))
        

        insti_data = SeatAllotment.objects.filter(
            gender=gender,
            category=category,
            year=year,
            round_no=round_number,
            Institute_name=Institute_name
        )

        context = {
            'insti_data': insti_data
        }

        return render(request, 'insti_analysis.html', context)

    return render(request, 'insti_analysis.html')

def rank_analysis(request):
    if request.method == 'POST':
        Institute_name = request.POST.get('institute')
        gender = request.POST.get('gender')
        category=request.POST.get('category')
        branch = request.POST.get('branch')
        year = int(request.POST.get('year'))
        round_number = int(request.POST.get('round_number'))
        

        rank_data = SeatAllotment.objects.filter(
            gender=gender,
            branch=branch,
            category=category,
            year=year,
            round_no=round_number,
            Institute_name=Institute_name
        )

        context = {
            'rank_data': rank_data
        }

        return render(request, 'rank_analysis.html', context)

    return render(request, 'rank_analysis.html')

def year_wise_graph(request):
    return render(request, 'graph.html')

def get_year_wise_data(request):
    if request.method == 'POST':
        branch = request.POST.get('branch')
        Institute_name = request.POST.get('insti')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        round_number = request.POST.get('round_number')

        cutoff_data = SeatAllotment.objects.filter(branch=branch, Institute_name=Institute_name, gender=gender, category=category, round_no=round_number).order_by('year')
        years = []
        opening_ranks = []
        closing_ranks = []
        for entry in cutoff_data:
            years.append(entry.year)
            opening_ranks.append(entry.opening_rank)
            closing_ranks.append(entry.closing_rank)

        data = {
            'years': years,
            'opening_ranks': opening_ranks,
            'closing_ranks': closing_ranks,
        }

        return JsonResponse(data)

    return JsonResponse({'error': 'Invalid request method'})

def round_wise_graph(request):
    return render(request, 'rgraph.html')

def get_round_wise_data(request):
    if request.method == 'POST':
        branch = request.POST.get('branch')
        Institute_name = request.POST.get('insti')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        year = request.POST.get('year')

        cutoff_data = SeatAllotment.objects.filter(branch=branch, Institute_name=Institute_name, gender=gender, category=category, year=year).order_by('round_no')
        round_numbers = []
        opening_ranks = []
        closing_ranks = []
        for entry in cutoff_data:
            round_numbers.append(entry.round_no)
            opening_ranks.append(entry.opening_rank)
            closing_ranks.append(entry.closing_rank)

        data = {
            'round_numbers':round_numbers,
            'opening_ranks': opening_ranks,
            'closing_ranks': closing_ranks,
        }

        return JsonResponse(data)

    return JsonResponse({'error': 'Invalid request method'})
def generate_plot(request):
    if request.method == 'POST':
        import sqlite3
        import pandas as pd
        import numpy as np
        conn = sqlite3.connect('db.sqlite3')
        query = "SELECT * FROM josaapp_seatallotment"
        df = pd.read_sql_query(query, conn)
        conn.close()
        plt.xkcd()
        Institute_name = request.POST.get('insti')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        branch = request.POST.get('branch')
        boolean=(df['Institute_name']==Institute_name) & (df['branch']==branch) &(df['gender']==gender) & (df['category']==category)
        #print(boolean)
        x=df[boolean&(df['round_no']==1)]['year'] 
        lis=df.year.unique()
        x_indexes=np.arange(len(lis))
        width=.25
        y=df[boolean&(df['round_no']==1)]['closing_rank']
        #print(y)
        y_1=df[boolean&(df['round_no']==3)]['closing_rank']
        y_2=df[boolean&(df['round_no']==6)]['closing_rank']
        plt.plot(x, y,label='round_1')
        plt.plot(x, y_1,label='round_3')
        plt.plot(x, y_2,label='round_6')
        plt.title('My Plot')
        plt.legend()
        plt.grid(True, alpha=0.5)
        #plt.show()
        image_stream = io.BytesIO()
        plt.savefig(image_stream, format='png')
        plt.close()
        image_stream.seek(0)
        image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

        context = {
            'branch': branch,
            'Institute_name': Institute_name,
            'image': image_base64,
        }

        return render(request, 'plot.html', context)
   
    return render(request, 'plot.html')