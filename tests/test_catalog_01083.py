"""Tests for catalog_01083."""

import pytest

from cartservice.generated.catalog_01083 import (
    Product_01083,
    bucket_by_tag_01083,
    is_valid_sku_01083,
    price_with_tax_01083,
)


def test_price_with_tax_01083():
    assert price_with_tax_01083(1000, 500) == 1050


def test_price_with_tax_negative_01083():
    with pytest.raises(ValueError):
        price_with_tax_01083(1000, -1)


def test_is_valid_sku_01083():
    assert is_valid_sku_01083("abc123")
    assert not is_valid_sku_01083("")


def test_bucket_by_tag_01083():
    p = Product_01083("s1", 100, ["a"])
    assert bucket_by_tag_01083([p]) == {"a": ["s1"]}
