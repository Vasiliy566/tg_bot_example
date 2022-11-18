from pyyaxml.search import YaSearch
y = YaSearch('prirodasaver', '03.183539997:d5c1bd989866bdaf80a6714ae7d951e9')
results = y.search('python', page=1)
for result in results.items:
    print(result.url)