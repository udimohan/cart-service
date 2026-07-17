"""Tests for catalog_00358."""

import pytest

from cartservice.generated.catalog_00358 import (
    Product_00358,
    bucket_by_tag_00358,
    is_valid_sku_00358,
    price_with_tax_00358,
)


def test_price_with_tax_00358():
    assert price_with_tax_00358(1000, 500) == 1050


def test_price_with_tax_negative_00358():
    with pytest.raises(ValueError):
        price_with_tax_00358(1000, -1)


def test_is_valid_sku_00358():
    assert is_valid_sku_00358("abc123")
    assert not is_valid_sku_00358("")


def test_bucket_by_tag_00358():
    p = Product_00358("s1", 100, ["a"])
    assert bucket_by_tag_00358([p]) == {"a": ["s1"]}
