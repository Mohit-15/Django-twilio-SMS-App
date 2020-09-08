from django.db import models
from django.utils.translation import ugettext_lazy as _
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


# Create your models here.
class ContactForm(models.Model):
	name = models.CharField(max_length = 40, verbose_name = "name")
	email = models.EmailField(max_length = 100, verbose_name = "email")
	phone = models.CharField(max_length = 14, blank = False, verbose_name = "phone")
	subject = models.CharField(max_length = 40)
	query = models.TextField(verbose_name = "query")
	ref_number = models.CharField(max_length = 20, verbose_name = "ref_number", blank = True)
	qr_code = models.ImageField(upload_to = 'codes_media', blank = True)

	class Meta:
		verbose_name = _('ContactForm')
		verbose_name_plural = _('ContactForms')

	def __str__(self):
		return str(self.subject)

	def save(self, *args, **kwargs):
		qrcodes =  qrcode.make(self.ref_number)
		canvas = Image.new('RGB', (290,290), "white")
		draw = ImageDraw.Draw(canvas)
		canvas.paste(qrcodes)
		fname = f'qr_code-{self.name}.png'
		buff = BytesIO()
		canvas.save(buff, 'PNG')
		self.qr_code.save(fname, File(buff), save = False)
		canvas.close()
		super().save(*args, **kwargs)
