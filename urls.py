#from django.conf.urls import include , url
from django.urls import path
from django.conf import settings

from . import views
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView



urlpatterns = [
    path('',views.index, name = 'index'),
    path('AddBasespaceLibrary/',views.add_basespace_library, name='add_basespace_library'),
    path('AddCommercialKit', views.add_commercial_kit, name='add_commercial_kit'),
    path('AddIndexLibrary', views.add_index_library, name = 'add_index_library'),
    path('AnnualReport/',views.annual_report, name='annual_report'),
    path('change_project_libKit=<int:project_id>',views.change_project_libKit, name ='change_project_libKit'),
    path('change_run_libKit=<int:run_id>',views.change_run_libKit, name ='change_run_libKit'),
    path('ChangeRunName=<int:run_id>',views.change_run_name, name='change_run_name'),
    path('createNextSeqRun/', views.create_nextseq_run, name='create_nextseq_run'),
    path('createProtocol', views.create_protocol, name = 'create_protocol'),
    path('configurationTest/', views.configuration_test, name='configuration_test'),
    path('defineProtocolParameters=<int:protocol_id>', views.define_protocol_parameters, name = 'define_protocol_parameters'),
    path('DisplayIndexLibrary=<int:index_library_id>/', views.display_index_library, name= 'display_index_library'),
    path('displayProject=<int:project_id>/', views.display_project, name='display_project'),
    path('displayProtocol=<int:protocol_id>', views.display_protocol, name = 'display_protocol'),
    path('displayRun=<int:run_id>/', views.display_run, name='display_run'),
    path('displaySample=<int:sample_id>/', views.display_sample, name= 'display_sample'),
    path('latest_run/',views.latest_run, name='latest_run'),
    path('incompletedRuns', views.incompleted_runs, name = 'incompleted_runs'),
    path('MonthlyReport/', views.monthly_report, name='montly_report'),
    path('QuarterReport/', views.quarter_report, name='quarter_report'),
    path('recordSample', views.record_sample, name='record_sample'),
    path('register_wetlab/',views.register_wetlab, name='register_wetlab'),
    path('searchIndexLibrary', views.search_index_library, name='search_index_library'),
    path('searchProject/', views.search_project, name ='search_project'),
    path('searchRun/', views.search_run, name='search_run'),
    path('searchSample/', views.search_sample, name = 'search_sample'),
    path('setDNAValues', views.set_DNA_values, name = 'set_DNA_values'),
    path('setLibraryValues', views.set_library_values, name = 'set_library_values'),
    path('StatsExperiment/', views.stats_experiment, name ='stats_experiment'),
    path('StatsLibrary/', views.stats_per_library , name ='stats_per_library'),
    path('StatsPerResearcher/',views.stats_per_researcher, name='stats_per_researcher'),
    path('StatsPerTime/', views.stats_per_time, name ='stats_per_time'),
    path('updateSamples', views.update_samples, name = 'update_samples'),
    path('updateTables/',views.update_tables, name='update_tables'),
    path('updateTablesDate/',views.update_tables_date, name='update_tables_date'),


]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
