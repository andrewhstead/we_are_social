# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from accounts.views import profile, login, register
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from .forms import UserRegistrationForm
from django import forms
from django.conf import settings
from .models import User


class CustomUserTest(TestCase):

    def test_manager_create(self):
        user = User.objects._create_user(None, "test@test.com",
                                         "password",
                                         False, False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password",
                                             False, False)

    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })

        self.assertTrue(form.is_valid())

    def test_missing_password_1(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password2': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_missing_password_2(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'letmein1',
            'password2': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein3',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

# class RegisterTest(TestCase):
#     def test_register_page_resolves(self):
#         register_page = resolve('/register/')
#         self.assertEqual(register_page.func, register)
#
#     def test_register_page_status_code_is_ok(self):
#         register_page = self.client.get('/register/')
#         self.assertEqual(register_page.status_code, 200)
#         register_page_template_output = render_to_response("register.html").content
#         self.assertEqual(register_page.content, register_page_template_output)
#
#
# class ProfileTest(TestCase):
#     def test_profile_page_resolves(self):
#         profile_page = resolve('/profile/')
#         self.assertEqual(profile_page.func, profile)
#
#     def test_profile_page_status_code_is_ok(self):
#         profile_page = self.client.get('/profile/')
#         self.assertEqual(profile_page.status_code, 200)
#         self.assertTemplateUsed(profile_page, "profile.html")
#         profile_page_template_output = render_to_response("profile.html").content
#         self.assertEqual(profile_page.content, profile_page_template_output)
#
#
# class LoginPageTest(TestCase):
#     def test_login_page_resolves(self):
#         login_page = resolve('/login/')
#         self.assertEqual(login_page.func, login)
#
#     def test_login_page_status_code_is_ok(self):
#         login_page = self.client.get('/login/')
#         self.assertEqual(login_page.status_code, 200)

