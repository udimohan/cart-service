"""Tests for catalog_01686."""

import pytest

from cartservice.generated.catalog_01686 import (
    Product_01686,
    bucket_by_tag_01686,
    is_valid_sku_01686,
    price_with_tax_01686,
)


def test_price_with_tax_01686():
    assert price_with_tax_01686(1000, 500) == 1050


def test_price_with_tax_negative_01686():
    with pytest.raises(ValueError):
        price_with_tax_01686(1000, -1)


def test_is_valid_sku_01686():
    assert is_valid_sku_01686("abc123")
    assert not is_valid_sku_01686("")


def test_bucket_by_tag_01686():
    p = Product_01686("s1", 100, ["a"])
    assert bucket_by_tag_01686([p]) == {"a": ["s1"]}
