# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "company_contacts"
app_title = "Company contacts"
app_publisher = "Bizimungu pascal"
app_description = "Managing the contacts for the companies"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "bizip04@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/company_contacts/css/company_contacts.css"
# app_include_js = "/assets/company_contacts/js/company_contacts.js"

# include js, css files in header of web template
# web_include_css = "/assets/company_contacts/css/company_contacts.css"
# web_include_js = "/assets/company_contacts/js/company_contacts.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "company_contacts/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "company_contacts.install.before_install"
# after_install = "company_contacts.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "company_contacts.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"company_contacts.tasks.all"
# 	],
# 	"daily": [
# 		"company_contacts.tasks.daily"
# 	],
# 	"hourly": [
# 		"company_contacts.tasks.hourly"
# 	],
# 	"weekly": [
# 		"company_contacts.tasks.weekly"
# 	]
# 	"monthly": [
# 		"company_contacts.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "company_contacts.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "company_contacts.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "company_contacts.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

