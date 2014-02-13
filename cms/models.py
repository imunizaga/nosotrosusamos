from django.db import models

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

    def parse_tags(self, commit=False):
        def tag_replace(match):
            title = match.group(1)
            path = match.group(2)
            link = match.group(3)

            if not path:
                path = ""

            tag = Tag.objects.get(title__iexact=title)
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

    #public methods
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
