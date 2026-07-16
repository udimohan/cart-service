"""Tests for catalog_00489."""

import pytest

from cartservice.generated.catalog_00489 import (
    Product_00489,
    bucket_by_tag_00489,
    is_valid_sku_00489,
    price_with_tax_00489,
)


def test_price_with_tax_00489():
    assert price_with_tax_00489(1000, 500) == 1050


def test_price_with_tax_negative_00489():
    with pytest.raises(ValueError):
        price_with_tax_00489(1000, -1)


def test_is_valid_sku_00489():
    assert is_valid_sku_00489("abc123")
    assert not is_valid_sku_00489("")


def test_bucket_by_tag_00489():
    p = Product_00489("s1", 100, ["a"])
    assert bucket_by_tag_00489([p]) == {"a": ["s1"]}
