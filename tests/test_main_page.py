from blog.templatetags.main_page import get_default_picture


def test_get_default_picture(link=None):
    assert get_default_picture('blog/800x400_2.jpeg') == 'media/blog/800x400_2.jpeg'
    assert get_default_picture('') == 'static/img/not found.jpg'
    assert get_default_picture(None) == 'static/img/not found.jpg'

