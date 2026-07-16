"""Tests for catalog_00352."""

import pytest

from cartservice.generated.catalog_00352 import (
    Product_00352,
    bucket_by_tag_00352,
    is_valid_sku_00352,
    price_with_tax_00352,
)


def test_price_with_tax_00352():
    assert price_with_tax_00352(1000, 500) == 1050


def test_price_with_tax_negative_00352():
    with pytest.raises(ValueError):
        price_with_tax_00352(1000, -1)


def test_is_valid_sku_00352():
    assert is_valid_sku_00352("abc123")
    assert not is_valid_sku_00352("")


def test_bucket_by_tag_00352():
    p = Product_00352("s1", 100, ["a"])
    assert bucket_by_tag_00352([p]) == {"a": ["s1"]}
