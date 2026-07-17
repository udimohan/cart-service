"""Tests for catalog_00644."""

import pytest

from cartservice.generated.catalog_00644 import (
    Product_00644,
    bucket_by_tag_00644,
    is_valid_sku_00644,
    price_with_tax_00644,
)


def test_price_with_tax_00644():
    assert price_with_tax_00644(1000, 500) == 1050


def test_price_with_tax_negative_00644():
    with pytest.raises(ValueError):
        price_with_tax_00644(1000, -1)


def test_is_valid_sku_00644():
    assert is_valid_sku_00644("abc123")
    assert not is_valid_sku_00644("")


def test_bucket_by_tag_00644():
    p = Product_00644("s1", 100, ["a"])
    assert bucket_by_tag_00644([p]) == {"a": ["s1"]}
