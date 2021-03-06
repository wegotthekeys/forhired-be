from os.path import abspath, join, dirname
from shutil import rmtree
from tempfile import mkdtemp
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import SimpleUploadedFile, UploadedFile
from django.urls import reverse
from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings
from api.models import Resume
from proj.settings import AWS_S3_ACCESS_KEY_ID, AWS_S3_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
import boto3
import mock


class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.media_folder = mkdtemp()

    def tearDown(self):
        rmtree(self.media_folder)

    def test_post_resume(self):
        resume_path = join(abspath(dirname(__file__)),
                           'fixtures/DanielSlapelisResume-2019.docx')
        resume = Resume()
        resume.name = 'oogity boogity'
        resume.resume = UploadedFile(open(resume_path, 'rb'))
        resume.save()
