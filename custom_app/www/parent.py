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
	print "@#$%^&*()!@#$%^&*()"
	context.products = frappe.db.get_all("Item", filters={}, fields=["image", "item_name", "item_group","route"])
	context.product_list =[]
	for i in context.products:
		context.product_list.append(i)
	context.contact_info = frappe.db.get_all("Address", filters={}, fields="*")