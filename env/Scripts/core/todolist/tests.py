from django.test import TestCase
from django.urls import reverse
from .models import TodoItem

class TodoListViewTest(TestCase):
    def test_todo_list_view(self):
        # 테스트용 todo 아이템 생성
        item1 = TodoItem.objects.create(item_text='Test Item 1')
        item2 = TodoItem.objects.create(item_text='Test Item 2')

        # todo_list 뷰 호출
        response = self.client.get(reverse('todo_list'))

        # 응답 상태코드 확인
        self.assertEqual(response.status_code, 200)

        # 응답으로 받은 HTML에 아이템 텍스트가 있는지 확인
        self.assertContains(response, 'Test Item 1')
        self.assertContains(response, 'Test Item 2')

    def test_add_todo_item(self):
        # 아이템 추가를 위한 POST 요청
        response = self.client.post(reverse('todo_list'), {'item_text': 'New Test Item'})

        # 추가 후 리다이렉트 되는지 확인
        self.assertRedirects(response, reverse('todo_list'))

        # 추가된 아이템이 표시되는지 확인
        self.assertTrue(TodoItem.objects.filter(item_text='New Test Item').exists())

    def test_delete_todo_item(self):
        # 테스트용 아이템 생성
        item = TodoItem.objects.create(item_text='Test Item')

        # 아이템 삭제를 위한 POST 요청
        response = self.client.post(reverse('delete_item', args=[item.pk]))

        # 삭제 후 리다이렉트 되는지 확인
        self.assertRedirects(response, reverse('todo_list'))

        # 삭제된 아이템이 데이터베이스에 존재하지 않는지 확인
        self.assertFalse(TodoItem.objects.filter(item_text='Test Item').exists())

    def test_edit_todo_item(self):
        # 테스트용 아이템 생성
        item = TodoItem.objects.create(item_text='Test Item')

        # 수정을 위한 POST 요청
        response = self.client.post(reverse('edit_item', args=[item.pk]), {'item_text': 'Updated Test Item'})

        # 수정 후 리다이렉트 되는지 확인
        self.assertRedirects(response, reverse('todo_list'))

        # 수정된 텍스트가 데이터베이스에 반영되었는지 확인
        updated_item = TodoItem.objects.get(pk=item.pk)
        self.assertEqual(updated_item.item_text, 'Updated Test Item')
