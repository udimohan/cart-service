"""Tests for catalog_01400."""

import pytest

from cartservice.generated.catalog_01400 import (
    Product_01400,
    bucket_by_tag_01400,
    is_valid_sku_01400,
    price_with_tax_01400,
)


def test_price_with_tax_01400():
    assert price_with_tax_01400(1000, 500) == 1050


def test_price_with_tax_negative_01400():
    with pytest.raises(ValueError):
        price_with_tax_01400(1000, -1)


def test_is_valid_sku_01400():
    assert is_valid_sku_01400("abc123")
    assert not is_valid_sku_01400("")


def test_bucket_by_tag_01400():
    p = Product_01400("s1", 100, ["a"])
    assert bucket_by_tag_01400([p]) == {"a": ["s1"]}
