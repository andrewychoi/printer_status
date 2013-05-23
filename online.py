import socket
import urllib2
from bs4 import BeautifulSoup

# canonical IP and hostname
printer_ip = "140.180.129.26"
printer_hostname = "club-ivy-hpm602dn.princeton.edu"

def check_online():

    # use if one is more consistent than the other, i.e. DDNS
    # print socket.getaddrinfo(printer_hostname, 80)
    # print socket.gethostbyaddr(printer_ip)

    status_url = "http://" + printer_hostname

    status_page = urllib2.urlopen(status_url)

    html_doc = status_page.read()

    # clean up, not necessary
    status_page.close()

    html_soup = BeautifulSoup(html_doc)

    # print html_soup.prettify()

    status_target_id = "MachineStatus"
    paper1_target_id = "TrayBinStatus_1"
    paper2_target_id = "TrayBinStatus_2"

    status = html_soup.find_all(id = status_target_id)[0].text
    paper1 = html_soup.find_all(id = paper1_target_id)[0].text
    paper2 = html_soup.find_all(id = paper2_target_id)[0].text

    print status
    print paper1
    print paper2

if __name__ == "__main__":
    check_online()
