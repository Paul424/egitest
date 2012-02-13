"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from nespresso.models import *
from django.test.client import Client

class OrderTest(TestCase):
    
    fixtures = ['test_nespresso.json']
    
    #def setUp(selfself):
        #print "setUp"
        
    #def tearDown(self):
        #print "teardown"
                
    def test_q(self):
        """
        Tests how many cups cheaper than...
        """
        q = cups.objects.filter(cost__lt=0.36) 
        self.assertEqual(q.count(), 2)
        
    def test_request_response(self):
        """
        Tests how many cups cheaper than...
        """
        c = Client()
        r = c.get('/cups/')
        self.assertEqual(r.status_code, 200)
        
        #this test is useless!
        #a next real test would be to open a view with a request object en test the response.
        #such test really includes the business logic!
        