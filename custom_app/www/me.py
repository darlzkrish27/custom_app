from __future__ import unicode_literals
import frappe
from frappe import _
import frappe.www.list

no_cache = 1
no_sitemap = 1

def get_context(context):
	if frappe.session.user=='Guest':
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

	# context.show_sidebar=True
	context.company = frappe.db.get_single_value("Global Defaults", "default_company")
	company = frappe.db.get_all("Company", filters={'company_name':context.company}, fields="*")
	context.email = company[0]['email']
	context.country = company[0]['country']
	context.logo = company[0]['company_logo']
	context.phone = company[0]['phone_no']
	
	context.top_bar = frappe.db.get_all("Top Bar Item", filters={}, fields=["label","parent_label","url"])
	from collections import defaultdict
	x = defaultdict(list)
	for d in context.top_bar:
		if d[u'parent_label'] is not None:
			x[d[u'parent_label']].append([d[u'label'], d[u'url']])
	context.top = x
	context.product_group =[]
	context.group = 'Products'
	for product in context.top:
		if product =='Products':
			for i in context.top[product]:
				context.product_group.append(i[0])
	context.user = frappe.session.user