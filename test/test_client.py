from   mock import mock
import requests
import six

from ihan import eprint, group, feed_file

if six.PY2:
    import unittest2 as unittest
else:
    import unittest




def mocked_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = 200

        def json(self):
            return self.json_data

    return MockResponse({"lines": 1}, 200)


class TestClient(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_eprint_to_stderr(self):
        with mock.patch('sys.stderr',
                        new_callable=six.StringIO) as mock_stderr:
            eprint('Test')
            stderr_ = mock_stderr.getvalue().rstrip()
            self.assertEqual('Test', stderr_)

    def test_group(self):
        out = group(3, [x for x in range(0, 6)])
        self.assertEqual([0, 1, 2], list(next(out)))

    @mock.patch('subprocess.Popen')
    def test_compressed_unsupported(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'stdout.readline.return_value': unichr(190)}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        with self.assertRaises(UnicodeEncodeError):
            feed_file('test', False, 10, '', 0)
        self.assertTrue(mock_subproc_popen.called)

    @mock.patch('subprocess.Popen')
    def test_send_payload(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'stdout.readline.return_value': 'Test\n'}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        @mock.patch('requests.post', side_effect=mocked_post)
        def test_post(self, mock_get):
            feed_file('test', False, 1, '', 0)
            self.assertTrue(mock_subproc_popen.called)

    @mock.patch('subprocess.Popen')
    @mock.patch('ihan.eprint')
    def test_failed_payload(self, mock_subproc_popen, mock_eprint):
        process_mock = mock.Mock()
        attrs = {'stdout.readline.return_value': 'Test\nTest\n'}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock

        @mock.patch('requests.post',
                    side_effect=requests.exceptions.ConnectionError())
        def test_post(self, mock_get):
            feed_file('test', False, 1, '', 0)
            self.assertTrue(mock_subproc_popen.called)
            self.assertTrue(mock_eprint.called)

if __name__ == '__main__':
    unittest.main()
