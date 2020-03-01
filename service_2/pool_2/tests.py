# from django.test import TestCase
# 
# # Create your tests here.
# from .views import *
# from .models import PoolCompare, ResultPoolService
# 
# class QuestionModelTests(TestCase):
#     
#     def test_put_pool(self):
#         put('as', 12)
#         put('asd', 13, 'ugyda')
#         list_c = ResultPoolService.objects.all().count()
#         self.assertEqual(list_c, 2, 'error')
#         
#     def test_compare_not_exist(self):
#         PoolCompare(result_pool=1, service_pool=3).save()
#         subscribe(1, 2)
#         list_c = PoolCompare.objects.all().count()
#         self.assertEqual(list_c, 2, 'not_created')
#     
#     def test_compare_exist(self):
#         PoolCompare(result_pool=1, service_pool=3).save()
#         subscribe(1, 3)
#         list_c = PoolCompare.objects.all().count()
#         self.assertEqual(list_c, 1, 'has_created')
#         
#     def test_delete_exist(self):
#         PoolCompare(result_pool=1, service_pool=3).save()
#         unsubscribe(1, 3)
#         list_c = PoolCompare.objects.all().count()
#         self.assertEqual(list_c, 0, 'hasnot_deleted')
#         
#     def test_get_subscription_yes(self):
#         PoolCompare(result_pool=1, service_pool=3).save()
#         res = get_subscriptions(1)
#         self.assertEqual(res, 3, "error")
#         
#     def test_get_subscription_no(self):
#         PoolCompare(result_pool=1, service_pool=3).save()
#         res = get_subscriptions(2)
#         self.assertIsNone(res, 'error')
#         
#     def test_delete_not_exist(self):
#         PoolCompare(result_pool=1, service_pool=3).save()
#         unsubscribe(2, 3)
#         list_c = PoolCompare.objects.all().count()
#         self.assertEqual(list_c, 1, 'has_deleted')
#         
#     def test_get_pool_with_ticket(self):
#         put('as', 12, 'qwerty')
#         res = get(12, 'qwerty')
#         list_c = ResultPoolService.objects.all().count()
#         self.assertEqual(list_c, 0, 'hasnot_deleted')
#         self.assertIsNotNone(res, 'is_none')
#         
#     def test_get_pool_without_ticket(self):
#         put('as', 12)
#         res = get(12)
#         list_c = ResultPoolService.objects.all().count()
#         self.assertEqual(list_c, 0, 'hasnot_deleted')
#         self.assertIsNotNone(res, 'is_none')
#         
#     def test_get_pool_false(self):
#         put('as', 12)
#         res = get(11)
#         list_c = ResultPoolService.objects.all().count()
#         self.assertEqual(list_c, 1, 'has_deleted')
#         self.assertIsNone(res, 'is_none')
        