from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.Dashboards), name="Dashboards"),
    # path("adminn", login_required(views.Admin.as_view()), name="adminn"),
    path('attendance/', (views.Attendence), name='attendance'),
    # path("agent/", login_required(views.Agent.as_view()), name="agent"),
    path("agent/<pk>", login_required(views.DetailCalling), name="detail_agent"),
    path("sales/<pk>", login_required(views.DetailSales), name="detail_sales"),

    path("Attendence/", login_required(views.Attendence), name="attendance"),
    path("reports/", login_required(views.Admin_reports.as_view()), name="reports"),
    path("reports/MinerActivity/", login_required(views.MinerActivity.as_view()), name="MinerActivity"),
    # path("reports/DailyAttendence/", login_required(views.DailyAttendence.as_view()), name="DailyAttendence"),
    path("reports/MinerActivity/<pk>", login_required(views.EmployeeDetail.as_view()), name="EmployeeDetail"),
    path("reports/LeadsActivity/", login_required(views.LeadsActivity.as_view()), name="LeadsActivity"),
    path("reports/Analysis/", login_required(views.AdminAnalysis.as_view()), name="AdminAnalysis"),

    path("mining", login_required(views.mining_view), name = "mining"),
    path("data", login_required(views.DataView.as_view()), name = "data"),
    path("detail/<pk>", views.DetailDataView.as_view(), name = "detaildata"),
    path("call", views.CallView.as_view(), name = "call"),
    path("videocall", views.VideoCallView.as_view(), name = "videocall"),
    path("joinmeet", views.join_meet, name = "joinmeet"),
    path("createcontact", views.Create_contact_view, name = "create_contact"), 
    path("message", views.Message.as_view(), name = "message"), 
    path("createlead", views.Create_lead_view, name = "create_lead"), 
    path("lead_data", login_required(views.LeadView.as_view()), name = "lead_data"), 
    path("opportunity_data", login_required(views.OpportunityView.as_view()), name = "opportunity_data"), 
    path("createopportunity", views.Create_opportunity_view, name = "create_opportunity"), 
    path("createquote", views.Create_quote_view, name = "create_quote"), 
    path("rev", views.MiningsView.as_view(), name = "view"), 
    path("tocall", views.Tocall.as_view(), name = "tocall"), 
    path("tocall/<pk>", views.Tocall_detail, name = "tocalldata"),
    path("cc", views.get_calling_agents, name ="cc"),
    path('get_timer/', login_required(views.get_timer_value), name='get_timer'),
]







