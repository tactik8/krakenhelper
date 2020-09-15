from kraken_helper.helper import Url

from kraken_helper.schema import Schema



url = 'https://www.test.com'

u = Url(url)

domain = u.get_domain()

print(domain)


s = Schema()


print(s.get_test())


main_record = s.get_main_record()


print(main_record)


