import datetime
from unittest import skip

from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Artist, Painting, Technique, Support


class TestSupportModel(TestCase):

    def setUp(self):
        Support.objects.create(name='testsupport')

    def test_support_model_input(self):
        test = Support.objects.get(name='testsupport')
        self.assertTrue(isinstance(test, Support))

    def test_support_model_return(self):
        test = Support.objects.get(name='testsupport')
        self.assertEqual(str(test), 'testsupport')


class TestTechniqueModel(TestCase):

    def setUp(self):
        Technique.objects.create(name='testtechnique')

    def test_technique_model_input(self):
        test = Technique.objects.get(name='testtechnique')
        self.assertTrue(isinstance(test, Technique))

    def test_technique_model_return(self):
        test = Technique.objects.get(name='testtechnique')
        self.assertEqual(str(test), 'testtechnique')


class TestArtistModel(TestCase):

    def setUp(self):
        user = User.objects.create(username='luis')
        Artist.objects.create(user=user)

    def test_artist_model_input(self):
        test = Artist.objects.get(user__username='luis')
        self.assertTrue(isinstance(test, Artist))

    def test_artist_model_return(self):
        test = Artist.objects.get(user__username='luis')
        self.assertEqual(str(test), 'luis')


# @skip("skip this")
class TestPaintingModel(TestCase):

    def setUp(self):
        user = User.objects.create(username='luis')
        support = Support.objects.create(name='testsupport')
        technique = Technique.objects.create(name='testtechnique')
        artist = Artist.objects.create(user=user)
        Painting.objects.create(name='testpainting', pub_date=datetime.datetime.now(), support=support, artist=artist,
                                technique=technique, pheight=2, pwidth=2)

    def test_painting_model_input(self):
        test = Painting.objects.get(name='testpainting')
        self.assertTrue(isinstance(test, Painting))

    def test_painting_model_return(self):
        test = Painting.objects.get(name='testpainting')
        self.assertEqual(str(test), 'testpainting')
