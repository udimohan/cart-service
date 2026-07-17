"""Tests for catalog_00289."""

import pytest

from cartservice.generated.catalog_00289 import (
    Product_00289,
    bucket_by_tag_00289,
    is_valid_sku_00289,
    price_with_tax_00289,
)


def test_price_with_tax_00289():
    assert price_with_tax_00289(1000, 500) == 1050


def test_price_with_tax_negative_00289():
    with pytest.raises(ValueError):
        price_with_tax_00289(1000, -1)


def test_is_valid_sku_00289():
    assert is_valid_sku_00289("abc123")
    assert not is_valid_sku_00289("")


def test_bucket_by_tag_00289():
    p = Product_00289("s1", 100, ["a"])
    assert bucket_by_tag_00289([p]) == {"a": ["s1"]}
