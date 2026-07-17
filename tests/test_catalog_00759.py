"""Tests for catalog_00759."""

import pytest

from cartservice.generated.catalog_00759 import (
    Product_00759,
    bucket_by_tag_00759,
    is_valid_sku_00759,
    price_with_tax_00759,
)


def test_price_with_tax_00759():
    assert price_with_tax_00759(1000, 500) == 1050


def test_price_with_tax_negative_00759():
    with pytest.raises(ValueError):
        price_with_tax_00759(1000, -1)


def test_is_valid_sku_00759():
    assert is_valid_sku_00759("abc123")
    assert not is_valid_sku_00759("")


def test_bucket_by_tag_00759():
    p = Product_00759("s1", 100, ["a"])
    assert bucket_by_tag_00759([p]) == {"a": ["s1"]}
