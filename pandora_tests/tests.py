from django.test import TestCase
from pandora import Box


class BoxTests(TestCase):
    def test_get_set_item(self):
        box = Box()
        box['foo'] = 1
        self.assertEqual(box['foo'], 1)

    def test_get_method(self):
        box = Box()
        self.assertEqual(box.get('foo', 0), 0)
        box['foo'] = 1
        self.assertEqual(box.get('foo', 0), 1)

    def test_del_item(self):
        box = Box()
        box['foo'] = True
        del box['foo']
        self.assertRaises(KeyError, box.__getitem__, 'foo')

    def test_contains(self):
        box = Box()
        self.assertFalse('foo' in box)
        box['foo'] = 1
        self.assertTrue('foo' in box)

    def test_missing_key(self):
        box = Box()
        self.assertRaises(KeyError, box.__getitem__, 'foo')

    def test_delete_missing_key(self):
        box = Box()
        self.assertRaises(KeyError, box.__delitem__, 'foo')

    def test_multiple_boxes(self):
        box1 = Box()
        box2 = Box()

        bar1 = object()
        box1['foo'] = bar1

        bar2 = object()
        box2['foo'] = bar2

        self.assertTrue(box1['foo'] is bar1)
        self.assertTrue(box2['foo'] is bar2)


class MultiThreadedTests(TestCase):
    '''
    Please contribute a patch if you know how to easily test the multithreaded
    behaviour of pandora's box.
    '''
