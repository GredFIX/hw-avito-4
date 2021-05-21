import pytest

from issue import Advert


@pytest.mark.parametrize(
    'given, expect_error',
    [
        ({'title': 'python', 'price': -2}, ValueError),
        ({'price': 1}, KeyError),
    ]
)
def test_validation(given, expect_error):
    with pytest.raises(expect_error):
        Advert(given)


def test_default_price():
    advert = Advert({'title': 'python'})
    assert advert.price == 0


def test_corgi_in_colors(capfd):
    corgi = Advert({'title': 'Вельш-корги', 'price': 1000})
    assert '\x1b[1;33;40mВельш-корги | 1000 ₽' == repr(corgi)


def test_has_fields_from_dict():
    obj = {
        "title": "python",
        "price": 10,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }
    advert = Advert(obj)

    assert advert.title == obj['title']
    assert advert.price == obj['price']
    assert advert.location.address == obj['location']['address']
    assert advert.location.metro_stations == obj['location']['metro_stations']
