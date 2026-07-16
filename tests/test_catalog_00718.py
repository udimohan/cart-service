"""Tests for catalog_00718."""

import pytest

from cartservice.generated.catalog_00718 import (
    Product_00718,
    bucket_by_tag_00718,
    is_valid_sku_00718,
    price_with_tax_00718,
)


def test_price_with_tax_00718():
    assert price_with_tax_00718(1000, 500) == 1050


def test_price_with_tax_negative_00718():
    with pytest.raises(ValueError):
        price_with_tax_00718(1000, -1)


def test_is_valid_sku_00718():
    assert is_valid_sku_00718("abc123")
    assert not is_valid_sku_00718("")


def test_bucket_by_tag_00718():
    p = Product_00718("s1", 100, ["a"])
    assert bucket_by_tag_00718([p]) == {"a": ["s1"]}
