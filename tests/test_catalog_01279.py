"""Tests for catalog_01279."""

import pytest

from cartservice.generated.catalog_01279 import (
    Product_01279,
    bucket_by_tag_01279,
    is_valid_sku_01279,
    price_with_tax_01279,
)


def test_price_with_tax_01279():
    assert price_with_tax_01279(1000, 500) == 1050


def test_price_with_tax_negative_01279():
    with pytest.raises(ValueError):
        price_with_tax_01279(1000, -1)


def test_is_valid_sku_01279():
    assert is_valid_sku_01279("abc123")
    assert not is_valid_sku_01279("")


def test_bucket_by_tag_01279():
    p = Product_01279("s1", 100, ["a"])
    assert bucket_by_tag_01279([p]) == {"a": ["s1"]}
