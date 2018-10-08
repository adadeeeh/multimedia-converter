import os
import unittest

from convert import audio, image, video


def mock_convert(converter_function, filename, args):
    filename = 'test/files/' + filename
    output = '%s.%s' % (filename, args['output'])
    result = converter_function(filename, output, args)
    os.remove(output)
    return result


class TestImage(unittest.TestCase):
    args = {
        'resolution': '1000x1000',
        'colors': '120',
        'output': 'png'
    }

    def test_convert_lena(self):
        result = mock_convert(image.convert, 'lena.bmp', self.args)
        self.assertEqual(result, 0)

    def test_convert_sails(self):
        result = mock_convert(image.convert, 'sails.bmp', self.args)
        self.assertEqual(result, 0)


class TestAudio(unittest.TestCase):
    args = {
        'bitrate': '128k',
        'sample_rate': 48000,
        'output': 'mp3'
    }

    def test_convert_audio(self):
        result = mock_convert(audio.convert, 'rain.wav', self.args)
        self.assertEqual(result, 0)

    def test_convert_wolves(self):
        result = mock_convert(audio.convert, 'wolves.wav', self.args)
        self.assertEqual(result, 0)


class TestVideo(unittest.TestCase):
    args = {
        'frame_size': '1000x1000',
        'frame_rate': '120',
        'bitrate': '128k',
        'sample_rate': 48000,
        'output': 'mkv'
    }

    def test_convert_video_1(self):
        result = mock_convert(video.convert, 'Video1.WMV', self.args)
        self.assertEqual(result, 0)

    def test_convert_video_2(self):
        result = mock_convert(video.convert, 'Video2.WMV', self.args)
        self.assertEqual(result, 0)
        
        
if __name__ == '__main__':
    unittest.main()