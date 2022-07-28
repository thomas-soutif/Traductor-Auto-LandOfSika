import unittest
from source.XmlManager.TheLandOfSika import XmlManagerTheLandOfSika


class TheLandOfSikaTest(unittest.TestCase):
    xml_manager = None

    def __init__(self):
        super().__init__()
        self.xml_manager = XmlManagerTheLandOfSika("xml_generic_the_land_of_sika.xml")

    def test_check_xml_file(self):
        self.assertIsNone(self.xml_manager.check_xml_file())


if __name__ == '__main__':
    unittest.main()
