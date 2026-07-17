"""Tests for catalog_00400."""

import pytest

from cartservice.generated.catalog_00400 import (
    Product_00400,
    bucket_by_tag_00400,
    is_valid_sku_00400,
    price_with_tax_00400,
)


def test_price_with_tax_00400():
    assert price_with_tax_00400(1000, 500) == 1050


def test_price_with_tax_negative_00400():
    with pytest.raises(ValueError):
        price_with_tax_00400(1000, -1)


def test_is_valid_sku_00400():
    assert is_valid_sku_00400("abc123")
    assert not is_valid_sku_00400("")


def test_bucket_by_tag_00400():
    p = Product_00400("s1", 100, ["a"])
    assert bucket_by_tag_00400([p]) == {"a": ["s1"]}
