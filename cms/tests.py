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

        tag1 = self.create_tag()
        tag2 = self.create_tag()
        tag3 = self.create_tag()

        path2 = '/hello'
        path3 = '/hello/123'

        interview = self.create_interview(
            who_you_are="[{}!!!]".format(tag1.title),
            what_hardware="[{}!!!{}]".format(tag2.title, path2),
            what_software="[{}!!!{}]".format(tag3.title, path3),
        )

        self.assertEqual(interview.tags.count(), 3)
        self.assertEqual(
            interview.what_hardware,
            '[{}{}]({})'.format(tag2.title, tag2.link, path2)
        )
