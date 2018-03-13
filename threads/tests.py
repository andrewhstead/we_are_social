# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Subject


# Create your tests here.
class ForumHomeTest(TestCase):

    fixtures = ['subjects', 'user']

    def test_home_page_status_code_is_ok(self):
        forum_home_page = self.client.get('/forum/')
        self.assertEqual(forum_home_page.status_code, 200)

    def test_check_content_is_correct(self):
        forum_home_page = self.client.get('/forum/')
        self.assertTemplateUsed(forum_home_page, "forum/forum.html")
        forum_home_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects': Subject.objects.all()}).content
        self.assertEqual(forum_home_page.content, forum_home_page_template_output)
