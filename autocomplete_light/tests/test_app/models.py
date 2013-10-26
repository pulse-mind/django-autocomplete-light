from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

try:
    from genericm2m.models import RelatedObjectsDescriptor
except ImportError:
    RelatedObjectsDescriptor = None


@python_2_unicode_compatible
class FkModel(models.Model):
    name = models.CharField(max_length=200)

    fk = models.ForeignKey('self', related_name='reverse_fk',
            null=True, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class OtoModel(models.Model):
    name = models.CharField(max_length=200)

    oto = models.OneToOneField('self', related_name='reverse_oto',
            null=True, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MtmModel(models.Model):
    name = models.CharField(max_length=200)

    mtm = models.ManyToManyField('self', related_name='reverse_mtm',
            blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class GfkModel(models.Model):
    name = models.CharField(max_length=200)

    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    gfk = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name


if RelatedObjectsDescriptor:
    @python_2_unicode_compatible
    class GmtmModel(models.Model):
        name = models.CharField(max_length=200)

        gmtm = RelatedObjectsDescriptor()

        def __str__(self):
            return self.name


'''
Maybe I'll need this one ?

@python_2_unicode_compatible
class FullModel(models.Model):
    name = models.CharField(max_length=200)

    oto = models.OneToOneField('self', related_name='reverse_oto')
    fk = models.ForeignKey('self', related_name='reverse_fk')
    mtm = models.ManyToManyField('self', related_name='reverse_mtm')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    gfk = generic.GenericForeignKey("content_type", "object_id")

    if RelatedObjectsDescriptor:
        gmtm = RelatedObjectsDescriptor()

    def __str__(self):
        return self.name
'''
