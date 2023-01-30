from django.test import TestCase
from .models import Postblog
from django.contrib.auth.models import User
from django.shortcuts import reverse

class BlogPostTest (TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')

        cls.post1 = Postblog.objects.create( #pub
                    title  = 'Post1' ,
                    text   = 'This is the describtion for Post1',
                    status = Postblog.STATUS_CHOICES[0][0],
                    author = cls.user,    
                )
        cls.post2 = Postblog.objects.create( #drf
                    title  = 'Post2' ,
                    text   = 'This is the describtion for Post2',
                    status = Postblog.STATUS_CHOICES[1][0],
                    author = cls.user,    
                )       

    # def setUp(self):
    #     self.user = User.objects.create(username='user1')
        
    #     self.post1 = Postblog.objects.create( #pub
    #                 title  = 'Post1' ,
    #                 text   = 'This is the describtion for Post1',
    #                 status = Postblog.STATUS_CHOICES[0][0],
    #                 author = self.user,    
    #             )
    #     self.post2 = Postblog.objects.create( #drf
    #                 title  = 'Post2' ,
    #                 text   = 'This is the describtion for Post2',
    #                 status = Postblog.STATUS_CHOICES[1][0],
    #                 author = self.user,    
    #             )       
        
    #Unit tests
    
    def test_post_list_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        
    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)
    
    def test_post_detail_url(self):
        response = self.client.get(f'/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)
        
    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.pk]))
        self.assertContains(response, self.post1.title)   
    
    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id])) 
        # response = self.client.get(f'/{self.post1.id}/')
        self.assertContains(response,self.post1.title)
        self.assertContains(response,self.post1.text)

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[998])) 
        self.assertEqual(response.status_code, 404)
        
    def test_draft_post_not_show_in_posts_list(self):   #TDD - Test Driven Development
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)