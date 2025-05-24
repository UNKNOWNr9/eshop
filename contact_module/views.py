from django.views.generic import TemplateView


class ContactUs(TemplateView):
    template_name = 'contact_module/contact_us.html'