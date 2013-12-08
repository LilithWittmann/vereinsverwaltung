# Print Templates 

## Possible Data Types

You may use `.html` or `.txt`.
Please make shure, that you don't have any external assets (like images).
If you want to include images convert them to a [data-url](http://dataurl.net/#dataurlmaker) and set them as `src`

## Placeholder

### Member

* {{member.forename}}
* {{member.surname}}
* {{member.phone}}
* {{member.email}}
* {{member.street}}
* {{member.postal_code}}
* {{member.city}}
* {{member.iban}}
* {{member.bic}}
* {{member.next_pay_date}}
* {{member.yearly_amount}}
* {{member.created_at}}
* {{member.updated_at}}

### Current Date

* {{data}}

Format the date via: {{date|date:"d.m.Y"}}.

[more info](https://docs.djangoproject.com/en/1.0/ref/templates/builtins/)