from __future__ import unicode_literals
import frappe

no_cache = 1
no_sitemap = 1

def get_context(context):
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
	
	# slides = frappe.db.get_all("Website Slideshow", filters={'slideshow_name': 'Website Home Slide Show'}, fields="*")
	# filter it through the website slideshow parenttype name
	context.slides = frappe.db.get_all("Website Slideshow Item", filters={'parent':'Website Home Slide Show'}, fields="*")
	context.blog = frappe.db.get_all("Blog Post", filters={}, fields="*")[:3]

	context.products = frappe.db.get_all("Item", filters={}, fields=["image", "item_name", "item_group","route","show_on_homepage","ordering"])
	context.my_list =[]
	for i in context.products:
		if i['show_on_homepage']==1:
			context.my_list.append(i)
	context.product_list = sorted(context.my_list, key=lambda d: d[u'ordering'], reverse=True)[:3]

	context.team  = frappe.db.get_all("About Us Team Member", filters={}, fields="*")

	context.contact_form = frappe.db.get_all("Web Form",filters={'title':'Contact us'},fields="*")
	context.contact_info = frappe.db.get_all("Address", filters={}, fields="*")
	# context.contact_form = frappe.db.get_all("Web Form Fields",filters={'title':'Contact us'},fields="*")
	# context.contact_form = context.contact_form[0]
	context.user = frappe.session.user