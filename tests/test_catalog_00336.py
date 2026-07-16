"""Tests for catalog_00336."""

import pytest

from cartservice.generated.catalog_00336 import (
    Product_00336,
    bucket_by_tag_00336,
    is_valid_sku_00336,
    price_with_tax_00336,
)


def test_price_with_tax_00336():
    assert price_with_tax_00336(1000, 500) == 1050


def test_price_with_tax_negative_00336():
    with pytest.raises(ValueError):
        price_with_tax_00336(1000, -1)


def test_is_valid_sku_00336():
    assert is_valid_sku_00336("abc123")
    assert not is_valid_sku_00336("")


def test_bucket_by_tag_00336():
    p = Product_00336("s1", 100, ["a"])
    assert bucket_by_tag_00336([p]) == {"a": ["s1"]}
