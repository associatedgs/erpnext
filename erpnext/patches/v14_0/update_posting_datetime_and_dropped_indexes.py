import frappe


def execute():
	frappe.db.sql(
		"""
		UPDATE `tabStock Ledger Entry`
			SET posting_datetime = timestamp(posting_date, posting_time)
	"""
	)

	drop_indexes()


def drop_indexes():
	if not frappe.db.has_index("tabStock Ledger Entry", "posting_sort_index"):
		return

	frappe.db.sql_ddl("ALTER TABLE `tabStock Ledger Entry` DROP INDEX `posting_sort_index`")
