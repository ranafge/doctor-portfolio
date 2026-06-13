from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = "ডা. শাহ আলম — অ্যাডমিন প্যানেল"
    site_title = "ডা. শাহ আলম"
    index_title = "স্বাগতম! সব মডিউল এখানে পরিচালনা করুন।"

admin_site = CustomAdminSite(name="custom_admin")
