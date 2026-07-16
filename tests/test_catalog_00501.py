"""Tests for catalog_00501."""

import pytest

from cartservice.generated.catalog_00501 import (
    Product_00501,
    bucket_by_tag_00501,
    is_valid_sku_00501,
    price_with_tax_00501,
)


def test_price_with_tax_00501():
    assert price_with_tax_00501(1000, 500) == 1050


def test_price_with_tax_negative_00501():
    with pytest.raises(ValueError):
        price_with_tax_00501(1000, -1)


def test_is_valid_sku_00501():
    assert is_valid_sku_00501("abc123")
    assert not is_valid_sku_00501("")


def test_bucket_by_tag_00501():
    p = Product_00501("s1", 100, ["a"])
    assert bucket_by_tag_00501([p]) == {"a": ["s1"]}
