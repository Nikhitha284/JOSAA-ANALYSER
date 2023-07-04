from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name='home'),
    path('seat-allotments/',views.seat_allotment_list, name='seat_allotment_list'),
    path('cutoff/', views.cutoff_analysis, name='cutoff_analysis'),
    path('branchanalyser/',views.branch_analysis,name='branch_analysis'),
    path('instianalyser/',views.insti_analysis,name='insti_analysis'),
    path('rankanalyser/',views.rank_analysis,name="rank_analysis"),
    path('graph/',views.year_wise_graph,name="chart_year_graph"),
    path('get-chart-data/', views.get_year_wise_data, name='get_chart_data'),
    path('rgraph/',views.round_wise_graph,name="chart_round_graph"),
    path('get-round-chart-data/', views.get_round_wise_data, name='get_round_chart_data'),
    path('plot/',views.generate_plot,name="generate_plot"),
    path('cloud/', views.cloud, name='cloud'),
     path('logo/', views.logo, name='logo'),
    path('wall/', views.wall, name='wall'),
    path('wall_2/', views.wall_2, name='wall_2'),
]