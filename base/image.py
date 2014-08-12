# -*- coding: utf-8 -*-
""" Image operations. """

from PIL import Image, ImageFile
from PIL.ImageOps import fit

from os.path import exists, splitext


def generate_thumbnail(file_path, size, bounds=None, force=False, img=None):
    """ Fits image to the given size in order to generate its thumbnail.

    Keyword arguments:
    file_path -- absolute path of file
    size -- int tuple, for example (200, 200)

    """
    (thumbnail_path, file_extension) = splitext(file_path)
    thumbnail_path = '%s-%sx%s%s' % (thumbnail_path, size[0], size[1],
                                     file_extension)
    if not exists(thumbnail_path) or force:
        # allow truncated images
        ImageFile.LOAD_TRUNCATED_IMAGES = True

        if img is None:
            img = Image.open(file_path)

        if bounds:
            img = img.crop(bounds)

        if size[0] and size[1]:
            thumbnail = fit(img, size, Image.ANTIALIAS)
            thumbnail.save(thumbnail_path)
        else:
            x, y = size
            if not size[0]:
                x = img.size[0]
            if not size[1]:
                y = img.size[1]
            size = (x, y)
            img.thumbnail(size, Image.ANTIALIAS)
            img.save(thumbnail_path)
