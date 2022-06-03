#!/usr/bin/env python

import pytest
import urllib.request

import ps_library as mylib

url='http://ftp.uk.debian.org/debian/dists/stable/main/'
    
def test_is_up_repository():
    
    code = urllib.request.urlopen(url).getcode()
    assert code == 200
    
@pytest.mark.parametrize("arch", ['amd64', 'udeb-amd64', 'udeb-all', 'udeb-amd64','udeb-arm64','udeb-armel','udeb-armhf', 'udeb-i386','udeb-mips64el', 'udeb-mipsel','udeb-ppc64el', 'udeb-s390x'])
def test_get_links(arch):
    
    has_link = len(mylib.get_links(url, arch))
    assert has_link > 0

@pytest.mark.parametrize("arch, count", [('amd64', 138726), ('udeb-amd64', 2097), ('udeb-all', 1246), ('udeb-amd64', 2097), ('udeb-arm64', 2459), ('udeb-armel', 1647), ('udeb-armhf', 3195), ('udeb-i386', 2471), ('udeb-mips64el', 1801), ('udeb-mipsel', 1795), ('udeb-ppc64el', 1793), ('udeb-s390x', 1548)])
def test_sum_per_arch(arch, count):

    top10 = mylib.main(arch)
    total_count = sum(j for i, j in top10)
    assert total_count == count
    
