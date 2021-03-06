"""index.py: Main File."""
__author__ = "Muhammad Usman Naeem"
__license__ = "GPL-3"
__version__ = "1.0.0"
__administrator__ = "Muhammad Usman Naeem"
__developers__ = "Muhammad Usman Naeem"
__email__ = "usman.naeem2212@gmail.com"
__status__ = "Production"

from src.sitemap import sitemap
conn = sitemap()

req_url = "https://www.muhammadumerfarooq.me"

if conn.is_image(req_url) :
    xml_1 = conn.get_xml(req_url, "url")
    print(conn.validate(xml_1, "url"))
    conn.write_on_file(xml_1, "sitemap_1.xml")

    xml_2 = conn.get_xml(req_url, "image")
    print(conn.validate(xml_2, "image"))
    conn.write_on_file(xml_2, "sitemap_2.xml")
else :
    xml = conn.get_xml(req_url, "url")
    print(conn.validate(xml, "url"))
    conn.write_on_file(xml, "sitemap.xml")
