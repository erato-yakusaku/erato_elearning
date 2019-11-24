# image_formats.py
from wagtail.images.formats import Format, register_image_format

register_image_format(Format('thumbnail', 'Thumbnail', 'richtext-image thumbnail', 'fill-120x120'))
register_image_format(Format('default', 'Default', 'richtext-image default', 'fill-300x200'))
register_image_format(Format('middium', 'Middium', 'richtext-image middium', 'fill-450x300'))
register_image_format(Format('large', 'Large', 'richtext-image large', 'fill-600x400'))