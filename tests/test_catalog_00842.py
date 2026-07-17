"""Tests for catalog_00842."""

import pytest

from cartservice.generated.catalog_00842 import (
    Product_00842,
    bucket_by_tag_00842,
    is_valid_sku_00842,
    price_with_tax_00842,
)


def test_price_with_tax_00842():
    assert price_with_tax_00842(1000, 500) == 1050


def test_price_with_tax_negative_00842():
    with pytest.raises(ValueError):
        price_with_tax_00842(1000, -1)


def test_is_valid_sku_00842():
    assert is_valid_sku_00842("abc123")
    assert not is_valid_sku_00842("")


def test_bucket_by_tag_00842():
    p = Product_00842("s1", 100, ["a"])
    assert bucket_by_tag_00842([p]) == {"a": ["s1"]}
