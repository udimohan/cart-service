"""Tests for catalog_00509."""

import pytest

from cartservice.generated.catalog_00509 import (
    Product_00509,
    bucket_by_tag_00509,
    is_valid_sku_00509,
    price_with_tax_00509,
)


def test_price_with_tax_00509():
    assert price_with_tax_00509(1000, 500) == 1050


def test_price_with_tax_negative_00509():
    with pytest.raises(ValueError):
        price_with_tax_00509(1000, -1)


def test_is_valid_sku_00509():
    assert is_valid_sku_00509("abc123")
    assert not is_valid_sku_00509("")


def test_bucket_by_tag_00509():
    p = Product_00509("s1", 100, ["a"])
    assert bucket_by_tag_00509([p]) == {"a": ["s1"]}
