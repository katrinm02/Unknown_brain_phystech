# import time
# 
# from django.test import TestCase
# # from django.urls import reverse
# 
# from pool.views import *
# from pool.models import PoolPending, PoolServices
# 
# 
# class QuestionModelTests(TestCase):
# 
#     def test_create(self):
#         register('ds', 12)
#         chl = PoolServices.objects.all()
#         self.assertIsNotNone(chl, "nomatch")
#         
#     def test_condition_endpoint_not_pool(self):
#         register('ds', 12)
#         register('ds', 11)
#         chl = PoolServices.objects.all().count()
#         self.assertEqual(chl, 1, 'has created')
#     
#     def test_delete_pool(self):
#         ticket = register('sd', 7)
#         unregister(ticket)
#         chl = PoolServices.objects.all().count()
#         self.assertEqual(chl, 0, 'oops')
#         
#     def test_update_state(self):
#         ticket = register('ds', 12)
#         update(ticket, 'SB')
#         for obj in PoolServices.objects.filter(ticket=ticket):
#             state = obj.state
#         self.assertEqual(state, 'SB', 'ou')
#         
#     def test_getWork_no_Available(self):
#         ticket = register('ds', 12)
#         update(ticket, 'SB')
#         res = getWork(12)
#         self.assertIsNone(res, 'available')
#         
#     def test_getWork_Available(self):
#         register('ds', 12)
#         res = getWork(12)
#         self.assertEqual(res, 'ds', 'error')
#         
#     def test_delete_pending(self):
#         register('ds', 12)
#         getWork(12)
#         time.sleep(39)
#         checkPending()
#         chl = PoolPending.objects.all().count()
#         self.assertEqual(chl, 1, 'time is over')
#         time.sleep(2)
#         checkPending()
#         chl = PoolPending.objects.all().count()
#         self.assertEqual(chl, 0, 'you still have time')
#         
#     def test_delete_old(self):
#         register('ds', 12)
#         time.sleep(59)
#         checkOld()
#         chl = PoolServices.objects.all().count()
#         self.assertEqual(chl, 1, 'time is over')
#         time.sleep(2)
#         checkOld()
#         chl = PoolServices.objects.all().count()
#         self.assertEqual(chl, 0, 'you still have time')

        
        