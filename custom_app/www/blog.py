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

	context.user = frappe.session.user

	context.blog_post = frappe.db.get_all("Blog Post", filters={}, fields="*")