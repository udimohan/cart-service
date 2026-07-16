"""Tests for catalog_00314."""

import pytest

from cartservice.generated.catalog_00314 import (
    Product_00314,
    bucket_by_tag_00314,
    is_valid_sku_00314,
    price_with_tax_00314,
)


def test_price_with_tax_00314():
    assert price_with_tax_00314(1000, 500) == 1050


def test_price_with_tax_negative_00314():
    with pytest.raises(ValueError):
        price_with_tax_00314(1000, -1)


def test_is_valid_sku_00314():
    assert is_valid_sku_00314("abc123")
    assert not is_valid_sku_00314("")


def test_bucket_by_tag_00314():
    p = Product_00314("s1", 100, ["a"])
    assert bucket_by_tag_00314([p]) == {"a": ["s1"]}
