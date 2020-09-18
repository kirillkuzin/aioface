from aioface import MemoryStorage


memory_storage = MemoryStorage()


class TestMemoryStorage:
    def test_memory_storage(self):
        data = memory_storage.get_data('0')
        assert data == {}
        memory_storage.set_data('0', {'foo': 'bar'})
        data = memory_storage.get_data('0')
        assert data == {'foo': 'bar'}
        memory_storage.update_data('0', {'baz': 'qux'})
        data = memory_storage.get_data('0')
        assert data == {'foo': 'bar', 'baz': 'qux'}
        memory_storage.set_data('0', {'foo': 'bar'})
        data = memory_storage.get_data('0')
        assert data == {'foo': 'bar'}
        memory_storage.reset_data('0')
        data = memory_storage.get_data('0')
        assert data == {}
