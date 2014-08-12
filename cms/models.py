from django.contrib import messages
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.sites.models import get_current_site

# models
from base.models import BaseModel

# standard library
import re


class Interview(BaseModel):
    def file_path(self, name):
        """ file path for the file obj """
        return "%s" % name
    tags = models.ManyToManyField(
        'Tag', related_name='interviews', editable=False,
    )

    title = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        unique=True, null=True, blank=True,
    )
    summary = models.TextField(
    )
    who_you_are = models.TextField(
    )
    what_hardware = models.TextField(
    )
    what_software = models.TextField(
    )
    dream_setup = models.TextField(
    )
    picture = models.ImageField(
        upload_to=file_path, null=True, blank=True,
    )
    active = models.BooleanField(
        default=False,
    )

    image_sizes = [
        (265, 170),
        (530, 340),
    ]

    title_regex = '([\w\s\-\.\/]+)'

    class Meta:
        ordering = ['-created_at']

    def parse_tags(self, commit=False, request=None):
        def tag_replace(match):
            title = match.group(1)
            path = match.group(2)
            link = match.group(3)

            if not path:
                path = ""

            try:
                tag = Tag.objects.get(title__iexact=title)
            except:
                if request and request.user.has_perm('admin'):
                    messages.add_message(
                        request, messages.ERROR,
                        _('Tag "{}" does not Exist').format(title)
                    )
                return
            if commit:
                self.tags.add(tag)

            if not link:
                link = tag.link
            else:
                link = link[1:-1]

            return '[{}]({}{})'.format(tag.title, link, path)

        if commit:
            self.tags.remove()

        search = '\[{}!!!([\w/]+)?\](\([\w/:\.]+\))?'.format(self.title_regex)

        self.who_you_are = re.sub(search, tag_replace, self.who_you_are)
        self.what_hardware = re.sub(search, tag_replace, self.what_hardware)
        self.what_software = re.sub(search, tag_replace, self.what_software)
        self.dream_setup = re.sub(search, tag_replace, self.dream_setup)

    def search_tags(self):
        def tag_replace(match):
            title = match.group(1)
            link = match.group(2)

            try:
                tag = Tag.objects.get(
                    title__iexact=title,
                    link=link,
                )
            except:
                return '[{}]({})'.format(title, link)

            return '[{}!!!]'.format(tag.title)

        self.tags.remove()

        search = '\[{}\]\(([:\w\./]+)\)'.format(self.title_regex)

        self.update(who_you_are=re.sub(search, tag_replace, self.who_you_are))
        self.update(what_hardware=re.sub(search, tag_replace,
                                         self.what_hardware))
        self.update(what_software=re.sub(search, tag_replace,
                                         self.what_software))
        self.update(dream_setup=re.sub(search, tag_replace, self.dream_setup))

    # public methods
    def save(self, *args, **kwargs):
        """
        Interview save method, overriden to set the picture size
        """

        super(Interview, self).save(*args, **kwargs)

        self.search_tags()

        try:
            self._process_image('picture')
        except:
            pass

        self.parse_tags(commit=True)


class Category(BaseModel):
    title = models.CharField(
        max_length=255,
    )

    def __unicode__(self):
        return self.title


class Tag(BaseModel):
    categories = models.ManyToManyField(
        Category, related_name='tags',
    )
    title = models.CharField(
        max_length=255,
    )
    link = models.URLField(
        blank=True, null=True,
    )

    def __unicode__(self):
        return self.title


class InterviewImage(BaseModel):
    def folder_path(self):
        return "interviews/%d/images/" % self.interview_id

    def file_path(self, name):
        """ file path for the file obj """
        return u"{}{}".format(self.folder_path(), name)

    image_sizes = (
        (0, 250),  # detail carousel
        (220, 220),  # index small
        (940, 330),  # index carousel
    )

    # foreign keys
    interview = models.ForeignKey(
        Interview, related_name="images",
        help_text=_("The interview of this image."),
    )

    interview = models.ForeignKey(
        Interview, related_name="images",
        help_text=_("The interview of this image."),
    )
    picture = models.ImageField(
        upload_to=file_path,
        null=True,
        blank=True,
        verbose_name=_("picture"),
    )
    caption_header = models.CharField(
        max_length=100,
    )
    caption_body = models.CharField(
        max_length=255,
    )

    # auto fields
    order = models.PositiveSmallIntegerField(
        default=0,
        help_text=_("The order in which this image appears"))

    def __unicode__(self):
        return u"%d-%d" % (self.interview_id, self.id)

    def save(self, process_image=True, *args, **kwargs):
        """ override the interview save method to transform the uploaded images
        to jpg to reduce it's file size

        """
        super(InterviewImage, self).save(*args, **kwargs)
        if process_image:
            self._process_image('picture')

    def get_image_url(self, field_name, width=None, height=None, request=None):
        picture = getattr(self, field_name)

        if picture:
            file_path = str(picture)
            if width and height:
                width = str(width)
                height = str(height)
                path = file_path.split('.')

                # update the path
                file_path = "{}-{}.{}".format(".".join(path[0:-1]),
                                              "".join((width, "x", height)),
                                              path[-1])

            if request:
                current_site = "http://%s" % get_current_site(request)
            else:
                current_site = ""
            return "%s%s%s" % (current_site, settings.MEDIA_URL, file_path)

    class Meta:
        verbose_name_plural = _('interview images')
        verbose_name = _('interview image')
        ordering = ['order']
