"""Tests for catalog_00640."""

import pytest

from cartservice.generated.catalog_00640 import (
    Product_00640,
    bucket_by_tag_00640,
    is_valid_sku_00640,
    price_with_tax_00640,
)


def test_price_with_tax_00640():
    assert price_with_tax_00640(1000, 500) == 1050


def test_price_with_tax_negative_00640():
    with pytest.raises(ValueError):
        price_with_tax_00640(1000, -1)


def test_is_valid_sku_00640():
    assert is_valid_sku_00640("abc123")
    assert not is_valid_sku_00640("")


def test_bucket_by_tag_00640():
    p = Product_00640("s1", 100, ["a"])
    assert bucket_by_tag_00640([p]) == {"a": ["s1"]}
