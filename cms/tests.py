"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


from base.tests import BaseTestCase


class InterviewTests(BaseTestCase):
    def test_parse_tags(self):
        """
        Tests tthat the parse_tags method creates the expected tags
        """

        category = self.create_category()

        tag1 = self.create_tag()
        tag2 = self.create_tag()
        tag3 = self.create_tag()
        tag4 = self.create_tag()

        tag1.categories.add(category)
        tag2.categories.add(category)
        tag3.categories.add(category)

        path2 = '/hello'
        path4 = '/hello/asdf'

        link3 = "http://magnet.cl"
        link4 = "http://google.cl"

        interview = self.create_interview(
            who_you_are="[{}!!!]".format(tag1.title),
            what_hardware="[{}!!!{}]".format(tag2.title, path2),
            what_software="[{}!!!]({})".format(tag3.title, link3),
            dream_setup="[{}!!!{}]({})".format(tag4.title, path4, link4),
        )

        self.assertEqual(interview.tags.count(), 4)
        self.assertEqual(
            interview.who_you_are,
            '[{}]({})'.format(tag1.title, tag1.link)
        )
        self.assertEqual(
            interview.what_hardware,
            '[{}]({}{})'.format(tag2.title, tag2.link, path2)
        )
        self.assertEqual(
            interview.what_software,
            '[{}]({})'.format(tag3.title, link3)
        )
        self.assertEqual(
            interview.dream_setup,
            '[{}]({}{})'.format(tag4.title, link4, path4)
        )

    def test_search_tags(self):
        """
        Tests tthat the parse_tags method creates the expected tags
        """

        category = self.create_category()

        tag = self.create_tag()

        tag.categories.add(category)

        interview = self.create_interview(
            who_you_are="[{}]({})".format(tag.title, tag.link),
        )

        self.assertEqual(interview.tags.count(), 1)
