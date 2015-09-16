from datetime import datetime
from django import template

register = template.Library()

@register.filter(name='check_date')
def check_date(date):

	if date > datetime.now():
		return False
	else:
		return True